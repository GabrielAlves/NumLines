import os
import sys

def num_lines(source, dest, empty_sep = 2):
    if source is None:
        print("No source file to number")
        sys.exit(1)

    with open(source, "r") as source_file:
        if dest is None:
            filename, extension = os.path.basename(source).split(".")
            dest = filename + "(numbered_lines)." + extension

        with open(dest, "w") as dest_file:
            lines = source_file.readlines()
            size_last_num = len(str(len(lines))) 

            for num, line in enumerate(lines, start = 1):
                size_curr_num = len(str(num))
                padding = " " * (size_last_num - size_curr_num)
                empty_spaces = " " * empty_sep 
                dest_file.write(f"{padding}{num}{empty_spaces}{line}")

def remove_num(source, dest, empty_sep = 2):
    if source is None:
        print("No source file to unnumber")
        sys.exit(1)

    with open(source, "r") as source_file:
        if dest is None:
            filename, extension = os.path.basename(source).split(".")
            dest = filename + "(unnumbered_lines)." + extension

        with open(dest, "w") as dest_file:
            lines = source_file.readlines()
            size_last_num = len(str(len(lines)))

            for num, line in enumerate(lines, start = 1):
                jump_size = (size_last_num + empty_sep)
                dest_file.write(f"{line[jump_size: ]}")


def main():
    arguments = sys.argv

    if len(arguments) > 1:
        op = sys.argv[1]

        if op != 1 and op != 2:
            print("Invalid operation. 1 -> Enumerate lines. 2 -> remove numbered lines")
            sys.exit(1)

        source = None
        dest = None
        empty_sep = 2

        if len(arguments) > 2:
            source = sys.argv[2]

        if len(arguments) > 3:
            dest = sys.argv[3]

        if len(arguments) > 4:
            empty_sep = sys.argv[4]

        if op == 1:
            num_lines(source, dest, empty_sep)

        else:
            remove_num(source, dest, empty_sep)

    

if __name__ == "__main__":
    main()