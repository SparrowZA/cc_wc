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
    parser.add_argument('-w')
    parser.add_argument('input_file', type=str)
    args = parser.parse_args()

    if hasattr(args, "c") and args.c is not None:
        file_name = args.c
        with open(file_name, 'r') as fd:
            file = fd.read()
        print(f"{len(file)} {file_name}")
    elif hasattr(args, 'l') and args.l is not None:
        # Don't use the readlines method because it omits the 
        # last \n in the file if the file ends in two \n's
        file_name = args.l
        count = 0
        with open(file_name, 'r', encoding='utf-8') as fd:
            while True:
                line = fd.readline()
                count += 1
                if not line:
                    break
        print(f'{count} {file_name}')
    elif hasattr(args, 'w') and args.w is not None:
        file_name = args.w
        with open(file_name, 'r') as fd:
            file = fd.read()
        words: list[str] = file.split(' ')
        print(f'{len(words)} {file_name}')
    else:
        file_name = args.input_file
        with open(file_name, 'r', encoding='utf-8') as fd:
            file = fd.read()
        
        count = 0
        with open(file_name, 'r', encoding='utf-8') as fd:
            while True:
                line = fd.readline()
                count += 1
                if not line:
                    break
        
        with open(file_name, 'r', encoding='utf-8') as fd:
            file = fd.read()
        words: list[str] = file.split(' ')
        print(f'{len(file)} {count} {len(words)} {file_name}')

if __name__ == "__main__":
    main()
