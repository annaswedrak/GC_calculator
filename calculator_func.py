#Write Python Code:
#Read the DNA Sequence: Input a DNA sequence. This can be hardcoded for simplicity, or you can write a function to read sequences from a file.
#Calculate GC Content: Write a function that counts the number of 'G' and 'C' characters in the sequence and divides this by the total length of the sequence.
#Output the Result: Print the GC content as a percentage.
#Test Your Code: Use known sequences to test if your code gives the correct GC content.
from reading_single_seq import read_single_sequence



#this function takes a sequence as a string and calculates GC%
def calculate_GC_percentage(sequence):
    GC_num = 0
    for nucleotide in sequence:
        if nucleotide == "G" or nucleotide == "C":
            GC_num += 1
    GC_percentage = (GC_num / len(sequence))* 100
    return GC_percentage

seq = read_single_sequence('CS_acid_synth.fasta')

print(f'Percentage of GC in sample sequence is {calculate_GC_percentage(seq)}')
