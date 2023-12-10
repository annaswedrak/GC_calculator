#a function that opens fasta file, removes header and return only sequence as a string (only for fasta files containing one sequence)

def read_single_sequence(file_path):
    with open(file_path,'r') as file:

        sequence = ''

        for line in file:
            line = line.strip()
            if not line.startswith('>'):
                sequence += line
    return sequence
