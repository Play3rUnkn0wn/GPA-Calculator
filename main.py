#variable
file = open("major.gpa.txt", "r")
GPA = 0 
classes = 0

#for loop
for line in file.readlines():
  text=line
  list=text.split()
  list[0]
  list[1]
  
#find class & grades
  
#number of classes
  classes += 1
#Career Prep Classes
  if list[0] == 'C': 
    if list[1] == 'A':
      # =3.5
      GPA += 3.5
    elif list[1] == 'B':
      # =2.5
      GPA += 2.5
    elif list[1] == 'C':
      # =1.5
      GPA += 1.5
    elif list[1] == 'D':
      # =0.5
      GPA += 0.5
    else:
      # =0
      GPA += 0
      
#College Prep Classes 
  elif list[0] == 'CP':
    if list[1] == 'A':
      # =4
      GPA += 4
    elif list[1] == 'B':
      # =3
      GPA += 3
    elif list[1] == 'C':
      # =2
      GPA += 2
    elif list[1] == 'D':
      # =1
      GPA += 1
    else:
      # =0
      GPA += 0
      
#Honors Classes 
  elif list[0] == 'H': 
    if list[1] == 'A':
      # =4.5
      GPA += 4.5
    elif list[1] == 'B':
      # =3.5
      GPA += 3.5
    elif list[1] == 'C':
      # =2.50
      GPA += 2.5
    elif list[1] == 'D':
      # =1.50
      GPA += 1.5
    else:
      # =0
      GPA += 0
      
#AP Classes
  elif list[0] == 'AP':
    if list[1] == 'A':
      # =5
      GPA += 5
    elif list[1] == 'B':
      # =4
      GPA += 4
    elif list[1] == 'C':
      # =3
      GPA += 3
    elif list[1] == 'D':
      # =2
      GPA += 2
    else:
      # =0
      GPA += 0

#close file
file.close()

#GPA
FinalGPA = round(GPA / classes, ndigits=2)
                 
#Print GPA
with open("major.gpa.txt", "a") as PrintTo:
  print('--------------------------------------------------', file=PrintTo)
  print('GPA =', FinalGPA, file=PrintTo)
file.close()