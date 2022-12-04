import sys


def pair_def_to_sets(string_pair):
    """
    input: 1-5,7-9
    output sets of 2 ranges
    """
    a, b = string_pair.split(',')

    a1,a2 = map(int, a.split('-'))
    b1,b2 = map(int, b.split('-'))

    return set(range(a1, a2+1)), set(range(b1, b2+1))


def main(filename):
    lines = open(filename).read().strip().split('\n')
    pairs = [pair_def_to_sets(l) for l in lines]

    contained = [(a,b) for a,b in pairs if a - b == set() or b - a == set()]
    do_overlap = [(a,b) for a,b in pairs if a & b != set() ]

    print(len(contained))
    print(len(do_overlap))


if __name__ == "__main__":
    main(sys.argv[1])