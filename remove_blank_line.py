input_file = "input.txt"
output_file = "output.txt"

with open(output_file, "w", encoding="utf-8") as fout:
    with open(input_file, encoding="utf-8") as fin:
        for line in fin.readlines():
            if line.strip():
                output.write(line)

