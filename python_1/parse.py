import argparse


def main():
    parser = argparse.ArgumentParser(description="calculate X ^ Y")
    parser.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("y", type=int, help="the exponent")
    args = parser.parse_args()
    answer = args.x**args.y
    if args.quiet:
        print(answer)
    elif args.verbose:
        print("{} to the power {} equals {}".format(args.x, args.y, answer))
    else:
        print("{}^{} == {}".format(args.x, args.y, answer))

if __name__ == '__main__':
    main()
