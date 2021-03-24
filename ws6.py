#!/usr/bin/python3
import string, random, sys
dimension=15
width=dimension#assuming dimension > longest word_length
height=dimension
counter_cap=100 #when check more than 100 time, raise exception. 
#just generate random position in grid 
#should have 'width' and 'height' as local var instead of global var. 
#do need 'word' as input to decide placement of the grid.
def random_pos(word):
	#create directional vector:
	d=random.choice([[0,1],[1,0],[1,1]])
	if d[0] == 0:
		xsize=width
	else:
		xsize=width - len(word)
	if d[1] == 0:
		ysize=height
	else:
		ysize=height - len(word)

	x=random.randrange(0,xsize)
	y=random.randrange(0,ysize)

	mylist = [x,y,d[0],d[1]]	

	return mylist 
#need to create a counter , if counter >100, raise exception (prompt user to adjust dimension to larger size) 
def put_word(word,grid):
	
	#check grid element == '-' prior write to it.  
	#Unless the full word can be all '-', don't write call random_pos(word) till it get right.	

	#mylist = random_pos(word)
	#initialize counter and if it goes over 'counter_cap' , raise exception to abort the progam. 
	counter=0	
    #the while loop below check thru all element to be written.  If any element not writable, trigger random_pos() again until all good. 
	writable=False
	while not writable:
		counter += 1
		if counter >= counter_cap:
			raise Exception('The counter value has reach {}, please adjust grid dimension to bigger size to fit in all the words'.format(counter))
		print('check space is called for {} times'.format(counter))
		mylist=random_pos(word)
		#set the flag to true,so we can AND with any False to turn the flag to False.  
		#unless any of the grid element trigger false, the while loop should not loop again	
		writable=True
		for i in range(0,len(word)):
			if grid[ mylist[1]+mylist[3]*i ][ mylist[0]+mylist[2]*i ] != '-':
				writable=writable and False  #use AND logic, in case non-writable happen in betw writables
			

	
	#The check should pass by now, we can safely use the mylist vector to start write to grid of given word.  
	for i in range(0,len(word)):
		grid[mylist[1] + mylist[3]*i][mylist[0] + mylist[2]*i] = word[i]

	
	return grid


#we could use lambda style of oneliner function here. 
#def chk_collision():

#	return 0


def space_filler(grid):
	
	#loop through entire grid and only fill in letter if element == '-'
	for i in range(0,width): 
		for j in range(0,height):
			if grid[j][i] == '-':
				grid[j][i] = random.choice(string.ascii_uppercase)	
		
	return grid


def file2list(filename):
	with open(filename,'r') as fn:
		mylist = fn.read().splitlines()
	return mylist


# should take a fully wordmatch text file, the generate the wordsearch puzzle. 
# the clue should be definition of the word, not the actual word itself. 	
def main():
	#wordlist=["HELLO","THERE","AGAIN"]
	wordlist = file2list(sys.argv[1]) 
	max_len= len(max(wordlist,key=len))
	if dimension <= max_len:
		print("dimension size too small to cater all word") 
		
		return	
	#Below is an empty grid filled with '-' to be used in put_word to start with
	#then, the grid will get updated for each of forloop interation. 
	grid = [ [ '-' for i in range(0,width)] for j in range(0,height) ]
	
	for word in wordlist:
		grid = put_word(word, grid)
	
	#fill up the rest of unwritten grid with random char.
	print("below are solution only:")
	aa= "\n".join(map(lambda row: " ".join(row), grid)) 
	print(aa)

	grid = space_filler(grid)
	#print final result:
	print("below are final result:")
	bb= "\n".join(map(lambda row: " ".join(row), grid)) 
	print(bb)




main()

