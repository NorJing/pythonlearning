# Run in Python 3.5
import math
"""
0 ≤ P < Q < R < N;
sequence [A[P], A[P+1], ..., A[Q]] is strictly decreasing,
i.e. A[P] > A[P+1] > ... > A[Q];
sequence A[Q], A[Q+1], ..., A[R] is strictly increasing,
i.e. A[Q] < A[Q+1] < ... < A[R].
The depth of a pit (P, Q, R) is the number min{A[P] − A[Q], A[R] − A[Q]}.
"""

def deepestPit(A):
    P = 0
    Q = -1
    R = -1
    depth = 0
    for i in range(1, len(A)):
        if Q < 0 and (A[i] >= A[i-1]):
            Q = i - 1
        # Find R
        if (Q >= 0 and R < 0) and (A[i] <= A[i-1] or i+1 == len(A)):
            if A[i] <= A[i-1]:
                R = i - 1
            else:
                R = i

            print(A[P], A[Q], A[R])
            depth = max(depth, min((A[P]-A[Q]), (A[R]-A[Q])))
            P = i - 1
            Q = -1
            R = -1

    return depth

if __name__ == '__main__':
    A = [None] * 10

    A[0] = 0
    A[1] = 1
    A[2] = 3
    A[3] = -2
    A[4] = 0
    A[5] = 1
    A[6] = 0
    A[7] = -3
    A[8] = 2
    A[9] = 3

    print(A)
    print(deepestPit(A))
    # print(list1)