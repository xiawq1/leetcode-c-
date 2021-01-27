
#coding:gbk
# import urllib.parse
# import urllib.request

# url = 'https://www.uniprot.org/uploadlists/'
#
# # params = {
# # 'from': 'ACC+ID',
# # 'to': '	STRING_ID',
# # 'format': 'tab',
# # 'query': 'P40925 P40926 O43175 Q9UM73 P97793'
# # }
# params = {
# 'from': 'ID',
# 'to': 'ACC',
# 'format': 'tab',
# 'query': 'PRS45_HUMAN PRS46_HUMAN'
# }
#
# data = urllib.parse.urlencode(params)
# data = data.encode('utf-8')
# print(data)
# req = urllib.request.Request(url, data)
# with urllib.request.urlopen(req) as f:
#    response = f.read()
#
# a = response.decode('utf-8')
# f = open(r'I:\xiawq\deep learning code\protein\deepgo-master\yy.txt', 'w')
# f.write(a)
# f.close()

import urllib.parse
import urllib.request


def read_fasta1(filename):
    seqs = list()
    info = list()
    info1 = []
    seq = ''
    inf = ''
    inf1 = ''
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if seq != '':
                    seqs.append(seq)
                    info.append(inf)
                    info1.append(inf1)
                    seq = ''
                inf0 = line.split()

                inf = inf0[0]
                inf1 = inf0[1]

            else:
                seq += line
        seqs.append(seq)
        info.append(inf)
        info1.append(inf1)

    return info, info1, seqs


def id_mapping(t, savepath):

    url = 'https://www.uniprot.org/uploadlists/'

    params = {
        'from': 'ID',
        'to': 'ACC',
        'format': 'tab',
        'query': t
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }

    data = urllib.parse.urlencode(params)
    data = data.encode('utf-8')

    req = urllib.request.Request(url, data, headers)
    with urllib.request.urlopen(req) as f:
        response = f.read()

    a = response.decode('utf-8')
    f = open(savepath, 'w')
    f.write(a)
    f.close()
import pandas as pd
ac = pd.read_table(r"H:\xiawq文献\汇报\AC.txt").AC.values
ac = ' '.join(ac)
print(ac)
id_mapping(ac, r'H:\xiawq文献\汇报\re.txt')




# from sklearn.metrics import roc_auc_score, roc_curve, auc, accuracy_score, precision_recall_curve, f1_score, matthews_corrcoef, recall_score, precision_score
# file = open(r'H:\xiawq文献\汇报\results.txt', 'w')
# import numpy as np
# a = [[0.36183358,0.44764189, 0.47433308, 0.35115366, 0.94741227],
#  [0.060577,0.48504076, 0.39831256, 0.91480969, 0.84649642],
#  [0.35810782,0.37254948, 0.63642593, 0.56342727, 0.45424455],
#  [0.35437011,0.81709586, 0.1103983, 0.40092847, 0.62286414],
#  [0.29883094,0.5816668,0.96496323, 0.61803764, 0.71478765]]
# pre = []
# for i in range(len(a)):
#     eachline = (np.array(a[i]) > 0.5).astype(np.int)
#
#     pre.append(eachline)
# actual = [[1, 0, 0, 0, 1],
# [0, 0, 0, 1, 1],
# [0, 0, 1, 1, 0],
# [0, 0, 1, 0, 1],
# [0, 1, 0, 1, 1]]
# actual = np.array(actual)
# pre = np.array(pre)
# for i in range(5):
#     pre1 = pre[:, i]
#     tru1 = actual[:, i]
#
#     f_score = f1_score(tru1, pre1, average='micro')
#     recall = recall_score(tru1, pre1, average='micro')
#     precision = precision_score(tru1, pre1, average='micro')
#     mcc = matthews_corrcoef(tru1, pre1)
#     file.write(str(i) + '\t' + str(f_score) + '\t' + str(recall) + '\t' + str(precision) + '\t' + str(mcc) + '\n')