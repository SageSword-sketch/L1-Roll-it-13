want_instructions =input("do you want to see the instruction? ").lower()

# check the user says yes / no
if want_instructions == "yes" or want_instructions == "y":
   print("y")
elif want_instructions == "no" or want_instructions == "n":
     print("you said no")
else:
     print("please enter yes / no")

