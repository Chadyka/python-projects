import sys

#
#   C:  Python:
#   ||  or
#   &&  and
#   !   not
#
def hello(s):
    if (s=='Batman') or (s=='Robin'):
        print('Denevérveszély!')
    else:
        print('Hello ' + s + '!')


def main():
        name = sys.argv[1]
        hello(name)

if __name__ == "__main__":
    main()
