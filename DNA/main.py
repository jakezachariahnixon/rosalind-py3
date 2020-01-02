# title: Counting DNA Nucleotides
# id: DNA

dataset = ['A','G','C','T','T','T','T','C','A','T','T','C','T','G','A','C','T','G','C','A','A','C','G','G','G','C','A','A','T','A','T','G','T','C','T','C','T','G','T','G','T','G','G','A','T','T','A','A','A','A','A','A','A','G','A','G','T','G','T','C','T','G','A','T','A','G','C','A','G','C']

def main():
    print(str(dataset.count('A')) + " " + str(dataset.count('C')) + " " + str(dataset.count('G')) + " " + str(dataset.count('T')))

if __name__ == '__main__':
    main()
