a = input('Do you see the ground squirrel?')
b = input('Ah,do you see the second ground squirrel?')
if a == 'yes' and b == 'yes':
    print("Tell me please, what did you eat yesterday... Because I have vague suspicions...")
elif a == 'yes' and b == 'no':
    print("Well done! I thought you won’t notice me!")
elif a == 'no' and b == 'no':
    print("But they are!")
elif a == 'no' and b == 'yes':
    print("Remember, if there is a second ground squirrel, then there is the first.")
else:
    print("Error 404!(Enter \'yes \' or \'no \'),Verdict: You are a ground squirrel!")
