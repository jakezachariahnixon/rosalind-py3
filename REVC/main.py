# title: Complementing a Strand of DNA
# id: REVC

dataset = ['A','A','A','A','C','C','C','G','G','T']
comp = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

def main():
    for char in dataset:
        print(comp[char], end='')
    print()

if __name__ == '__main__':
    main()
