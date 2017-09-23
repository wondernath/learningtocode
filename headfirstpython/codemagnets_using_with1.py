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
	with open('man.txt','w') as man_text:
		print(man,file=man_text)
	with open('other.txt', 'w') as other_text:
		print(other,file=other_text)
except IOError as err:
	print('File Error'+ str(err))
