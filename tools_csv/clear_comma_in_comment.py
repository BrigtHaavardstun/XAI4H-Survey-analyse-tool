

def run(filename, new_filename=None):
    top = []
    data_lines = []
    with open("csv_files/"+filename, 'r') as file:
        all_lines = file.read().split("\n")
        top = all_lines[0]
        data_lines = all_lines[1:]

    clean_data_lines = []
    for line in data_lines:
        data_row = line[0]
        for i in range(1, len(line)-1, 1):
            if line[i] == ',' and (line[i + 1] != '"' or line[i - 1] != '"'):
                continue
            data_row += (line[i])
        data_row += line[-1]
        clean_data_lines.append(data_row)
    if new_filename is None:
        new_filename = filename[:-4] + "_clean.csv"
    with open("csv_files/" + new_filename, "w") as file:
        file.write(top + "\n" + "\n".join(clean_data_lines))


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--filename", help="name of csv file")

    args = parser.parse_args()

    filename = args.filename

    if filename is None:
        raise ValueError("filename must be specified")

    print(f"Cleaning file {filename}")
    run(filename)
