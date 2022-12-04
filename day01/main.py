
import sys

def main(input_file):
    lines = [l.strip() for l in open(input_file)]

    expression = ""
    for line in lines:
        if line !="":
            expression += f" {line} +"
        else: 
            expression += "0,"

    expression += " 0"

    # part 1
    cmd = f"sorted([{expression}], reverse=True)[0]"
    print(eval(cmd))  # :D

    # part 2
    cmd = f"sum(sorted([{expression}], reverse=True)[0:3])"
    print(eval(cmd))  # :D


if __name__ == "__main__":
    main(sys.argv[1])