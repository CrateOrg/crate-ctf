#!/usr/bin/python3
#coding: utf-8
import sys, argparse



def isPrime(number):
    # Corner cases
    if number <= 1:
        return False
    if number <= 3:
        return True

    # This is checked according to that every prime are of the form 6n +- 1
    if number % 2 == 0 or number % 3 == 0:
        return False

    iteration = 5
    while iteration ** 2 <= number:
        if number % iteration == 0 or number % (iteration + 2) == 0:
            return False
        iteration += 6

    return True

# Driver program
def main(talet):
    if talet < 1:
        sys.exit('You must give a positive integer as input!')

    raknare = 0
    itsPrime = {False:-1}
    while itsPrime.get(True,-1) < 2:
        itsPrime = {isPrime(x):x for x in [talet-raknare,talet+raknare]}
        raknare += 1
#    if len(sys.argv) > 2:
#        print(itsPrime.get(True))
    return itsPrime.get(True)
    
if __name__ == "__main__":
    CLI=argparse.ArgumentParser()
    CLI.add_argument("-n", "--number_to_test", type=int, help='The number to test for primality.')
    args = CLI.parse_args()
    if len(sys.argv) > 2:
        print(main(args.number_to_test))
    else:
        main(int(sys.argv[1]))
