#!/usr/bin/env python
# a = ['bat','cat', 'rat' , 'gnat']
import sys
import random

def make_chains(input_list):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    text_chain_dict = {}
    
    for i in range(len(input_list)-2):
        key = (input_list[i],input_list[i+1])
        value = input_list[i+2]
        if key in text_chain_dict:
            text_chain_dict[key].append(value)
        else:
            text_chain_dict[key] = [value]
           
    return text_chain_dict

def make_text(chain_dict):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    
    #initialize empty list and make random choice from keys in chain_dict
    text_block = []
    start_phrase = random.choice(chain_dict.keys()) 

    #assign variable key to start of random text and add to text_block list
    key = (start_phrase[0],start_phrase[1])
    text_block.extend([start_phrase[0],start_phrase[1]])

    #step through key value pairs to randomly pick next value 
    while key in chain_dict:
        add_phrase = random.choice(chain_dict.get(key)) # chooses random value from key value list
        text_block.extend([add_phrase])
        key = (key[1],add_phrase) # makes a new tuple key from start phrase and add phrase
    
    return text_block

def clean_up_text(random_text):
    """Takes in list of random text and outputs it 5 words on a line"""
    # random_join = " ".join(random_text)
    total_text = ""

    for index in range(0,len(random_text),5):
        new_line = " ".join(random_text[index:index+5]) + '\n'
        total_text = total_text + new_line
 
    return total_text

def sixty_characters(text_block):
    
    my_tweet = text_block[0:59]

    return my_tweet

def main():
    args = sys.argv

    filename = sys.argv[1]

    #Open and read input file, use .split to break into list separated on whitespace
    f = open(filename)
    input_text = f.read()
    input_list = input_text.split()

    #call function to create dictionary of key value pairs
    chain_dict = make_chains(input_list)
    #call function to generate random text from dictionary
    random_text = make_text(chain_dict)
    #call function to clean up the random text generated to five lines at a time
    total_text = clean_up_text(random_text)

    #print joined list of random text
    # print total_text

    #print cleaned up text of random words
    # print " ".join(random_line)

    my_tweet = sixty_characters(total_text)
    print my_tweet


if __name__ == "__main__":
    main()
