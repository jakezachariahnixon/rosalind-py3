# title: Counting Point Mutations
# id: HAMM

import sys

def main():
    with open("input.txt", 'r') as file:
        s1 = file.readline()
        s2 = file.readline()
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
