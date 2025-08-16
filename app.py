import json
import random

with open('questions.json', 'r') as q:
    quiz_questions = json.load(q)


def menu():
    print('\n---Quiz App---\n')

    categories = {1: 'science', 2: 'math', 3: 'literature'}
    difficulties = {1: 'easy', 2: 'medium', 3: 'hard'}

    try:
        user_category = int(
            input('Choose the category 1)Science 2)Math 3)Literature: '))
        user_difficulty = int(
            input('Choose the difficulty 1)Easy 2)Medium 3)Hard: '))

        category_key = categories.get(user_category)
        difficulty_key = difficulties.get(user_difficulty)

        if category_key and difficulty_key:
            questions = quiz_questions[category_key][difficulty_key]
            score = 0
            total_questions = len(questions)
            random.shuffle(questions)

            for q in questions:
                user_answer = input(f"\n{q['question']}: ")

                if user_answer.strip() == q['answer']:
                    print('Correct!')
                    score += 1
                else:
                    print(f"Incorrect! Correct answer was {q['answer']}")

            print(
                f"\nYou answered {score} out of {total_questions} questions.")

            play_again = input("\nDo you want to play again? (y/n): ").lower()
            if play_again == "y":
                menu()
            else:
                print('Bye Bye.')
        else:
            print('Enter valid numbers.')

    except ValueError:
        print('Enter valid numbers.')


menu()
