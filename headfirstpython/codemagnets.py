import os

if os.path.exists('sketch.txt'):
	data = open('sketch.txt')
	man = []
	other = []
	for each_line in data:
		try:
			(role, line_spoken) = each_line.split(':',1)
			if role.strip() == 'Man':
				man.append(line_spoken.strip())
			elif role.strip() == 'Other Man':
				other.append(line_spoken.strip())
		except:
			pass
else:
	print("The file does not exist")
try:
	man_text=open('man.txt','w')
	other_text=open('other.txt', 'w')
	print(man,file=man_text)
	print(other,file=other_text)
except IOError:
	print('File Error')
finally:
	man_text.close
	other_text.close
