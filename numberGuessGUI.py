"""
Program: numberGuessGUI.py
Chapter 8
8/11/2024
Dennis Schauf

**NOTE: the module breezypythongui.py MUST be in the same directory as this file for the app to run correctly!

Template code for ANY GUI-based application in Chapter 8
"""

from breezypythongui import EasyFrame
import random

# Other imports can go here
# Class header (class name will change project to project)
class GuessingGame(EasyFrame):
     # Definition of our classes' constructor method
     def __init__(self):
          # Call to the Easy Frame class constructor
          EasyFrame.__init__(self, title = "Guessing Game 2.0", width = 260, height = 180 )

          #Initialize the instance variable for this class
          self.magicNumber = random.randint(1, 10)
          self.count = 0

          #Create and add widgets to the window
          self.hintLabel= self.addLabel(text = "Guess a Number Between 1 and 100", row = 0, column = 0, columnspan = 2, sticky = "NSEW")
          self.addLabel(text = "Your guess:", row = 1, column = 0)
          self.guessField = self.addIntegerField(value = 0, row = 1, column = 1)
          self.nextButton = self.addButton(text = "Next", row =2, column = 0, command = self.nextGuess)
          self.newButton = self.addButton(text = "New Game", row = 2, column = 1, command = self.newGame)

     # definition of the nextGuess() function
     def nextGuess(self):
          '''Process the user's next guess.'''
          self.count += 1
          # collect the user input from the integer field
          guess = self.guessField.getNumber()
          # logic that determines the game's outcome
          if guess == self.magicNumber:
               self.hintLabel["text"] = "Hooray! You got it in " + str()
               self.nextButton["state"] = "disabled"
          elif guess < self.magicNumber: 
               self.hintLabel["text"] = "Sorry, your guess was too low!"
          else:
               self.hintLabel["text"] = "Whoops! your guess was too high!"

     # definition of the newGame() function
     def newGame(self):
          '''Resets the data and GUI to their original states'''
          self.magicNumber = random.randint(1, 10)
          self.count = 0
          self.hintLabel["text"] = "Guess a number between 1 and 100"
          self.guessField.setNumber(0)
          self.nextButton["state"] = "normal"
# Global definition of the main() method
def main():
     # Instantiate an object from the class into mainloop()
     GuessingGame().mainloop()
# Global call to main() for program entry
if __name__ == '__main__':
     main()