#DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999. Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
#Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

from reading_multiple_gene_fasta import read_fasta
from calculator_func import calculate_GC_percentage


def max_gc_percent(data):
    '''this function takes a fasta file data and returns a gene id with the highest GC percentage followed by the GC-content'''
    genes = read_fasta(data)
    GC_percentage = {}
    for k in genes:
        GC_percentage[k] = round(calculate_GC_percentage(genes[k]),2)
    print(GC_percentage)

    return GC_percentage


print(max_gc_percent('sample_data'))
