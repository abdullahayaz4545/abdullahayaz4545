import random
import time


print("the game is about to start")
print("the game has started")

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    global limit
    limit=5
    words_to_guess = ["aggressiveness","barrenness","bookkeeper","Chattahoochee","cheerlessness","committee","greenness","heedlessness","keenness","rottenness","Mississippi"]
    word=random.choice(words_to_guess)
    length=len(word)
    display='_'*length;
    already_guessed=[];
main()
def hangman():
   global limit;
 
     
   global display
   global word
   
    
   print("the word you have to guess is"+display)
    
   while(limit >0):
     if "_" not in display:
         print("success you have guessed the word, Congratuations")   
         print("the word is ",display);   
         break
     guess=input("enter your word one letter at  a time")
     # finding the number of times the thing exist in the string 
     count= word.count(guess)
     print("the number of times this word exist is",count)
     if guess in word:
       index= word.find(guess)
       display=display[:index]+guess+display[index+1:]
       for x in range(1,count):
          # print("heyyyyyy")
           index=word.find(guess,index+1)
           display=display[:index]+guess+display[index+1:]
                  
       print(display)
     elif    guess not in word:
        print("number is not in the word you loose 1 chance")
        limit=limit-1
        print("remaning chances are ",limit)
        if limit==0:
            print("You failed better luck next time")
            print( "the corrrect word is ",word) 
       

hangman()
