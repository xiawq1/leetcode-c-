#coding:gbk

#ð������
def bubblesort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):   ######����������ÿ�ε����򶼻Ὣ�������ŵ����
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#ѡ��
def selectionSort(arr):
    for i in range(len(arr) - 1):
        # ��¼��С��������
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # i ������С��ʱ���� i ����С�����н���
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

selectionSort([8,2,1,3,10,7,18,4,1,5,2,14])

#��������
def insertionSort(arr):
    for i in range(len(arr)):
        preIndex = i-1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+1] = arr[preIndex]
            preIndex-=1
        arr[preIndex+1] = current
    return arr
insertionSort([8,1,3,10,18,4,1,5,2,14])
#�鲢����

def merge(s1,s2,s):
    """�������б���s1��s2��˳���ں�Ϊһ���б�s,sΪԭ�б�"""
    # j��i���൱������ָ���λ�ã�iָs1��jָs2
    i = j = 0
    while i+j<len(s):
        # j==len(s2)ʱ˵��s2�����ˣ�����s1û���겢��s1�и�λ������С��
        if j==len(s2) or (i<len(s1) and s1[i]<s2[j]):
            s[i+j] = s1[i]
            i += 1
        else:
            s[i+j] = s2[j]
            j += 1

def merge_sort(s):
    """�鲢����"""
    n = len(s)
    # ʣһ����û��ֱ�ӷ��أ���������
    if n < 2:
        return
    # ���
    mid = n // 2
    s1 = s[0:mid]
    s2 = s[mid:n]
    # �����еݹ��������
    merge_sort(s1)
    merge_sort(s2)
    # �ϲ�
    merge(s1,s2,s)




#ϣ������
def shellSort(arr):
    import math
    gap=1
    while(gap < len(arr)/3):
        gap = gap*3+1
    while gap > 0:
        for i in range(gap,len(arr)):
            temp = arr[i]
            j = i-gap
            while j >=0 and arr[j] > temp:
                arr[j+gap]=arr[j]
                j-=gap
            arr[j+gap] = temp
        gap = math.floor(gap/3)
    return arr