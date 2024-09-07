import random;
def guessTrue():
    
        print("Wow you just guessed the actual number with 1 in a 100 probability")
        print("\n\tYou have a luck of a century!!!")
        
i=0   

print("Can you guess a number between 0 & 100\n")
theRealValue=random.randrange(100)
while(True):  
    guess=int(input()) 
    if(i == 6):
         print(theRealValue)
         break
    elif(guess == theRealValue):
        guessTrue();
        break
    elif(abs(theRealValue   -   guess)>=20):
        print("You're too far")
        i+=1
        continue
    elif(abs(theRealValue   -  guess)<20):
         print("Too close for comfort")
         i+=1
         continue
    elif(guess  > 100):
         print("Bro what the helll!!!!!")
         print("Don't play with me you're out")
         break
    