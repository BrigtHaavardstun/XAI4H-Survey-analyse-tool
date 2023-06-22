from tools_csv.clear_comma_in_comment import run as run_comma
from tools_csv.remove_between_date import run as run_date
from tools_csv.remove_new_line import run as run_newline
import argparse


def main(filename):
    new_file = filename[:-4] + "_fixed.csv"
    run_newline(filename=filename, new_filename=new_file)
    run_comma(filename=new_file, new_filename=new_file)
    run_date(filename=new_file, new_filename=new_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='ProgramName',
        description='Fix csv',
        epilog='updates newline, fix comma, fix date')
    parser.add_argument('-f', '--filename')           # positional argument
    args = parser.parse_args()
    print("Fixing: ", args.filename)
    main(args.filename)
