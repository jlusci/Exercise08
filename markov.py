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
    
    text_block = []

    start_phrase = random.choice(chain_dict.keys()) 
  

    key = (start_phrase[0],start_phrase[1])
    # text_block.extend(start_phrase[0],start_phrase[1])
    # print text_block

    while key in chain_dict:
        add_phrase = random.choice(chain_dict.get(key)) # chooses random value from key value list
        print key[0],key[1], add_phrase

        key = (key[1],add_phrase) # makes a new tuple key from start phrase and add phrase
    

    # return "Here's some random text."

def main():
    args = sys.argv

    # Change this to read input_text from a file
    
    f = open("green_eggs.txt")
    input_text= f.read()
    input_list = input_text.split()
   
    # print input_list


    chain_dict = make_chains(input_list)
    # print chain_dict
    random_text = make_text(chain_dict)
    # print random_text

if __name__ == "__main__":
    main()
