# Number-Guessing-Game-Python

## Project Overview
This project is a simple Number Guessing Game built using Python.  
The program generates a random number between 1 and 10, and the user has to guess it.
The program gives hints like "Too low" or "Too high" until the correct number is guessed.

## Features
- Random number generation  
- Unlimited attempts until correct guess  
- Hint system (Too low / Too high)  
- Tracks number of attempts  
- Handles invalid input using exception handling  

## Technologies Used
- Python  
- random module  

## How the Program Works

### 1. Generate Number

- A random number between 1 and 10 is generated:

``python
number = random.randint(1, 10)
## 2. User Input
User enters a number
Input is validated using try-except
## 3. Hint System
If guess is less → "Too low"
If guess is greater → "Too high"
## 4. Correct Guess
When user guesses correctly, program shows attempts
Example:
Correct! You guessed in 3 attempts

## How to Run
Install Python
Save file as guess_game.py
Run the program:
python guess_game.py

## Concepts Used
Random number generation
Loops (while)
Conditional statements
Exception handling
User input

## Learning Outcomes
After completing this project, you will learn:
How to generate random numbers
How to build interactive games
How to validate user input
How to use loops and conditions effectively

## Possible Improvements

Limit number of attempts
Add difficulty levels
Add score system
Store best score in file
Build GUI version

## Author
Harsha G
Learning Python | Embedded Systems | IoT
