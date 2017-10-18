import sys
import argparse


def sumMax(args):
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')
    parsedArgs = parser.parse_args(args)
    print(parsedArgs.accumulate(parsedArgs.integers))
    return parsedArgs.accumulate(parsedArgs.integers)


if __name__ == "__main__":
    sumMax(sys.argv[1:])
