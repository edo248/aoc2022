import sys

map_move={
    'A': 'R',
    'B': 'P',
    'C': 'S',
    'X': 'R',
    'Y': 'P',
    'Z': 'S'
}

map_end_result={
    'X': 0,
    'Y': 3,
    'Z': 6
}

def score(shape):
    _score = {
        'R': 1,
        'P': 2,
        'S': 3
    }
    return _score[shape]

def outcome(shapes):
    """
    Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. 
    If both players choose the same shape, the round instead ends in a draw.

    (0 if you lost, 3 if the round was a draw, and 6 if you won).
    """
    them,you = shapes

    your_score = score(you)

    if them == you:
        return 3 + your_score
    
    if (you == 'R' and them == 'S') or  (you == 'S' and them == 'P') or  (you == 'P' and them == 'R'):
        return 6 + your_score
    else:
        return 0 + your_score
    

def outcome2(expectation):
    """
    
    """
    them,end_result = expectation
   
    if end_result == 3:
        your_move = them
    elif end_result == 6:
        if them == 'S':
            your_move = 'R'
        if them == 'P':
            your_move = 'S'
        if them == 'R':
            your_move = 'P'            
    else:
        if them == 'S':
            your_move = 'P'
        if them == 'P':
            your_move = 'R'
        if them == 'R':
            your_move = 'S'  

    your_score = score(your_move)
    return your_score + end_result
    

def main(intput_file):
    pairs = [line.strip().split()  for line in open(intput_file) ]
    
    # part 1
    rounds = [(map_move[a],map_move[b]) for a,b in pairs]
    total1 = sum([outcome(round) for round in rounds])

    # part 2
    expectations = [(map_move[a],map_end_result[b]) for a,b in pairs]
    total2 = sum([outcome2(expectation) for expectation in expectations])

    print(total1)
    print(total2)
    

if __name__ == "__main__":
    main(sys.argv[1])