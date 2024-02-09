import os

def process_files(files):
		processed_files = []

		for file in files:
				with open(file, 'r', encoding='utf-8') as f:  

						lines = f.readlines()
						processed_files.append((file, len(lines), enumerate(lines, 1)))  
		processed_files.sort(key=lambda x: (x[0] == '1.txt', x[0] == '2.txt', -x[1])) 

		with open('result.txt', 'w', encoding='utf-8') as result: 
				for file, num_lines, lines_enum in processed_files:
						result.write(f'{file}\n{num_lines}\n')

						for line_num, line in lines_enum:
								result.write(f'Строка номер {line_num} файла номер {file}\n')
								result.write(f'{line}')

files = [f for f in os.listdir() if os.path.isfile(f) and f.endswith('.txt')]
process_files(files)