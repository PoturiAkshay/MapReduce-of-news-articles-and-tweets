#opening the sgm file
InputFile = open("reut2-020.sgm", "r")
#counter variable to indicate the occurance of <text> and </text> tags
counter = -1
#count variable for creating the files
count=1

#for each line in the input file searching for content between <text> and </text> tags
for line in InputFile:
    if("<TEXT" in line):
        counter=0
        file=open('./Article'+str(count)+'.txt','a')
        continue
    elif("</TEXT>" in line):
        counter=-1
        count=count+1
        file.close()
        continue
    elif(counter==0):
        file.write(line)
        continue

InputFile.close()

#opening the sgm file
InputFile = open("reut2-021.sgm", "r")
#counter variable to indicate the occurance of <text> and </text> tags
counter = -1

#for each line in the input file searching for content between <text> and </text> tags
for line in InputFile:
    if("<TEXT" in line):
        counter=0
        file=open('./Article'+str(count)+'.txt','a')
        continue
    elif("</TEXT>" in line):
        counter=-1
        count=count+1
        file.close()
        continue
    elif(counter==0):
        file.write(line)
        continue

InputFile.close()
