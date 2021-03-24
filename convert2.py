import json,requests
import time,os
#google dict api. 
#input_file = 'sub4.txt'
#output_file = 'output1.txt'
dictapi = 'https://api.dictionaryapi.dev/api/v2/entries/en_US/'
#test_vocab = 'oxymoron22222'
mydir = '/home/stock/Documents/LEE/crossword0/wordlist/'

#take str as input word and lookup api to return definition of it. 
# need to capture word-not-found and return such error message!!!!

def word_lookup(myword):
    myquery = dictapi + myword
    #print (myquery)
    r = requests.get(myquery)
    if r.status_code == 200:
        j = r.json()
        #any error on looking up specific dict field failed, resulting mydef= 'word not found'
        try:
            mydef = str(dict(j[0])['meanings'][0]['definitions'][0]['definition'])
        except:
            mydef = '***Word Not Found***'

        #print (mydef)
        #return mydef
    else:
            mydef = '********HTTP Error Status Code =' + str(r.status_code)
            print(mydef)


    return mydef
        



def main():
    #open a writable new file and read-in the vocab file content. 
    #Then look up word_def and append into the word and write this string to the new file. 
    
    for filename in os.listdir(mydir):
        with open(filename+'_out.txt','w') as out_file:
            with open(mydir+filename,'r') as in_file:
                for line in in_file:
                    print(line)
                    #time.sleep(1)
                    s= word_lookup(line)
                    out_file.write(line.rstrip('\n')+' '+s+'\n')    
    
    #mystr=word_lookup(test_vocab)
    #print(mystr)

#open file, call word_lookup() and append the def string to the word.   Then repeat for the entire file.  

main()

