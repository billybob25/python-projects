import random
answers = ['no','cant count on it','the badger']
print('''
wlecome to the magic eight ball please enter your question''')
while True:
    question = input('> ')
    answer = random.choice(answers)
    print(answer)
