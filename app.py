print("Title of program: Post Exam Activity Bot")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "hapPy":
      feelings_list.append("happy")
      encouragement_list.append("keep smiling. There is so much positivity in the world!")
      counter += 1
    if each_word == "bored":
      feelings_list.append("bored")
      encouragement_list.append("find new hobbies to do or go out with your friends! I am sure there is something out there for you to do!")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("get some sleep! Sleep is very important!")
      counter += 1
    if each_word == "sad"
      feelings_list.append("sad")
      encouragement_list.append("cheer up! Tomorrow will be better!")
      counter += 1

  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that you have to"+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember that you have to"+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
