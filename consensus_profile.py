from lib.fasta_import import *

def consensus_profile(FILE) :

    # import fasta file
    SEQ_LIST = list( fasta_import(FILE).values() )

    # instantiate empty dict to build matrix with
    COL = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    # instantiate reference list of bases
    BASES = ['A', 'C', 'G', 'T']

    # instantiate seq length
    SEQ_LENGTH = len(SEQ_LIST[0])

    # instantiate and generate matrix of size depending on seq length
    matrix = [COL.copy() for i in range(SEQ_LENGTH)]

    # loop over all sequences in seq list
    for seq in SEQ_LIST :

        # loop over every seq and increase the count of the base in that position
        for pos, base in enumerate(seq) :
            matrix[pos][base] += 1
            # print(f'{pos}: {matrix[pos]}')

    # print out the consensus string
    consensus_string = ''
    for pos in range(SEQ_LENGTH) :
        consensus_string += max( matrix[pos], key=lambda key: matrix[pos][key])

    print(consensus_string)
    # print out the matrix
    for base in BASES :
        out_string = ''
        out_string += f'{base}: '
        for entry in matrix :
            out_string += f'{str(entry[base])} '
        print(out_string)


if __name__ == '__main__' :
    print( consensus_profile('input.txt'))
