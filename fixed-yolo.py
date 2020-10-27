import os
import argparse
def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  

def fixfile(filepath, kelas):
	#reading file
	reading_file = open(filepath, "r")
	z = []
	new_file_content = ""
	#setup a list within same classes number
	for line in reading_file:
		if( line[0] == opt.c):
			z.append(line)
		else:
			new_file_content = ""
			stripped_line = line.strip()
			jpop = stripped_line.split(" ")
			jpop.pop(0)
			jpop.insert(0,kelas+" ")
			benar =listToString(jpop)
			z.append(benar+"\n")
			print (benar)
	# open the file and changing the class number
	with open(filepath, 'w') as f:
		for item in z:
		    f.write("%s" % item)  

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--f", type=str, default="", help="path to dataset")
	parser.add_argument("--c", type=str, default="", help="nomor class")
	opt = parser.parse_args()
	for file in os.listdir(opt.f):
		if file.endswith(".txt"):
			#skip file that is named classes.txt
			if (file == "classes.txt"):
				continue
			filepath = os.path.join(opt.f, file)
			fixfile(filepath, opt.c)
