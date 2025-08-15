import json

with open ('questions.json', 'r') as q:
    quiz_questions = json.load(q)

def menu():
    print('\n---Quiz App---\n')

    categories = {1: 'science', 2: 'math', 3: 'literature'}
    difficulties = {1: 'easy', 2: 'medium', 3: 'hard'}

    try:
        user_category = int(input('Choose the category(1.Science 2.Math 3.Literature): '))
        user_difficulty = int(input('Choose the difficulty(1.Easy 2.Medium 3.Hard): '))

        category_key = categories.get(user_category)
        difficulty_key = difficulties.get(user_difficulty)

        if category_key and difficulty_key:
            print(quiz_questions[category_key][difficulty_key])
        else:
            print('Enter a valid number.')

    except ValueError:
        print('Enter a valid number.')



menu()