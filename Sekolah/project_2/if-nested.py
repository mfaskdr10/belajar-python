grade = int(input("Enter your grade: "))
list = []

if grade == 100:
  print("perfect")
elif grade >= 85:
  print("awesome")
elif grade >= 65:
  print("passed the exam")
  if grade <= 70:
    print("but you need to improve it")
  else:
    print("with ok grade")

else: 
  print("below the passing grade")

