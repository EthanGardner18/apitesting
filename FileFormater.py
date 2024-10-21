def add_line_numbers(input_file, output_file='formatted.txt'):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()

        with open(output_file, 'w') as formatted_file:
            for index, line in enumerate(lines, start=1):
                formatted_file.write(f'{index}: {line}')

        print(f'Line numbers added successfully to {output_file}')
    except FileNotFoundError:
        print(f'Error: {input_file} not found.')

add_line_numbers("functions.py")