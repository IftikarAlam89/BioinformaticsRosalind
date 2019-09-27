import collections
def cnt_nuc(DNA):
    c=collections.Counter()
    for base in DNA:
        c[base]+=1

    return c


if __name__=="__main__":
    with open("/Users/iftikarsunny/Downloads/rosalind_dna-2.txt") as f:
        line=f.read()
    print(cnt_nuc(line))






