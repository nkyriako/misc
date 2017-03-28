#Nicole Kyriakopoulos
#nkyriako@ucsc.edu
#This assignment lets you choose how many test scores you would like
#to check, and takes the average of those scores.

def avg_score():
  sum = 0
  num_grades = eval(input("How many grades will you be entering? "))
  if type(num_grades) == int:
    for i in range(num_grades):
      grade = eval(input("Please enter a grade between 0 and 100: "))
      if grade > 100 or grade < 0:  
	                    #grades must be between 0 and 100 to be added
        print("Your number is out of range!")
        grade = eval(input("Please enter a grade between 0 and 100: "))  
        num_grades = num_grades - 1
        continue		#loop to last block
      else:             #take average
        sum = sum + grade
    sum = sum/num_grades 
    if sum < 70:        #print averages. Average must be at least 70 to be "great"
      print("Your class did poorly. The average was ", sum)
    if sum >=70:
      print("Your class did great! The average was ", sum)
  elif type(num_grades) != int:
    print("You can't enter ", num_grades, " grades! ")
    avg_score()        #loop to beginning
	
avg_score()