#Nicole Kyriakopoulos
#nkyriako@ucsc.edu
#When the user inputs a sentence, the program will calculate the length
#of the sentence, in words, and average word length.

def word_calc():
  num_words = 0
  num_letters = 0 
  sentence = input("Please write a sentence. ")
#use regex to create a modified input w/o special characters  
  import re
  regex = re.compile('[^a-zA-Z]')
#substitute anything not alphabet with a space
  mod_sentence = regex.sub(' ', sentence)
#for each word in sentence, add 1 to num_words to count how many
  for each_word in mod_sentence.split():
    #if(each_word.isalpha() == True)
    num_words += 1
#for the average, add up all characters that aren't ,.?!
  for letter in sentence:
    if(letter.isalpha() == True):
      num_letters += 1
#average word length is number of letters/number of words
  awl = num_letters/num_words	  
#print the number of words and average length	
  if(num_words > 1):  
    print("Your sentence has ", num_words, " words.")
  elif(num_words == 1):
    print("Your sentence has 1 word.")
  print("The average word length of your sentence is approximately ", round(awl, 2), ".")
	
  
word_calc()