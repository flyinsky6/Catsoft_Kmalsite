import numpy as np
import pandas as pd

def sliding_slice_fasta(sequence):
    fragments = []
    slices = []
    lines = sequence.split('\n')
    indices = []
    seq_name =''
    header = ''
    for line in lines:
        if line.startswith('>'):
            seq_name = line[1:].split('|')[0:]
            header = line
        else:
            current_indices = [i for i, letter in enumerate(line) if letter == 'K']
            indices.extend(current_indices)
            for k in current_indices:
                if k - 16 < 0:
                    padding_left = (16 - k) * '-'
                    left = padding_left + line[0:k]
                else:
                    left = line[k - 16:k]
                if len(line) - (k + 1) < 16:
                    padding_right = (18 + k - len(line)) * '-'
                    right = line[k:-1]+ padding_right
                elif len(line) - (k + 1) == 16:
                    right = line[k:-1] + '-'
                else:
                    right = line[k:k + 17]
                seq = left + right

                fragments.append(header+'\n'+seq)
                # if '-' in seq:
                #     seqs = seq.replace('-', '')
                slices.append((seq_name, seq, k))

    with open('fragments.fasta', 'w') as output_file:
        output_file.write('\n'.join(fragments))

    fragments_fasta=r'fragments.fasta'

    return fragments_fasta, slices, indices
