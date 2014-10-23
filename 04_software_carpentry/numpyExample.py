# coding: utf-8

# ##Sieve of Eratosthenes
import argparse

import numpy as np


def sieve_of_eratosthenes(n):
    """sieveOfEratosthenes(n): return the list of the primes < n."""
    # Code from: <dickinsm@gmail.com>, Nov 30 2006
    # http://groups.google.com/group/comp.lang.python/msg/f1f10ced88c68c2d
    if n <= 2:
        return []
    sieve = range(3, n, 2)
    top = len(sieve)
    for si in sieve:
        if si:
            bottom = (si * si - 3) / 2
            if bottom >= top:
                break
            sieve[bottom::si] = [0] * -((bottom - top) / si)
    return np.array([2] + [el for el in sieve if el])

# Simple Argv/Output
# if __name__ == '__main__':
# if len(sys.argv) != 2:
#         print 'One Argument is mandatory'
#     else:
#         n = sys.argv[1]
#         print 'List of primes numbers <', n
#         print sieveOfEratosthenes(int(n))

# Argparse example Argv/Output
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="calculate X to the power of Y")
    parser.add_argument("n", help="return primes until n", type=int)
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="increase output verbosity")
    args = parser.parse_args()
    n = args.n
    answer = sieve_of_eratosthenes(n)
    if args.verbose:
        print "List of primes numbers < {} is: \n{}".format(args.n, answer)
    else:
        print answer
    print