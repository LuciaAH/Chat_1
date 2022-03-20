def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None # 定義person一開始為虛無
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person: # 如果person有值，才會執行if
			new.append(person + ':' + line)
	return new

def write_file(filename, lines):
	with open(filename, 'w', encoding = 'utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')

def chat():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

chat()