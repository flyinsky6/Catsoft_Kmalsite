import pandas as pd
import numpy as np

def sliding_slice_dssp(str_):
    a = str_.splitlines()
    AA = ""
    Structure = ""
    n = 16

    for line in a:
        AA += line[13]
        Structure += line[16]

    Structure = Structure.replace(" ", '_')

    seq = []
    k = []
    str_list = []
    d = len(AA)

    for p in range(d):
        if AA[p] == 'K':
            if len(AA[p - n:p + n + 1]) == 2 * n + 1:
                seq.append(AA[p - n:p + n + 1])
                k.append(p + 1)
                str_list.append(Structure[p - n:p + n + 1])
            else:
                if len(AA[p - n:p]) < n:
                    se = '{0:X>{1}}{2}{3:X<{4}}'.format(AA[:p], n, AA[p], AA[p + 1:p + n + 1], n)
                    st = '{0:_>{1}}{2}{3:_<{4}}'.format(Structure[:p], n, Structure[p],
                                                        Structure[p + 1:p + n + 1], n)
                    seq.append(se)
                    k.append(p + 1)
                    str_list.append(st)
                if len(AA[p + 1:p + n + 1]) < n:
                    se = '{0:X>{1}}{2}{3:X<{4}}'.format(AA[p - n:p], n, AA[p], AA[p + 1:], n)
                    st = '{0:_>{1}}{2}{3:_<{4}}'.format(Structure[p - n:p], n, Structure[p], Structure[p + 1:],
                                                        n)
                    seq.append(se)
                    k.append(p + 1)
                    str_list.append(st)

    b = sorted(list(set(Structure)))

    def map_to_binary(m):
        g = {}
        for i, item in enumerate(m):
            g[item] = bin(i)[2:].zfill(3)
        return g

    h = []
    for o in str_list:
        r = ''
        for l in o:
            r += map_to_binary(b)[l]
        h.append(r)
    data = []
    for q in range(len(k)):
        row_data = []
        for j in range(len(h[q])):
            row_data.append(float(h[q][j]))
        data.append(row_data)
    df = pd.DataFrame(data)
    return df.to_numpy()
