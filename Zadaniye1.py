
text=("demofile.txt")
n=open(text)
for line in n:
    line.split('.')
koma=","
for i in line:
	if not koma in i:
		print (i)
f = open("demofile.txt", "r")
print(f.read())