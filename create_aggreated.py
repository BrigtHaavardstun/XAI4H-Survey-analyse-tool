
from pandas import read_csv
from datetime import date

from get_info.data_info.get_robot_info import get_robot_info_old
from get_info.data_info.get_robot_info import get_robot_info_new as get_robot_info


def get_participant_score(idx, dataframe):
    score = 0
    row = dataframe.iloc[idx]
    clean_row = []
    correct_answers = []
    nr_of_robots = 5
    for i in range(1, nr_of_robots+1):
        print(i)
        robot_info = get_robot_info(i)
        print(robot_info)
        columns = robot_info["columns"]
        answers = robot_info["answer"]
        for column, answer in zip(columns, answers):
            clean_row.append((row[column]))
            correct_answers.append(answer)

    # print(" ".join(clean_row))
    # print(" ".join(correct_answers))
    nrCorrect = 0
    nrIncorrect = 0
    for i, (ans, correct) in enumerate(zip(clean_row, correct_answers)):
        if ans == correct and ans in ["Box 1", "Box 2"] and correct in ["Box 1", "Box 2"]:
            nrCorrect += 1
            continue
        nrIncorrect += 1
        if ans not in ["Box 1", "Box 2"] or correct not in ["Box 1", "Box 2"]:
            print("WARNING not valid!", ans, correct,
                  "idx: ", idx, "column: ", i)
    return nrCorrect / (nrCorrect + nrIncorrect)


def create(filename, treatment):
    dataframe = read_csv(f"csv_files/{filename}")
    all_rows = []
    for i in dataframe.index:
        curr_score = 0
        try:
            curr_score = get_participant_score(i, dataframe=dataframe)
        except AttributeError:
            print(f"skipping: {i} as date is outside range")
            continue
        row = f"{treatment},{curr_score}"
        all_rows.append(row)
    return all_rows


def main():
    all_files = ["S_fixed.csv", "R_fixed.csv"]
    treatments = ["S", "R"]
    all_rows = []
    for file, treatment in zip(all_files, treatments):
        all_rows.extend(create(file, treatment))
    top_row = "index,treatment,score"
    new_file_name = "csv_files/aggregated_file.csv"
    with open(new_file_name, "w") as f:
        all_text = top_row + "\n" + \
            "\n".join([f'{i},{row}' for i, row in enumerate(all_rows)])
        f.write(all_text)


if __name__ == "__main__":
    main()
