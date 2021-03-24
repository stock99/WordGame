#!/usr/bin/python
import sys, getopt, random


inputfile = '/home/stock/Documents/LEE/word_match/workspace/song1.txt'
mydir = '/home/stock/Documents/LEE/word_match/workspace/'
#outputfile= '/home/stock/Documents/LEE/word_match/workspace/result1.txt'

# 1)take in a file. split first column and the rest into two different list
# 2) massage and rejoin the two
# do we need to try.. exception statement in each function? (maybe added later on)


#read file into two lists
#call myshuffle() and then add symbol (other wise need to pass file handle.. to much hassle)
#write result into output file. 
def file_process(filename):
	mylist1=[]
	mylist2=[]
	counter=0
	with open(filename+'_out.txt', 'w') as out_file:
		with open(filename,'r') as in_file:
			for line in in_file:
				counter += 1
				mylist1.append('['+ str(counter) + '] '+line.split('	', 1)[0])
				mylist2.append('[ ] '+ line.split('	', 1)[1])
			
			#shuffle the elements in mylist2 randomly
			# we need to split into two lists so we can shuffle the second list. 
			random.shuffle(mylist2)
			# combine mylist1 and mylist2 via zip()
			result=zip(mylist1, mylist2)
		#write the content of 'result' (list of lists) into file.
		for item in result:
			out_file.write(( item[0] + '	' + item[1]) )
						
			
#call file_process(filename) 
#adding the command line argument --option stuff. (skeleton??)
def main():
	file_process(inputfile)

main()
	


