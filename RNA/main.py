# title: Transcribing DNA into RNA
# id: RNA

dataset = ['G','A','T','G','G','A','A','C','T','T','G','A','C','T','A','C','G','T','A','A','A','T','T']

def main():
    for char in dataset:
        if char == 'T':
            print('U', end='')
        else:
            print(char, end='')
    print()

if __name__ == '__main__':
    main()
