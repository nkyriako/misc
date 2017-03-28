#Nicole Kyriakopoulos
#nkyriako@ucsc.edu
#programming assignment 0
#This program converts kilometers to miles

def convert():                                                    #define function
	  kil = eval(input('What is the distance in kilometers?:  ')) #stores kilometer value in variable kil
	  mil = kil * .62                                             #mile value stored in variable mil
	  print('The distance in miles is ', mil)                     #print converted value
 
 
convert()                                                         #call function separately