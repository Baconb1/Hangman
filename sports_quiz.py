"""
Project: sports_quiz.py
Author: Brock Bacon
Date: 9/29/2022
"""
import random

# Constant Variables

score = 0 

# Have a list of sports questions to go through
questions = ["How often is each world cup in soccer/football?\n->",
             "?\n->",
             "?\n->",
             "?\n->",
             "?\n"]

# Answers for the questions
answers = ["4","","","",""]


print("---------------------------------")
print("You are running Brocks sports quiz")
print("---------------------------------\n")

question = random.sample(range(1, len(questions) + 1), len(questions))

for num in question:
    user_answer = input(questions[num - 1])
    if user_answer.lower() == answers[num - 1]:
        print("Correct\n")
        score += 1
    else:
        print("Incorrect\n")

# Set up whether they get the answer right

# Have a list of sports questions to go through

# Display how they did out of 10
print("Your final score is",score,"out of 10\n")

input("Press ENTER to exit")

