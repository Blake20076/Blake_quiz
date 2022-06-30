#base learing quiz

#importing the random libary
import random

#globals and questions list
score = 0
english = ["Yellow", "Mail", "dog", "keyboard", "hello"]
right_answer = ["kōwhai", "mēra", "kuri", "papapātuhi", "kia ora"]
option_1 = ["kia ora", "mera","kai", "free wrong answer", ""]
option_2 = ["whakautu hē", "mōra","whakamaramatanga", "papapatuhi"]

#define a function to generate a question
def generate_question(english, right_answer, option_1, option_2 ):
  global score 
  print ("what is the correct word for", english, "in maori")
  # genrate a random number to determent the sequence of questions
  random_sequence = random.randint(0,2)
#seperate print statements for readabilty
  if (random_sequence == 0):
    print ("A", option_1)
    print ("B", option_2)
    print ("C", right_answer)
    answer = input (). lower()
    if answer == "c":
      score += 1
    else:
      print ("incorrect")
  elif (random_sequence == 1):
    print ("A", option_1)
    print ("B", right_answer)
    print ("C", option_2)
    answer = input (). lower()
    if answer == "b":
      score += 1
    else:
      print ("incorrect")

  elif (random_sequence == 2):
    print ("A", right_answer)
    print ("B", option_2)
    print ("C", option_1)
    answer = input (). lower()
    if answer == "a":
      score += 1
    else:
      print ("incorrect")        
#genrate 3 questions pulling possible answer
for i in range(0,5):
  generate_question(english[i],right_answer[i],option_1[i],option_2[i])


print (score)

