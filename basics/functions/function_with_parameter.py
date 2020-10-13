def escape_by (): 
  print("How should we escape? A - jumping over, B - running around or C - going deeper")

  response = input()
  if response == "A":
    print ("We cannot escape that way! The boulder is too big!")
  elif response == "B":
    print ("We cannot escape that way! The boulder is moving too fast!")
  elif response == "C":
    print ("That might just work! Let's go deeper!")
  else: 
    print ("make sure the option is captalised or is from the listed options A, B or C")

escape_by()