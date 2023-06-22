import matplotlib.pyplot as plt
from pandas import read_csv
from datetime import date
from get_info.data_info.get_robot_info import get_accuracy
from get_info.data_info.get_robot_info import get_robot_info_old as get_robot_info
from get_info.data_info.get_robot_info import get_robot_info_new


def main():

    files = ["A.csv", "B.csv", "C.csv"]

    data = {}

    for file in files:
        ys = []
        print(f"Checking file {file}")
        dataframe = read_csv(f"csv_files/{file}")
        columns_data = dataframe.columns
        nr_robots = 6
        for i in range(1, nr_robots+1):
            robot_info = get_robot_info(i)

            ys.append(get_accuracy(
                columns_index=robot_info["columns"], correct_answers=robot_info["answer"], columns_data=columns_data, dataframe=dataframe))

        xs = list(range(1, nr_robots+1))

        data[file] = {"xs": xs, "ys": ys}

    width = 0.2
    curr_x = width/2
    for file in files:
        xs = list(map(lambda x: x + curr_x, data[file]["xs"]))
        ys = data[file]["ys"]
        print(file, ys)
        print("xs:", xs, "ys:", list(map(lambda y: round(y, 3), ys)))
        plt.bar(xs, ys, width=width)
        curr_x += width
    plt.legend(list(map(lambda x: x.replace(".csv", ""), files)))
    plt.ylabel("Accuracy")
    plt.xlabel("Robot")
    plt.show()


if __name__ == "__main__":
    main()
