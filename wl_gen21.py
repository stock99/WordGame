#!/usr/bin/python
#take in a file and generate a wordlist
#take in a wl and a file and generated a new of what's not presented in the wl.

import re,sys
import argparse
# simply run `wl_gen.py lyric.txt`
#inputfile=sys.argv[1]

#Extracting non-repeated word to form a wordlist (of a given text file)
def w_extract(inputfile):
	mylist=[]
	f=open(inputfile)
	for word in f.read().split():
		alph_only=(re.sub("[^a-zA-Z]+", "", word)).lower()
		if alph_only not in mylist:
			mylist.append(alph_only)
	#print(sorted(mylist))
	return (sorted(mylist))

#w_extract()


# take a lyric.txt and word_list, create return a list of word *WITHOUT* what's presented in given word_list
def delta(lyric_fn,wl_fn):
	newlist= w_extract(lyric_fn)
	print("below will be the newlist print out:")
	#print(newlist)
	with open(wl_fn,'r') as fn:
		oldlist = fn.read().splitlines()
	#print("below is the oldlist:")
	#print(type(oldlist))
	#print(oldlist)
	#creating new delta list
	d_list=[]
	for item in newlist:
		if item not in oldlist:
			d_list.append(item)
	#print("the following are delta list:")
	print(d_list)

	return (sorted (d_list))


def mywriteout(mylist,filename):
	with open(filename + 'out', 'w')  as outfile:
		for item in mylist:
			outfile.write(item + '\n')


	
#main function
#1. call w_extract to get a list of word. 
#2. write to a file. (only lyrics) 
#3.  get another file and delta the new wl file out. (--lyrics lyric.txt --wl wordlist.txt)
#4.  append the new word into the existing wl and sort it.  (not sure if I can exclude +ing/+ed repeated word without causing issue....should be ok??)
#5.  default word length is 4.  allow to change by specifying `--wordlength length`
#6.  provide option to give half of the total vocab for defn' only.  we will use this as hint for word search. 

#@@@@@@@@@@@
#1. maybe make lyric.txt a mandatory input???
#2. -l lyric.txt -pl previous_list  oldlist.txt
#3. -ds word_def.txt ==> shuffle def'n in the word:defn file and create []  
#4. [not needed]:-wsl wordlist => produce wordsearch map ; -pw print word below; -pd print def below
#5	-l2w lyric.txt => lyric.txt to wordsearch game ; -nw number -> number of word in wordsearch map 
#6.  ; -sol -> solution of wordsearch. 
#@@@@@@@@@@@@


def main():
	#setup input argument routine:
	parser = argparse.ArgumentParser(description="****Wordlist Generator Python Script****")		
	parser.add_argument("-lo","--lyriconly",help="provide the lyric text file", metavar="lyric.txt")
#	parser.add_argument()
#	parser.add_argument()

	
	#parsing provided arguments.
	args= parser.parse_args()

	#swtich like statements:
	if args.lyriconly:
		wordlist=w_extract(args.lyriconly)
		mywriteout(wordlist, args.lyriconly)
		#should put below as function for extreme readability of code:
		#with open(args.lyriconly + 'out', 'w')	as outfile:
		#	for item in wordlist:
		#		outfile.write(item + '\n')


#myd_list=delta(sys.argv[1],sys.argv[2])



main()
	
