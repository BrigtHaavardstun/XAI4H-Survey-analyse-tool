from pandas import read_csv
from get_info.data_info.get_robot_info import get_robot_info_new as get_robot_info
import argparse


def run():
    parser = argparse.ArgumentParser()

    # -db DATABSE -u USERNAME -p PASSWORD -size 20
    parser.add_argument("-f", "--filename", help="name of csv file")
    parser.add_argument("-r", "--robot", help="Robot index, 0,1,2,3,4,5 or 6")

    args = parser.parse_args()

    filename = args.filename
    idx = int(args.robot)

    get_human_why(idx, filename)
    # get_human_why_ans_idx(idx, filename)
    # Test = 0, Rob 1 = 1, Rob 2 = 2, Rob 3 = 3, Rob 4 = 4, Rob 5 = 5, Rob 6 = 6


def get_human_why_ans_idx(idx, filename, find_answers=[], answer_numbers=[]):
    robot_info = get_robot_info(idx)
    question_columns = robot_info["columns"]
    dataframe = read_csv(f"csv_files/{filename}")
    columns_data = dataframe.columns

    non_matching_partcipants = set()
    for j, nr in enumerate(answer_numbers):
        answers = dataframe.get(
            columns_data[question_columns[nr]])
        for i, answer in enumerate(answers):
            # print("par_", answer)
            if i in non_matching_partcipants:
                continue
            if answer != find_answers[j]:
                # print(answer, find_answers[nr])
                non_matching_partcipants.add(i)

    print(non_matching_partcipants)
    get_human_why(idx, filename, forbidden=non_matching_partcipants)


def get_human_why(idx, filename, forbidden=set()):
    robot_info = get_robot_info(idx)
    question_column = robot_info["columns"][-1]+1
    dataframe = read_csv(f"csv_files/{filename}")
    columns_data = dataframe.columns
    answers = dataframe.get(columns_data[question_column])
    for i, answer in enumerate(answers):
        if i in forbidden:
            continue
        print("#####")
        print(answer)
        print("#####")
