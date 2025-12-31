"""
This is the main module to the coding challenge
is which I will create a wc -like program in Python.
"""
import argparse


def main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c')
    parser.add_argument('-l')
    args = parser.parse_args()

    if hasattr(args, "c") and args.c is not None:
        file_name = args.c
        with open(file_name, 'r') as fd:
            file = fd.read()
        print(f"{len(file)} {file_name}")
    if hasattr(args, 'l') and args.l is not None:
        file_name = args.l
        with open(file_name, 'r') as fd:
            lines = fd.readlines()
        print(f'{len(lines)} {file_name}')

if __name__ == "__main__":
    main()
