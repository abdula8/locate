import re
import sys

def grep(pattern, filename) -> None:
    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if re.search(pattern, line):
                    print(f"{filename}:{line_number}: {line.strip()}")
    except FileNotFoundError:
        # print(f"Error: File '{filename}' not found.")
        pass
    except PermissionError:
        # print(f"Error: Permission denied while trying to open '{filename}'.")
        pass
    except Exception as e:
        # print(f"An unexpected error occurred: {e}")
        pass


def grep_string(search_string, filename):
    with open(filename, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if search_string in line:
                print(f"{filename}:{line_number}: {line.strip()}")



def grep_stdin(pattern):
    for line in sys.stdin:
        if re.search(pattern, line):
            print(line.strip())

def grep_stdin_2(pattern, npt):
    npt = str(npt)
    # for line in sys.stdin:
    if re.search(pattern, npt):
        print(npt.strip())


def usage():
    print('''Usage: python grep_script.py -in <pattern>
              OR
              python grep_script.py -f pattern filename
              OR
              python grep_script.py -s pattern'''
              )