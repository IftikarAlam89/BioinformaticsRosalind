import re

def reverse_slicing(s):
    return s[::-1]

def revDNA(DNA1):
    rep={"A":"T","T":"A","C":"G","G":"C"}
    pattern=re.compile("|".join(rep.keys()))
    DNA2=pattern.sub(lambda m:rep[m.group(0)],DNA1)
    return reverse_slicing(DNA2)


if __name__=="__main__":
    with open("/Users/iftikarsunny/Downloads/rosalind_revc-4.txt") as f:
        line=f.read()
    with open("/Users/iftikarsunny/Downloads/revc2.txt","w") as f:
        f.write(revDNA(line))