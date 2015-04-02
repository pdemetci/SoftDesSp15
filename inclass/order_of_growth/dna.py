""" Evaluate the performance of various DNA proessing algorithms """

from random import randint
import time
import matplotlib as plt

def generate_random_dna(n):
    """ Generate a random DNA sequence of length n """
    dna_list = []
    nucleotides = ['A','C','G','T']
    for i in range(n):
        r = randint(0,3)
        dna_list.append(nucleotides[r])
    return "".join(dna_list)

def get_complement(c):
    """ Returns the complimentary nucleotide to c """
    if c == 'A':
        return 'T'
    if c == 'C':
        return 'G'
    if c == 'G':
        return 'C'
    if c == 'T':
        return 'A'

def reverse_complement_1(dna):
    """ Method 2 for computing the reverse complementary sequence of DNA
        for the specfied DNA sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    >>> reverse_complement_1("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> reverse_complement_1("CCGCGTTCA")
    'TGAACGCGG'
    """
    return_val = ""
    for c in dna:
        return_val = get_complement(c) + return_val 
    return return_val

def reverse_complement_2(dna):
    """ Method 1 for Computing the reverse complementary sequence of DNA
        for the specfied DNA sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    >>> reverse_complement_2("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> reverse_complement_2("CCGCGTTCA")
    'TGAACGCGG'
    """
    return_val = []
    for c in reversed(dna):
        return_val.append(get_complement(c))
    return "".join(return_val)

if __name__ == '__main__':
    time_dict1={}
    time_dict2={}
    for i in range(100,1001):
        dna_length = i
        import doctest
        doctest.testmod()
        dna = generate_random_dna(dna_length)
        start_time = time.time()
        rev_complement = reverse_complement_1(dna)
        stop_time = time.time()
        time1= stop_time - start_time
        time_dict1[i]=time1

        dna = generate_random_dna(dna_length)
        start_time = time.time()
        rev_complement = reverse_complement_2(dna)
        stop_time = time.time()

        time2= stop_time - start_time
        time_dict2[i]=time2

    x1=[]
    y1=[]
    for i in time_dict1:
        x1.append(i)
        y1.append(time_dict1[i])
    x2=[]
    y2=[]
    for i in time_dict2:
        x2.append(i)
        y2.append(time_dict2[i])
    plt.plot(x1,y1)

