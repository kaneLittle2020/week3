#This is the function 
def greet_user():
  print ("please enter your name")
  name = input ()
  print ("hello", name)

#calls to the function
greet_user()

-------------------------------------

print ("PROMGRAM STARTED")
print ("please enter a standard character:")
character = input ()

if (len(character)== 1):
  ascii_value = ord (character)
  print ("The ASCII code for {} is {}." .fromat(character, ascii_value))
else:
  print ("invalid character")

  
print ("program ended")


-------------------
def escape_by (plan): 
  print("How should we escape? A - jumping over, B - running around or C - going deeper")

  if (plan == "jumping over"):
    print ("We cannot escape that way! The boulder is too big!")
  elif (plan == "running around "):
    print ("We cannot escape that way! The boulder is moving too fast!")
  elif (plan == "going deeper"):
    print ("That might just work! Let's go deeper!")
  else: 
    print ("make sure the option is captalised or is from the listed options A, B or C")

escape_by()

--------------------------
def climb_ladder(steps_remaining, steps_crossed):
  if (steps_remaining > steps_crossed):
    print ("still some way to go")
  else: 
    print ("We are almost there")


climb_ladder (3,4)