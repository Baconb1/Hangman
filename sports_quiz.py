"""
Project: sports_quiz.py
Author: Brock Bacon
Date: 9/29/2022
"""
import random

# Constant Variables

score = 0 

# Have a list of sports questions to go through
questions = ["How many years apart is each world cup in soccer/football?\n->",
             "What sport is described as “the beautiful game”?\n->",
             "How many NBA championships did Michael Jordan win with the Chicago Bulls?\n->",
             "What team won the very first NBA game?\n->",
             "What NFL team scored the most points in a single Super Bowl?\n->",
             "Which NFL team went undefeated and also won the super bowl?\n->",
             "MLB (Major league baseball) founded on which year??\n->",
             "A professional baseball game consists of how many innings?\n->",
             "How many people on each team are on the volleyball court?\n->",
             "What is it called if you score the point on the serve?\n"]

# Answers for the questions
answers = ["4","soccer","6","knicks","49ers","dolphins","1903","9","6","ace"]


print("---------------------------------")
print("You are running Brocks sports quiz")
print("---------------------------------\n")

# Set up whether they get the answer right
question = random.sample(range(1, len(questions) + 1), len(questions))

for num in question:
    user_answer = input(questions[num - 1])
    if user_answer.lower() == answers[num - 1]:
        print("Correct\n")
        score += 1
    else:
        print("Incorrect\n")

# Display how they did out of 10
print("Your final score is",score,"out of 10\n")

input("Press ENTER to exit")

