from get_info.data_info.get_robot_info import get_robot_info_new as get_robot_info
# from get_info.data_info.get_robot_info import get_robot_info_old as get_robot_info

from pandas import read_csv


def run(filename):
    print("_"*10, filename, "_"*10)
    path_to_file = "csv_files/" + filename
    data_dict = read_csv(path_to_file)
    # print(data_dict)

    ansewer_count_dict = {}

    nr_robots = 5
    for i in range(1, nr_robots+1):
        ansewer_count_dict[i] = {}

    for robot_nr in range(1, nr_robots+1):
        robot_info = get_robot_info(robot_nr)
        columns = robot_info["columns"]

        for row_nr in range(len(data_dict)):
            row = data_dict.iloc[row_nr]  # one particpant
            curr_answer = []  # Their answer
            for i in columns:
                curr_answer.append(row[i])

            curr_answer = list(map(str, curr_answer))
            curr_answer = ",".join(curr_answer)
            if curr_answer not in ansewer_count_dict[robot_nr]:
                ansewer_count_dict[robot_nr][curr_answer] = 0
            ansewer_count_dict[robot_nr][curr_answer] += 1

    for robot_nr in ansewer_count_dict.keys():
        print("#"*10, "Robot nr ", robot_nr, "#"*10)
        for answer in reversed(sorted(ansewer_count_dict[robot_nr].keys(), key=lambda answer: ansewer_count_dict[robot_nr][answer])):
            print(answer, ansewer_count_dict[robot_nr][answer])


if __name__ == "__main__":
    run()
