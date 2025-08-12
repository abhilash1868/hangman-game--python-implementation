import random
hangman_stages = [
    """
     .......
     |     |
     |     
     |    
     |    
    _|_
    """,  
    """
     .......
     |     |
     |     O
     |    
     |    
    _|_
    """,  
    """
     .......
     |     |
     |     O
     |     |
     |    
    _|_
    """,  
    """
     .......
     |     |
     |     O
     |    /|\
     |    
    _|_
    """,  
    """
     .......
     |     |
     |     O
     |    /|\
     |    / 
    _|_
    """,  
    """
     .......
     |     |
     |     O
     |    /|\
     |    / \
    _|_
    """   
]

word = ['NOBITA','SUNIYO','DORAEMON']
lives = 6
choosen_word = random.choice(word)
print(choosen_word) #'NOBITA'
blanks = [] # ------
for blank in range(len(choosen_word)):
    blanks += '-'
print(blanks)
game = False
while not game:
    guess_letter = input("guess the letter:")  
    if guess_letter not in choosen_word:
          lives -= 1
          print(lives)
          print(hangman_stages[5-lives])
          if lives == 0:
              print('game over')
              game = True
    else:
     for position in range(len(choosen_word)):
         if choosen_word[position] == guess_letter:
             blanks[position] = guess_letter
             if '-' not in blanks:
                 game = True
                 print("you won")
             print(blanks)
   
