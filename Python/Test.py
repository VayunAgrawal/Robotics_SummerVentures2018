from math import sqrt
import sys


def myfunction (n):
    for i in range(1,int(sqrt(n)+1)):
        if n%i == 0:
         print  i, n/i

if __name__ == '__main__':
    n = int( sys.argv[1])
    myfunction(n)
    
