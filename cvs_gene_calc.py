#import
#
import re
import sys
from operator import itemgetter
import argparse
import csv
import os

 


#arguments
#

parser = argparse.ArgumentParser(description="Gene Calculator") 
parser.add_argument("-in", "--infile", required=True,   
	help="name of file", type=str)
parser.add_argument("-out", "--outfile",  
	help="save to a file", type=str)
args = parser.parse_args()

	
	
	
	
try:
     fileObj = open(args.infile, 'r') #try to open the file
except FileNotFoundError as errorObj: 
    print("File not found", errorObj)
    
line = fileObj.readlines()#read file
string = ''.join(line) #make a string out of a list
sublines = string.splitlines() #split into lines
data0 = ' '.join(sublines) #make a string out of each line
final = data0.split('>') #split on the appearance of ">"
my_line = final[1:] #remove '' before the first line of interest


ann = 0
pseudo = 0
count = 0
rev = 0
forw = 0
leng = 0
scaf = 0
cOne = 0
cTwo = 0 
cThree = 0 
cFour = 0 
cFive = 0 
cSix = 0 
cSeven = 0
cEight = 0 
cNine = 0 
cTen = 0 
cEleven = 0  
cTwelve = 0 
cX = 0 
cY = 0 
T = 0
loc = 0
c13 = 0 
c14 = 0 
c15 = 0 
c16 = 0 
c17 = 0 
c18 = 0
c19 = 0 
c20 = 0 
c21 = 0 
c22 = 0
c23 = 0
c24 = 0
c25 = 0
cTwoA = 0 
cTwoB = 0


		
for s in my_line:
	if re.search(r'NONE', s):
		ann += 1
	else:
		pass

	
		
for s in my_line:
	count += 1		
	
		
		
for s in my_line:
	if  s.startswith(' (+)'):
		forw += 1
	else:
		pass		
		
for s in my_line:
	if  s.startswith(' (-)'):
		rev += 1
	else:
		pass	
		
		
for s in my_line:
	if  re.search(r'(?<=PSE)UDO', s):
		pseudo += 1	
	else:
		pass	
		
		
for s in my_line:
	if  re.search(r' P ', s):
		leng += 1	
	else:
		pass	
				

for s in my_line:
		if re.search(r'unplaced', s):
			scaf += 1
		else:
			pass
			
for s in my_line:
		if re.search(r'chromosome 1', s):
			cOne += 1
		else:
			pass
			
for s in my_line:
		if re.search(r'chromosome 2', s):
			cTwo += 1
		else:
			pass
						
			
for s in my_line:
		if re.search(r'chromosome 3', s):
			cThree += 1
		else:
			pass
			
for s in my_line:
		if re.search(r'chromosome 4', s):
			cFour += 1
		else:
			pass
			
for s in my_line:
		if re.search(r'chromosome 5', s):
			cFive += 1
		else:
			pass
			
for s in my_line:
		if re.search(r'chromosome 6', s):
			cSix += 1
		else:
			pass
			
for s in my_line:
		if re.search(r'chromosome 7', s):
			cSeven += 1
		else:
			pass
			
for s in my_line:
		if re.search(r'chromosome 8', s):
			cEight += 1
		else:
			pass
			
for s in my_line:
		if re.search(r'chromosome 9', s):
			cNine += 1
		else:
			pass
			
for s in my_line:
		if re.search(r'chromosome 10', s):
			cTen += 1
		else:
			pass
			
for s in my_line:
		if re.search(r'chromosome 11', s):
			cEleven += 1
		else:
			pass
			
for s in my_line:
		if re.search(r'chromosome 12', s):
			cTwelve += 1
		else:
			pass
			
for s in my_line:
		if re.search(r'chromosome X', s):
			cX += 1
		else:
			pass
			
for s in my_line:
		if re.search(r'chromosome Y', s):
			cY += 1
		else:
			pass
			
for s in my_line:
		if re.search(r' T1 ', s):
			T += 1
		else:
			pass
			
for s in my_line:
		if re.search(r' unlocalized ', s):
			loc += 1
		else:
			pass



for s in my_line:
		if re.search(r'chromosome 13', s):
			c13 += 1
		else:
			pass
			
for s in my_line:
		if re.search(r'chromosome 14', s):
			c14 += 1
		else:
			pass
			
for s in my_line:
		if re.search(r'chromosome 15', s):
			c15 += 1
		else:
			pass
			
for s in my_line:
		if re.search(r'chromosome 16', s):
			c16 += 1
		else:
			pass
			
for s in my_line:
		if re.search(r'chromosome 17', s):
			c17 += 1
		else:
			pass
			
for s in my_line:
		if re.search(r'chromosome 18', s):
			c18 += 1
		else:
			pass
			
for s in my_line:
		if re.search(r'chromosome 19', s):
			c19 += 1
		else:
			pass
			
for s in my_line:
		if re.search(r'chromosome 20', s):
			c20 += 1
		else:
			pass
			
for s in my_line:
		if re.search(r'chromosome 21', s):
			c21 += 1
		else:
			pass
			
for s in my_line:
		if re.search(r'chromosome 22', s):
			c22 += 1
		else:
			pass
			
for s in my_line:
		if re.search(r'chromosome 23', s):
			c23 += 1
		else:
			pass
			
for s in my_line:
		if re.search(r'chromosome 24', s):
			c24 += 1
		else:
			pass
			
for s in my_line:
		if re.search(r'chromosome 25', s):
			c25 += 1
		else:
			pass
			
			
			
			
			

fname = args.outfile
if os.path.isfile(fname):
    print("File updated", args.outfile)
    with open(args.outfile, 'a') as csvfile:
    	writer1 = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    	writer1.writerow([args.infile, ann, pseudo, forw, rev, scaf, loc, leng, count, T,cOne, cTwo, cThree,cFour, cFive,cSix,cSeven,cEight,cNine,cTen,cEleven,cTwelve, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23,c24,c25,cX,cY])
    
    
    
else:
    print("New file created", args.outfile)
    with open(args.outfile, 'w') as csvfile:
	
    	fieldnames = ['Species', 'No Annotation', 'Pseudo Annotation', 'Forward', 'Reverse', 'Unplaced', 'Unlocalised', 'Partial', 'Count', 'Transcript', 'Chr 1', 'Chr 2(A/B)', 'Chr 3', 'Chr 4', 'Chr 5', 'Chr 6','Chr 7' ,'Chr 8', 'Chr 9', 'Chr 10','Chr 11','Chr 12', 'Chr 13', 'Chr 14', 'Chr 15', 'Chr 16','Chr 17' ,'Chr 18', 'Chr 19', 'Chr 20','Chr 21','Chr 22', 'Chr 23', 'Chr 24', 'Chr 25', 'Chr X','Chr Y']
    	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    	writer.writeheader()
    	writer.writerow({'Species': args.infile, 'No Annotation': ann, 'Pseudo Annotation' : pseudo, 'Forward' : forw, 'Reverse' : rev, 'Unplaced' : scaf, 'Unlocalised': loc, 'Partial' : leng, 'Count': count, 'Transcript' : T, 'Chr 1' : cOne, 'Chr 2(A/B)' : cTwo, 'Chr 3': cThree, 'Chr 4' : cFour, 'Chr 5' : cFive, 'Chr 6' : cSix ,'Chr 7' : cSeven ,'Chr 8' : cEight, 'Chr 9' : cNine, 'Chr 10' : cTen, 'Chr 11' : cEleven, 'Chr 12' : cTwelve, 'Chr 13' : c13, 'Chr 14' : c14, 'Chr 15' : c15, 'Chr 16' : c16,'Chr 17' : c17 ,'Chr 18' : c18, 'Chr 19' : c19, 'Chr 20' : c20, 'Chr 21' : c21, 'Chr 22' : c22, 'Chr 23' : c23,'Chr 24' : c24,'Chr 25' : c25,'Chr X' : cX, 'Chr Y' : cY})
    
    

    	