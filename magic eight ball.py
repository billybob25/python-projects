import random

answers = ['yes.','no.','maybe.','definitely.','no way!'] 
print('''
Welcome to the magic eight ball!
Enter your name below:
''')

while True:
    question = input('> ')
    answer = random.choice(answers)
    print(answer)





