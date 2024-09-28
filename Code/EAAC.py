import random
import pandas as pd
import numpy as np
from collections import Counter
import os
import re

class Sequence(object):
    def __init__(self, file):
        self.file = file  # whole file path
        self.fasta_list = []  # 2-D list [sampleName, fragment, label, training or testing]
        self.sample_purpose = None  # 1-D ndarray, sample used as training dataset (True) or testing dataset(False)
        self.sequence_number = 0  # int: the number of samples
        self.sequence_type = ''  # DNA, RNA or Protein
        self.is_equal = False  # bool: sequence with equal length?
        self.minimum_length = 1  # int
        self.maximum_length = 0  # int
        self.minimum_length_without_minus = 1  # int
        self.maximum_length_without_minus = 0  # int
        self.error_msg = ''  # string

        self.fasta_list, self.sample_purpose, self.error_msg = self.read_fasta(self.file)
        self.sequence_number = len(self.fasta_list)

        if self.sequence_number > 0:
            self.is_equal, self.minimum_length, self.maximum_length, self.minimum_length_without_minus, self.maximum_length_without_minus = self.sequence_with_equal_length()
            self.sequence_type = self.check_sequence_type()


        else:
            self.error_msg = 'File format error.'

    def read_fasta(self, file):
        """
        read fasta sequence
        :param file:
        :return:
        """
        msg = ''
        if not os.path.exists(self.file):
            msg = 'Error: file %s does not exist.' % self.file
            return [], None, msg
        with open(file) as f:
            records = f.read()
        records = records.split('>')[1:]
        fasta_sequences = []
        for fasta in records:
            array = fasta.split('\n')
            header, sequence = array[0].split()[0], re.sub('[^ACDEFGHIKLMNPQRSTUVWY-]', '-', ''.join(array[1:]).upper())
            header_array = header.split('|')
            name = header_array[0]
            label = header_array[1] if len(header_array) >= 2 else '0'
            label_train = header_array[2] if len(header_array) >= 3 else 'training'
            fasta_sequences.append([name, sequence, label, label_train])
        sample_purpose = np.array([item[3] == 'training' for item in fasta_sequences])
        return fasta_sequences, sample_purpose, msg

    def sequence_with_equal_length(self):
        """
        Check if fasta sequence is in equal length
        :return:
        """
        length_set = set()
        length_set_1 = set()
        for item in self.fasta_list:
            length_set.add(len(item[1]))
            length_set_1.add(len(re.sub('-', '', item[1])))

        length_set = sorted(length_set)
        length_set_1 = sorted(length_set_1)
        if len(length_set) == 1:
            return True, length_set[0], length_set[-1], length_set_1[0], length_set_1[-1]
        else:
            return False, length_set[0], length_set[-1], length_set_1[0], length_set_1[-1]

    def check_sequence_type(self):
        """
        Specify sequence type (Protein, DNA or RNA)
        :return:
        """
        tmp_fasta_list = []
        if len(self.fasta_list) < 100:
            tmp_fasta_list = self.fasta_list
        else:
            random_index = random.sample(range(0, len(self.fasta_list)), 100)
            for i in random_index:
                tmp_fasta_list.append(self.fasta_list[i])

        sequence = ''
        for item in tmp_fasta_list:
            sequence += item[1]

        char_set = set(sequence)
        if 5 < len(char_set) <= 21:
            for line in self.fasta_list:
                line[1] = re.sub('[^ACDEFGHIKLMNPQRSTVWY]', '-', line[1])
            return 'Protein'
        elif 0 < len(char_set) <= 5 and 'T' in char_set:
            return 'DNA'
        elif 0 < len(char_set) <= 5 and 'U' in char_set:
            for line in self.fasta_list:
                line[1] = re.sub('U', 'T', line[1])
            return 'RNA'
        else:
            return 'Unknown'


class EAAC_Descriptor(Sequence):
    def __init__(self, file, kw):
        super(EAAC_Descriptor, self).__init__(file=file)
        self.kw = kw  # dict
        self.encoding_array = np.array([])  # 2-D ndarray with column name and index name
        self.column = 0  # int
        self.row = 0  # int
        """ variable for ACC descriptors """
        self.myDiIndex = {
            'AA': 0, 'AC': 1, 'AG': 2, 'AT': 3,
            'CA': 4, 'CC': 5, 'CG': 6, 'CT': 7,
            'GA': 8, 'GC': 9, 'GG': 10, 'GT': 11,
            'TA': 12, 'TC': 13, 'TG': 14, 'TT': 15
        }
        self.myTriIndex = {
            'AAA': 0, 'AAC': 1, 'AAG': 2, 'AAT': 3,
            'ACA': 4, 'ACC': 5, 'ACG': 6, 'ACT': 7,
            'AGA': 8, 'AGC': 9, 'AGG': 10, 'AGT': 11,
            'ATA': 12, 'ATC': 13, 'ATG': 14, 'ATT': 15,
            'CAA': 16, 'CAC': 17, 'CAG': 18, 'CAT': 19,
            'CCA': 20, 'CCC': 21, 'CCG': 22, 'CCT': 23,
            'CGA': 24, 'CGC': 25, 'CGG': 26, 'CGT': 27,
            'CTA': 28, 'CTC': 29, 'CTG': 30, 'CTT': 31,
            'GAA': 32, 'GAC': 33, 'GAG': 34, 'GAT': 35,
            'GCA': 36, 'GCC': 37, 'GCG': 38, 'GCT': 39,
            'GGA': 40, 'GGC': 41, 'GGG': 42, 'GGT': 43,
            'GTA': 44, 'GTC': 45, 'GTG': 46, 'GTT': 47,
            'TAA': 48, 'TAC': 49, 'TAG': 50, 'TAT': 51,
            'TCA': 52, 'TCC': 53, 'TCG': 54, 'TCT': 55,
            'TGA': 56, 'TGC': 57, 'TGG': 58, 'TGT': 59,
            'TTA': 60, 'TTC': 61, 'TTG': 62, 'TTT': 63
        }

    """ Protein descriptors """

    def Protein_EAAC(self):
        try:
            self.encoding_array = np.array([])

            if not self.is_equal:
                self.error_msg = 'EAAC descriptor need fasta sequence with equal length.'
                return False

            AA = 'ARNDCQEGHILKMFPSTWYV'
            encodings = []
            for i in self.fasta_list:
                sequence= i[1]
                code = []
                for j in range(len(sequence)):
                    if j < len(sequence) and j + self.kw['sliding_window'] <= len(sequence):
                        count = Counter(sequence[j:j + self.kw['sliding_window']])
                        for key in count:
                            count[key] = count[key] / len(sequence[j:j + self.kw['sliding_window']])
                        for aa in AA:
                            code.append(count[aa])
                encodings.append(code)

            self.encoding_array = np.array(encodings, dtype=str)
            self.column = self.encoding_array.shape[1]
            self.row = self.encoding_array.shape[0] - 1
            del encodings
            if self.encoding_array.shape[0] > 1:
                return True
            else:
                return False
        except Exception as e:
            self.error_msg = str(e)
            return False

