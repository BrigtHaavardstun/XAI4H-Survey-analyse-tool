
from datetime import date


def convert_txt_to_date(txt):
    year, month, day = txt.split("-")
    day = int(day[0:2])
    month = int(month)
    year = int(year.replace('"', ""))
    curr_date = date(year=year, month=month, day=day)
    return curr_date


def remove_date_based(filename, start_date, end_date):
    all_text = ""
    with open(f"csv_files/{filename}", "r") as f:
        all_text = f.read()

    all_lines = all_text.split("\n")
    top = all_lines[0]
    data = all_lines[1:]

    data_to_keep = []
    for line in data:
        date = convert_txt_to_date(line.split(",")[-1])
        if start_date <= date <= end_date:
            data_to_keep.append(line)

    all_text = top + "\n" + "\n".join(data_to_keep)
    return all_text


def run(filename=None, new_filename=None, start_date=None, end_date=None, ):
    if filename is None:
        filename = "S.csv"
    if start_date is None or end_date is None:
        start = "22-02-2023"
        end = "24-02-2023"

        start_time = list(map(int, start.split("-")))
        start_date = date(
            year=start_time[2], month=start_time[1], day=start_time[0])
        end_time = list(map(int, end.split("-")))
        end_date = date(year=end_time[2], month=end_time[1], day=end_time[0])
    txt_to_store = remove_date_based(filename, start_date, end_date)
    if new_filename is None:
        new_filename = filename[:-4] + "_date_selected.csv"
    with open(f"csv_files/{new_filename}", "w") as f:
        f.write(txt_to_store)


if __name__ == "__main__":
    run()
