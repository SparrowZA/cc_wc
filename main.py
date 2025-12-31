"""
This is the main module to the coding challenge
is which I will create a wc -like program in Python.
"""
import argparse


def main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c')
    args = parser.parse_args()

    if hasattr(args, "c"):
        file_name = args.c

    with open(file_name, 'r') as fd:
        file = fd.read()
    
    print(f"{len(file)} {file_name}")

if __name__ == "__main__":
    main()
