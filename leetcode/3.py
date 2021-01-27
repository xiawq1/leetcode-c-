from torch.utils.data import Dataset
from torch.utils.data.sampler import Sampler
# import utils  ##############
import numpy as np
import torch
import random
from rdkit import Chem
from scipy.spatial import distance_matrix
from rdkit.Chem.rdmolops import GetAdjacencyMatrix
import pickle

random.seed(0)
import numpy as np
import torch
from scipy import sparse
import os.path
import time
import torch.nn as nn
from ase import Atoms, Atom

# from rdkit.Contrib.SA_Score.sascorer import calculateScore
# from rdkit.Contrib.SA_Score.sascorer
# import deepchem as dc

N_atom_features = 28


def set_cuda_visible_device(ngpus):
    import subprocess
    import os
    empty = []
    for i in range(8):
        command = 'nvidia-smi -i ' + str(i) + ' | grep "No running" | wc -l'
        output = subprocess.check_output(command, shell=True).decode("utf-8")
        # print('nvidia-smi -i '+str(i)+' | grep "No running" | wc -l > empty_gpu_check')
        if int(output) == 1:
            empty.append(i)
    if len(empty) < ngpus:
        print('avaliable gpus are less than required')
        exit(-1)
    cmd = ''
    for i in range(ngpus):
        cmd += str(empty[i]) + ','
    return cmd


def initialize_model(model, device, load_save_file=False):
    if load_save_file:
        model.load_state_dict(torch.load(load_save_file))
    else:
        for param in model.parameters():
            if param.dim() == 1:
                continue
                nn.init.constant(param, 0)
            else:
                # nn.init.normal(param, 0.0, 0.15)
                nn.init.xavier_normal_(param)

    if torch.cuda.device_count() > 1:
        print("Let's use", torch.cuda.device_count(), "GPUs!")
        # dim = 0 [30, xxx] -> [10, ...], [10, ...], [10, ...] on 3 GPUs
        model = nn.DataParallel(model)
    model.to(device)
    return model


def one_of_k_encoding(x, allowable_set):
    if x not in allowable_set:
        raise Exception("input {0} not in allowable set{1}:".format(x, allowable_set))
    # print list((map(lambda s: x == s, allowable_set)))
    return list(map(lambda s: x == s, allowable_set))


def one_of_k_encoding_unk(x, allowable_set):
    """Maps inputs not in the allowable set to the last element."""
    if x not in allowable_set:
        x = allowable_set[-1]
    return list(map(lambda s: x == s, allowable_set))


def atom_feature(m, atom_i, i_donor, i_acceptor):
    atom = m.GetAtomWithIdx(atom_i)
    return np.array(one_of_k_encoding_unk(atom.GetSymbol(),
                                          ['C', 'N', 'O', 'S', 'F', 'P', 'Cl', 'Br', 'B', 'H']) +
                    one_of_k_encoding(atom.GetDegree(), [0, 1, 2, 3, 4, 5]) +
                    one_of_k_encoding_unk(atom.GetTotalNumHs(), [0, 1, 2, 3, 4]) +
                    one_of_k_encoding_unk(atom.GetImplicitValence(), [0, 1, 2, 3, 4, 5]) +
                    [atom.GetIsAromatic()])  # (10, 6, 5, 6, 1) --> total 28


def get_atom_feature(m, is_ligand=True):
    n = m.GetNumAtoms()  ######获取原子的个数，，m是smiles字符串吗
    H = []
    for i in range(n):
        H.append(atom_feature(m, i, None, None))
    H = np.array(H)
    if is_ligand:
        H = np.concatenate([H, np.zeros((n, 28))], 1)
    else:
        H = np.concatenate([np.zeros((n, 28)), H], 1)
    return H


class MolDataset(Dataset):

    def __init__(self, keys, data_dir):
        self.keys = keys
        self.data_dir = data_dir

    def __len__(self):
        return len(self.keys)

    def __getitem__(self, idx):
        # idx = 0
        key = self.keys[idx]
        with open(self.data_dir + '/' + key, 'rb') as f:
            m1, m2 = pickle.load(f)

        # prepare ligand
        n1 = m1.GetNumAtoms()
        c1 = m1.GetConformers()[0]
        d1 = np.array(c1.GetPositions())
        adj1 = GetAdjacencyMatrix(m1) + np.eye(n1)
        H1 = get_atom_feature(m1, True)

        # prepare protein
        n2 = m2.GetNumAtoms()
        c2 = m2.GetConformers()[0]
        d2 = np.array(c2.GetPositions())
        adj2 = GetAdjacencyMatrix(m2) + np.eye(n2)
        H2 = get_atom_feature(m2, False)

        # aggregation
        H = np.concatenate([H1, H2], 0)
        agg_adj1 = np.zeros((n1 + n2, n1 + n2))
        agg_adj1[:n1, :n1] = adj1
        agg_adj1[n1:, n1:] = adj2
        agg_adj2 = np.copy(agg_adj1)
        dm = distance_matrix(d1, d2)
        agg_adj2[:n1, n1:] = np.copy(dm)
        agg_adj2[n1:, :n1] = np.copy(np.transpose(dm))

        # node indice for aggregation
        valid = np.zeros((n1 + n2,))
        valid[:n1] = 1

        # pIC50 to class
        Y = 1 if 'CHEMBL' in key else 0

        # if n1+n2 > 300 : return None
        sample = {
            'H': H, \
            'A1': agg_adj1, \
            'A2': agg_adj2, \
            'Y': Y, \
            'V': valid, \
            'key': key, \
            }

        return sample
with open(r"I:\xiawq\deep learning code\PYTORCH\分类回归\GNN_DTI-master\keys\train_dude_gene.pkl",'rb') as f:
    train_keys = pickle.load(f)
print(train_keys)
