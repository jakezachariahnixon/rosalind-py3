# title: Computing GC Content
# id: GC

dna = "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"

def main():
    print(100*(dna.count("C")+dna.count("G"))/len(dna))

if __name__ == '__main__':
    main()
