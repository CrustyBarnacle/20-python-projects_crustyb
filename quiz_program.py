#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Mario Burgos
# Tutorial: https://github.com/tomitokko/20-python-projects
# Youtube: https://youtu.be/pdy3nh1tn6I
# Created Date: Tue Sep 13 2022
# version ='1.0'


# Dictionary to store quiz (Q's and Answers)
# Track score
# Loop through dictionary, and display each Q, get answer
# Let user know if they are correct
# Display final score


# Quiz questions and answers
quiz = {
    "question_1": {
        "question": "What is the capitol of France?",
        "answer": "Paris"
    },
    "question_2": {
        "question": "The capital of this country is Berlin",
        "answer": "Germany"
    },
    "question_3": {
        "question": "What is the capitol of Italy",
        "answer": "Rome"
    },
    "question_4": {
        "question": "What is the capitol of Spain?",
        "answer": "Madrid"
    },
    "question_5": {
        "question": "What is the capitol of Portugal?",
        "answer": "Lisbon"
    },
    "question_6": {
        "question": "What is the capitol of Switzerland?",
        "answer": "Bern"
    },
    "question_7": {
        "question": "What is the capitol of Austria?",
        "answer": "Vienna"
    },
}


def run_quiz(quiz):
    # Score starts at 0
    score = 0

    for key, value in quiz.items():
        print(f" {value['question']}") # display question
        user_answer = input(" Answer: ")

        if user_answer.title() == value['answer']: # Could use .lower() on user input and answer
            print(f" Correct. The answer is {value['answer']}\n")
            score +=1
        else:
            print(" That is incorrect...\n")

    return score


def main():
    final_score = run_quiz(quiz)
    print(f"Final score: {final_score}/7.")


main()
