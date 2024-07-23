def filter_lines(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as file:
        for line in lines:
            if " 102[EXAMPLE KIND NUMBER YOU WANT REMOVED] " in line:
                file.write(line)

# Example usage
input_file = 'input_kind.log.txt'
output_file = 'output.txt'
filter_lines(input_file, output_file)
