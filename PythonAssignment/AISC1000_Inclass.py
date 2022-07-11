import sys

def main():

    FILE_PATH = "/Users/jeetu/Jupyter/Data Science/Loyalist/Deterministic Models and Optimization 02/Assignments/Week 10/Assignment.csv"
    #Reading CSV file...
    f = open(FILE_PATH, "r")
    char = f.read() #Read full file
    print(char)

    f.close()

    #Writing CSV file...
    f = open(FILE_PATH, "a")
    f.write("END,END,END\n")
    f.close()

    #Reading again CSV file...
    f = open(FILE_PATH, "r")
    line = f.readline()
    while line:
        print(line) #Read line by line
        line = f.readline()
    f.close()
    


def read():
    sys.stdin  = open('../input.txt', 'r')
    sys.stdout = open('../output.txt', 'w')


if __name__ == "__main__":
    read()
    main()