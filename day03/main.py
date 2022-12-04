import sys

def priority(item):
    """
    To help prioritize item rearrangement, every item type can be converted to a priority:
        Lowercase item types a through z have priorities 1 through 26.
        Uppercase item types A through Z have priorities 27 through 52.
    """
    if item.islower():
        return ord(item)-96  
    else:
        return ord(item)-38

def parse(filename):
    lines = open(filename).read().strip().split('\n')
    return lines

def part1(filename):
    lines = parse(filename)
    common_letters = []
    for line in lines:
        first_half = set(i for i in line[:len(line)//2]) 
        second_half = set(i for i in line[len(line)//2:])
        common_letter = first_half & second_half
        common_letters.append(list(common_letter)[0])

    print(sum(priority(l) for l in common_letters))

def part2(filename):
    lines = parse(filename)
    badges = []

    for i in range(0, len(lines), 3):
        badge =  set(i for i in lines[i]) & set(i for i in lines[i+1])  &  set(i for i in lines[i+2]) 
        badges.append(list(badge)[0])
    
    print(sum(priority(b) for b in badges))


if __name__ == "__main__":
    part1(sys.argv[1])
    part2(sys.argv[1])


    