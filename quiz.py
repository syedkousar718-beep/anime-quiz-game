
import time

from question import (
    easy_questions,
    moderate_questions,
    medium_questions,
    hard_questions
)

def quiz_page(difficulty):

    start_time = time.time()

    if difficulty == "Easy":
        questions = easy_questions

    elif difficulty == "Hard":
        questions = hard_questions

    elif difficulty == "Medium":
        questions = medium_questions

    elif difficulty == "Moderate":
        questions = moderate_questions

    else:
        print('please select difficulty level')

    score = 0

    for q in questions:

        print("\n" + q["question"])

        for option in q["options"]:
            print(option)

        user_answer = input("Your answer: ").lower()

        if user_answer == q["answer"]:
            print("✅ Correct!")
            score += 1

        else:
            print("❌ Wrong!")

        end_time = time.time()

        time_taken = end_time - start_time

    return score, time_taken




