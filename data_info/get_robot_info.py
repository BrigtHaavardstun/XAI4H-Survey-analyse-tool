from datetime import date


def get_robot_info_new(idx):
    robots = {}
    for i in range(1, 7):
        robots[i] = {"columns": "", "answer": ""}

    robots[1]["columns"] = [11, 12, 13, 14, 15]
    robots[1]["answer"] = ["Box 2", "Box 2", "Box 2", "Box 1", "Box 2"]

    robots[2]["columns"] = [20, 21, 22, 23, 24]
    robots[2]["answer"] = ["Box 1", "Box 1", "Box 2", "Box 2", "Box 1"]

    robots[3]["columns"] = [29, 30, 31, 32, 33]
    robots[3]["answer"] = ["Box 1", "Box 1", "Box 1", "Box 1", "Box 1"]

    robots[4]["columns"] = [38, 39, 40, 41, 42]
    robots[4]["answer"] = ["Box 2", "Box 2", "Box 1", "Box 2", "Box 1"]

    robots[5]["columns"] = [47, 48, 49, 50, 51]
    robots[5]["answer"] = ["Box 1", "Box 2", "Box 1", "Box 1", "Box 1"]

    return robots[idx]


def get_robot_info_old(idx):
    robots = {}
    for i in range(1, 7):
        robots[i] = {"columns": "", "answer": ""}

    robots[1]["columns"] = [10, 11, 12, 13, 14]
    robots[1]["answer"] = ["Box 2", "Box 2", "Box 2", "Box 2", "Box 2"]

    robots[2]["columns"] = [19, 20, 21, 22, 23]
    robots[2]["answer"] = ["Box 2", "Box 2", "Box 1", "Box 1", "Box 1"]

    robots[3]["columns"] = [28, 29, 30, 31, 32]
    robots[3]["answer"] = ["Box 2", "Box 2", "Box 1", "Box 1", "Box 1"]

    robots[4]["columns"] = [37, 38, 39, 40, 41]
    robots[4]["answer"] = ["Box 2", "Box 1", "Box 1", "Box 1", "Box 1"]

    robots[5]["columns"] = [46, 47, 48, 49, 50]
    robots[5]["answer"] = ["Box 2", "Box 1", "Box 2", "Box 1", "Box 1"]

    robots[6]["columns"] = [55, 56, 57, 58, 59]
    robots[6]["answer"] = ["Box 1", "Box 1", "Box 1", "Box 1", "Box 1"]

    return robots[idx]


def get_accuracy(columns_index, correct_answers, columns_data, dataframe):
    nrCorrect = 0
    nrIncorrect = 0
    start_time = list(map(int, "21-01-2023".split("-")))
    start_date = date(
        year=start_time[2], month=start_time[1], day=start_time[0])
    end_time = list(map(int, "24-02-2023".split("-")))
    end_date = date(year=end_time[2], month=end_time[1], day=end_time[0])

    for i, c in enumerate(columns_index):
        answers = dataframe.get(columns_data[c])
        if answers[0] == "":
            print("empty answer!")
        time_stamps = dataframe.get("question41")
        for answer, time_stamp in zip(answers, time_stamps):
            year, month, day = time_stamp.split("-")
            day = int(day[0:2])
            month = int(month)
            year = int(year)
            curr_date = date(year=year, month=month, day=day)
            # print(curr_date, end=" ")
            # print(start_date, end=" ")
            # print(end_date)
            if start_date <= curr_date and curr_date <= end_date:  # Check that the day is valid
                if answer == correct_answers[i]:
                    nrCorrect += 1
                elif answer in ["Box 1", "Box 2"]:
                    nrIncorrect += 1
                else:
                    print(i, c)

                    print(
                        "WARNING! WARNING! WARNING! ONE OF THE CELLS DID NOT HAVE A VALID ANSWER")
                    continue  # ignore answer
                    raise ValueError("Neither Box 1 nor Box 2 for ", answer)
            else:
                continue
                # print(f"No! Day: {day}, Month: {month}, Day: {year}")
    print(f"Total: {nrCorrect+nrIncorrect}")
    print(f"Accuracy: {nrCorrect/(nrCorrect+nrIncorrect)}")
    return nrCorrect/(nrCorrect+nrIncorrect)
