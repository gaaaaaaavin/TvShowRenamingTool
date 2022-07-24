import os


print(os.getcwd())


season=str(input("Which Season?\n"))
season="S"+season.zfill(2)+"E"

extension=input("format? example.mkv\n")


files=[]

for x in os.listdir():
	if x != str(os.path.basename(__file__)):
		if extension in x:
			files.append(x)


files.sort()


print("before\n")
for x in files:
	print(x)

print("\n\n")

print("Preview: "+season+"01"+extension)
askStart=input('"Y" to continue\n')

if askStart.upper() != "Y":
	quit()

for x in range(len(files)):
	ep=str(x+1)
	fileName=season+ep.zfill(2)+extension	
	os.rename(files[x],fileName)

print("\n\nFiles: \n"
for x in os.listdir():
	print(x)
