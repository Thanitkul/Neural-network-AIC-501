# File name : argument 1
# example row: "Hidden Layer: 9, Learning Rate: 0.200000, Epochs: 800, Accuracy: 0.920635"

# find the highest accuracy in the file and print the row out

import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 findHighestAcc.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    highest = 0
    highestrow = ""
    with open(filename, "r") as f:
        for line in f:
            acc = float(line.split()[-1])
            if acc > highest:
                highest = acc
                highestrow = line
    print(highestrow)

if __name__ == "__main__":
    main()
