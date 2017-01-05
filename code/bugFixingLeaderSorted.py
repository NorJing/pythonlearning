#  Run in Python 2.7

def solution(A):
    n = len(A)
    L = [-1] + A
    count = 0
    # before: pos = (n + 1) / 2
    pos = (n/2) + 1
    candidate = L[pos]
    for i in xrange(1, n + 1):
        if (L[i] == candidate):
            count = count + 1
    if (count >= pos): # before: count > pos
        return candidate
    return -1

if __name__ == '__main__':
    A = [None] * 10
    A[0] = 2
    A[1] = 2
    A[2] = 2
    A[3] = 2
    A[4] = 2
    A[5] = 4
    A[6] = 4
    A[7] = 4
    A[8] = 4
    A[9] = 6
    a = solution(A)
    print a

    B=[None] * 5
    B[0] = 1
    B[1] = 1
    B[2] = 1
    B[3] = 2
    B[4] = 50
    b = solution(B)
    print b