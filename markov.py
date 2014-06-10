#!/usr/bin/env python
# a = ['bat','cat', 'rat' , 'gnat']
import sys

def make_chains(input_list):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    text_chain_dict = {}
    
    # i = 0
    for i in range(len(input_list)-2):
        key = (input_list[i],input_list[i+1])
        value = input_list[i+2]
        if not key in text_chain_dict:
            text_chain_dict[key] = value
        else:
            text_chain_dict[key].append(value)
           #text_chain_dict.get(key)
    # print text_chain_dict   
    return text_chain_dict

# def make_text(chains):
#     """Takes a dictionary of markov chains and returns random text
#     based off an original text."""
#     return "Here's some random text."

def main():
    args = sys.argv

    # Change this to read input_text from a file
    input_list = []
    f = open("green_eggs.txt")
    # indata = f.read()
    # input_text = list(indata.strip('\n').split(' '))
    #input_text = list(input_text.split(' '))
    # print input_text
  
    for line in f:
        line = line.rstrip()
        input_text = line.split(' ')
        input_list += input_text

    # print input_list

    chain_dict = make_chains(input_list)
    print chain_dict
   # random_text = make_text(chain_dict)
    # print random_text

if __name__ == "__main__":
    main()
