import sys

def findMax(A):
    maxNumber = 0
    maxNumberIndex = 0
    for x in range(len(A)):
        if x > maxNumber:
            maxNumber = A[x]
            maxNumberIndex = x
    print("index =", x)


if __name__ == '__main__':
    arr = sys.argv[1].split(',')
    arrInt = []
    for i in arr:
        arrInt.append(int( i ))
    findMax(arrInt)