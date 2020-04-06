# title: Rabbits and Recurrence Relations
# id: FIB

import sys

def population(n, k):
    if n in [1, 2]:
        return 1
    else:
        return population(n-1, k) + (population(n-2, k) * k)

if __name__ == '__main__':
    with open('input.txt', 'r') as infile:
        n, k = map(int, infile.readline().split())
    print(population(n, k))
