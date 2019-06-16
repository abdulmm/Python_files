#Mohammed Abdul Mohi

import sys

if len(sys.argv) < 2:
	print('The correct usage of this file is: python method2_read_write_files.py <file_text.txt>')
	exit(1)
	
filename = sys.argv[1]
f = open(filename,'r')

data = f.read()
f.close()

def lines_count(data):
	lines = data.split('\n')
	for line in lines:
		if not line:
			lines.remove(line)
	num_lines = len(lines)
	return num_lines
	
def words_count(data):
	words = []
	lines = data.split('\n')
	for line in lines:
		if not line:
			continue
		else:
			line_words = line.split(' ')
			for word in line_words:
				words.append(word)
	num_words = len(words)
	return num_words
	
print('\n')
print('Number of lines = ',lines_count(data))
print('Number of words = ',words_count(data))								
