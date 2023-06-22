def update_new_lines(filename, new_filename=None):
    all_txt = ""
    with open("csv_files/" + filename) as f:
        all_txt = f.read()
    all_lines = all_txt.split("\n")
    top_row = all_lines[0]

    data_rows = all_lines[1:]
    curr_row = ""

    fixed_lines = []
    for line in data_rows:
        last_line = line.split(",")[-1].replace('"', "")
        is_date = True
        try:
            times = last_line.split("-")
            assert len(times) == 3
            assert len(times[0]) == 4
            assert len(times[1]) == 2
            assert len(times[2].split(":")) == 3
            assert "T" in times[2]

        except:
            is_date = False

        if curr_row != "":
            curr_row += " "
        curr_row += line
        if is_date:
            fixed_lines.append(curr_row)
            curr_row = ""

    if new_filename is None:
        new_filename = filename[:-4] + "_line_fix.csv"

    with open("csv_files/" + new_filename, "w") as f:
        txt = top_row + "\n" + "\n".join(fixed_lines)
        f.write(txt)


def run(filename, new_filename=None):
    update_new_lines(filename=filename, new_filename=new_filename)


if __name__ == "__main__":
    filename = "S.csv"
