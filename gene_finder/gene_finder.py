# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: YOUR NAME HERE

"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons, aa_table
import random
from load import load_seq

def shuffle_string(s):
    """ Shuffles the characters in the input string
        NOTE: this is a helper function, you do not have to modify this in any way """
    return ''.join(random.sample(s,len(s)))

### YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###


def get_complement(nucleotide):
    """ Returns the complementary nucleotide

        nucleotide: a nucleotide (A, C, G, or T) represented as a string
        returns: the complementary nucleotide

        I have added the last two tests for G and T because a syntax error while coding for 'G' or 'T' inputs could cause an error. Just because 'A' input
        yields to 'T' output, it doesn't guarantee a 'T' input will yield to 'A' output.
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    >>> get_complement('G') 
    'C'
    >>> get_complement('T')
    'A'
    """
    # TODO: implement this
    complement = ''
    if nucleotide == 'A':
        complement+='T'
    elif nucleotide== 'T':
        complement += 'A'
    elif nucleotide == 'C':
        complement += 'G'
    elif nucleotide == 'G':
        complement += 'C'
    #it'd be best to directly return complement instead of adding to a string that you return at the end.
    else:raise Exception('Invalid nucleotide')
    return complement


def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'
    """
    # TODO: implement this
    complement=''
    for x in range(len(dna)):
        complement += get_complement(dna[x])
    reverse_complement = complement[::-1]
    return reverse_complement
def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string

        I added one more test because the existing test covered of 2 the stop codons: TAG and TGA. To include the third one, TAA, I added the last test.
    >>> rest_of_ORF("ATGTGAA")
    'ATG'
    >>> rest_of_ORF("ATGAGATAGG")
    'ATGAGA'
    >>> rest_of_ORF("ATGAGAAGATAA")
    'ATGAGAAGA'
    """

    ORF=''
    for i in range(0, len(dna), 3):
        if dna[i:i+3] == 'TAG' or dna[i:i+3] == 'TAA' or dna[i:i+3] == 'TGA':
            #could use if dna[i:i+3] in ('TAG','TAA','TGA')
           return ORF
        else:
            ORF += dna[i:i+3]
    return ORF
    
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']

    """
    ALL_ORF = []
    i = 0
    while i < len(dna)-2:
        if dna[i:i+3] == 'ATG':
            ALL_ORF.append(rest_of_ORF(dna[i:]))
            i += len(rest_of_ORF(dna[i:]))
        else:
            i += 3
    return ALL_ORF

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs

    >>> find_all_ORFs("ATGCATGAATGTAG")
    ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']
    """
    ALL_ORF = []
    ALL_ORF += (find_all_ORFs_oneframe(dna))
    ALL_ORF += (find_all_ORFs_oneframe(dna[1:]))
    ALL_ORF += (find_all_ORFs_oneframe(dna[2:]))
    return ALL_ORF

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    ALL_ORF = []
    reverse_dna = get_reverse_complement(dna)
    ALL_ORF += find_all_ORFs(dna)
    ALL_ORF += find_all_ORFs(reverse_dna)
    return ALL_ORF
    

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """
    for i in find_all_ORFs_both_strands(dna):
        if max(len(i))== True:
            print i
    #A solution that would make snese would be:
   #ORFS = find_all_ORFs_both_strands(dna)
   #return max(ORFS, key=len)
   #please read the documentation for the max() function so you'll know what inputs it takes and gives.

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    for i in find_all_ORFs_both_strands(dna):
        print max(len(i))
    #good thought, but running this just runs max on an integer, when max expects a list of values. We should meet to go over what the correct answer is, as there is clearly a misunderstanding of what this problem is asking for. For reference, a solution that would make sense is:
   #ORFS = []
   #for i in range(num_trials):
   #    ORFS.append(longest_ORF(shuffle_string(dna)))
   #return max(ORFS, key=len)

def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
    """
    amino_acids = ''
    for i in range(0,len(dna)-2,3):
        codon = dna[i:i+3]
        if codon in aa_table:
            amino_acids += aa_table[codon]
    return amino_acids

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    threshold = longest_ORF_noncoding(dna, 1500)
    ORFS = find_all_ORFs_both_strands(dna)
    amino_acids_final = []
    for i in ORFS:
        if len(i) > threshold:
            amino_acid = coding_strand_to_AA(i)
            amino_acids_final.append(amino_acid)
    return amino_acids_final


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    dna = load_seq("./data/X73525.fa")
    amino_acids = gene_finder(dna, 1500)
    print amino_acids
