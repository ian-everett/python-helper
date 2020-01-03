'''
Using a argpars
'''

import argparse

def main():
    '''
    main()
    '''
    parser = argparse.ArgumentParser(description='A description of the program')

    # args requiring a value
    parser.add_argument('--input', help='path to thing to read', type=str, required=True)
    parser.add_argument('--output', help='path to thing to create', type=str)
    parser.add_argument('--count', help='using a int as command line arg', type=int)

    # arg without a value just for turning a flag on
    parser.add_argument('--flag', help='flag which can turn option on', action='store_true',
                        default=False)
    args = parser.parse_args()

    print(args)

    # Get the input value
    if args.input:
        print('Got input file of %s' % args.input)

    # Get the output value
    if args.output:
        print('Got output file of %s' % args.output)

    # Get the count integer val
    if args.count:
        print('count is a %s' % type(args.count))
        print('count is %d' % args.count)

    # The boolean flag
    print("flag is %r" % args.flag)

if __name__ == "__main__":
    main()
