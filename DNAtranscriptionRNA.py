def DTrans(DNA):
    RNA=DNA.replace("T","U")
    return RNA

if __name__=="__main__":
    with open("/Users/iftikarsunny/Downloads/rosalind_rna.txt") as f:
        line=f.read()
    with open("/Users/iftikarsunny/Downloads/rna_trans.txt","w") as f:
        f.write( DTrans(line))
