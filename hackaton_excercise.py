import random
words = ['account', 'addition', 'adjustment', 'advertisement', 'agreement',
         'amount', 'amusement', 'animal', 'answer', 'apparatus', 'approval',
         'argument', 'attack', 'attempt', 'attention', 'attraction',
         'authority', 'balance', 'behavior', 'belief', 'breath', 'brother',
         'building', 'business', 'butter', 'canvas', 'chance', 'change',
         'comfort', 'committee', 'company', 'comparison', 'competition',
         'condition', 'connection', 'control', 'copper', 'cotton', 'country',
         'credit', 'current', 'damage', 'danger', 'daughter', 'decision',
         'degree', 'design', 'desire', 'destruction', 'detail', 'development',
         'digestion', 'direction', 'discovery', 'discussion', 'disease',
         'disgust', 'distance', 'distribution', 'division', 'driving',
         'education', 'effect', 'example', 'exchange', 'existence', 'expansion',
         'experience', 'expert', 'family', 'father', 'feeling', 'fiction',
         'flight', 'flower', 'friend', 'government', 'growth', 'harbor',
         'harmony', 'hearing', 'history', 'impulse', 'increase', 'industry',
         'insect', 'instrument', 'insurance', 'interest', 'invention',
         'journey', 'knowledge', 'language', 'learning', 'leather', 'letter',
         'liquid', 'machine', 'manager', 'market', 'measure', 'meeting',
         'memory', 'middle', 'minute', 'morning', 'mother', 'motion',
         'mountain', 'nation', 'number', 'observation', 'operation', 'opinion',
         'organisation', 'ornament', 'payment', 'person', 'pleasure', 'poison',
         'polish', 'porter', 'position', 'powder', 'process', 'produce',
         'profit', 'property', 'protest', 'punishment', 'purpose', 'quality',
         'question', 'reaction', 'reading', 'reason', 'record', 'regret',
         'relation', 'religion', 'representative', 'request', 'respect',
         'reward', 'rhythm', 'science', 'secretary', 'selection', 'servant',
         'silver', 'sister', 'sneeze', 'society', 'statement', 'stitch',
         'stretch', 'structure', 'substance', 'suggestion', 'summer', 'support',
         'surprise', 'system', 'teaching', 'tendency', 'theory', 'thought',
         'thunder', 'transport', 'trouble', 'vessel', 'weather', 'weight',
         'winter', 'writing']

random_word = random.choice(words)
len_random_word = len(random_word)

print('This is hangman game. I have randomly selected a word, you will provide letter to guess the word. ')
print('You can guess 6 times. After each round you will have a chance to guess entire word. Good Luck! ')
print(f'My word has {len_random_word} letters: ')

answer = ['_'] * len_random_word
print(' '.join(answer))

counter = 0
nr_of_guesses = 10

while nr_of_guesses > 0:
    user_guess = input(f'Please provide letter which you would like to guess. You have {nr_of_guesses} guesses left: ')

    if len(user_guess) > 1:
        print('Try again, you need to provide only one letter.')
        user_guess = input(f'Please provide letter which you would like to guess: ')

    if user_guess.isdigit():
        print('Try again, you need to provide only letters')
        user_guess = input(f'Please provide letter which you would like to guess: ')

    user_guess = user_guess.lower()

    for letter in random_word:
        if user_guess == letter:
            answer[counter] = user_guess
        counter += 1

    print(' '.join(answer))
    counter = 0
    nr_of_guesses -= 1

    answer_to_string = ''.join(answer)
    if answer_to_string == random_word:
        print(f'You have guessed correctly. This word is {random_word}. Congratulations!')
        break

    is_final_answer = input('Would you like to guess entire word? y/n: ')

    if is_final_answer == 'y':
        final_answer = input('Please guess entire word: ')
        if final_answer == random_word:
            print(f'You have guessed correctly. This word is {random_word}. Congratulations!')
            break
        else:
            print('No this is not the word I am looking for. Guess further! ')

    if nr_of_guesses == 0:
        print(f'You are out of guesses. The word I was looking for is: {random_word} ')
