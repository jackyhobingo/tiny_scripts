input_file = "input.txt"
output_file = "output.txt"

output = open(output_file, "w")
with open(input_file) as fin:
	for line in fin.readlines():
		if line.strip():
			output.write(line)
output.close()

