def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip().split())
	print(lines)
	return lines

def convert(lines):
	Allen_fig = 0
	Allen_pic = 0
	Allen_word = 0
	Viki_fig = 0
	Viki_pic = 0
	Viki_word = 0
	for line in range(len(lines)):
		if lines[line][1] == 'Allen':
			if lines[line][2] == '貼圖':
				Allen_fig += 1
			elif lines[line][2] == '圖片':
				Allen_pic += 1
			else:
				for a in lines[line]:
					Allen_word += len(a)
				Allen_word = Allen_word - len(lines[line][0]) - len(lines[line][1])
			continue
		elif lines[line][1] == 'Viki':
			if lines[line][2] == '貼圖':
				Viki_fig += 1
			elif lines[line][2] == '圖片':
				Viki_pic += 1
			else:
				for a in lines[line]:
					Viki_word += len(a)
				Viki_word = Viki_word - len(lines[line][0]) - len(lines[line][1])
			continue
		#if person: # 如果person有值，才會執行if
			#new.append(person + ':' + line)
	print('Allen說了', Allen_word, '個字')
	print('Allen傳了', Allen_fig, '張貼圖')
	print('Allen傳了', Allen_pic, '張圖片')
	print('Viki說了', Viki_word, '個字')
	print('Viki傳了', Viki_fig, '張貼圖')
	print('Viki傳了', Viki_pic, '張圖片')

def write_file(filename, lines):
	with open(filename, 'w', encoding = 'utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')

def chat():
	lines = read_file('LINE-Viki.txt')
	convert(lines)
	# write_file('output.txt', lines)

chat()