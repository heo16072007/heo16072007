from time import sleep

inp = ''
class user:
    name = ''
    nick_name = ''
    age = 0

class AI:
    name = ''


print('------------------------Wellcom to AI chat box-----------------------')
print('-----------Just type any command and I will answer if i can----------')

while 2 > 1:
    inp = input()
    inp = inp.lower()

    if inp == 'hi' or inp == 'hello' or inp == 'hey':
        sleep(0.5)
        print("Hi, I'm there")
    
    elif inp == 'exit':
        sleep(0.5)
        print("! EVERY THING ABOUT YOU WILL BE DELETE!")
        print("Type 'Y' to close or 'N' to continue!")
        check = input()
        check = check.upper()
        if check == 'Y':
            sleep(0.5)
            print('See you next time..')
            exit()
        
        elif check == 'N':
            sleep(0.5)
            print('Right!! Stay with me :v')
        
        else:
            sleep(0.5)
            print("I'm so sorry but I can't understand that :((")
    
    elif inp == 'get my name':
        def gmn():
            sleep(0.5)
            print('Your name is: ' + user.name)
        gmn()

    elif inp == 'get my age':
        def gma():
            sleep(0.5)
            print('Your age is: ' + user.age)
        gma()
    
    elif inp == 'change my name':
        sleep(0.5)
        print("Let's type your name there: ")
        user.name = input()
        sleep(0.5)
        print("OK! Now your name is " + user.name)
        
    elif inp == 'change my age':
        sleep(0.5)
        print("Let's type your age there:")
        user.age = input()
        sleep(0.5)
        print("OK! Now your age is " + user.age)
    elif inp == 'change my nick name':
        sleep(0.5)
        print("Type it here:")
        user.nick_name = input()
        sleep(0.5)
        print("OK! Now your nick name is " + user.nick_name)

    elif inp == 'change ai name':
        sleep(0.5)
        print('Always ready!! Type it:')
        AI.name = input()
        sleep(0.5)
        print("OK! That's suck :> My name is " + AI.name)

    elif inp == 'get ai name':
        if len(AI.name) != 0:
            sleep(0.5)
            print('My name is ' + AI.name)
        else:
            sleep(0.5)
            print("Please creat my name! Try 'change ai name'")

    elif inp == 'list':
        sleep(0.5)
        print('-----------------------------Here you are!---------------------------')
        sleep(0.25)
        print('1. hi, hello, hey')
        sleep(0.25)
        print('2. change my name')
        sleep(0.25)
        print('3. change my age')
        sleep(0.25)
        print('4. change my nick name')
        sleep(0.25)
        print('5. get my nick name')
        sleep(0.25)
        print('6. get my name')
        sleep(0.25)
        print('7. get my age')
        sleep(0.25)
        print('8. change ai name')
        sleep(0.25)
        print('9. exit')

        #Here you are!

    else:
        sleep(0.5)
        print("I'm so sorry but I can't understand that :((")