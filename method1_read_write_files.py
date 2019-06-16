#Mohammed Abdul Mohi

filename = 'file_text.txt'
f = open(filename,'r')
data = f.read()
f.close()

lines = data.split('\n')

for line in lines:
    if not line:
        lines.remove(line)
        
print('The lines in the text are:')
print(lines)

num_lines=len(lines)
print('\nThe number of lines is:',(num_lines))

words = []
for line in lines:
        lines_word = line.split()
        for word in lines_word:
            words.append(word)
           
print('\nThe words in the text are:')     
print(words)
num_words = len(words)
print('\nThe total number of words is:',(num_words))

       