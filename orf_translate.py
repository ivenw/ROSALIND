from lib.fasta_import import *
from lib.reverse_complement import *
from lib.dna_to_rna import *
from lib.rna_to_protein import *

def orf_translate(FILE) :

    # define start and stop codons
    START_CODON = 'AUG'
    STOP_CODONS = ['UAG', 'UGA', 'UAA']
    # instatiate output translated protein dna_string list
    protein_str_list = []

    # import fasta file and convert the returning dict to list of only values
    dna_dna_str_list = list( fasta_import(FILE).values() )
    # append reverse complement to dna dna_string list
    dna_dna_str_list.append( reverse_complement(dna_dna_str_list[0]))

    # apply the following on sense and anti sense strand
    for dna_str in dna_dna_str_list :
        #convert dna str to rna
        rna_str = dna_to_rna(dna_str)

        # loop over rna string to first find a start codon
        for index, base in enumerate(rna_str) :
            codon = rna_str[index:index+3]

            # if start codon has been found next loop over the rest of the
            # rna string in codon steps (3) to find a stop codon
            if codon == START_CODON :
                for x in range(index+3, len(rna_str), 3) :
                    codon = rna_str[x:x+3]

                    # if closest stop codon has been found translate rna to
                    # protein string and break
                    if codon in STOP_CODONS :
                        protein_str = rna_to_protein(rna_str[index:x])
                        if protein_str in protein_str_list :
                            break
                        else :
                            protein_str_list.append(protein_str)
                        break

    for i in protein_str_list :
        print(i)

print(orf_translate('input.txt'))
