# CodeMeHackathon1

# Hangman game

Game included in this project is Hangman game with following options:
- Programme is randomly choosing word in english from included list of words.
- User will be given information how many letters does this word contains.
- Next user is given 10 tries/rounds to guess letters and entire word.
- After user provides a letter it is checked if it is not a digit and if yes, then user is given another try to enter a letter.
- Each round begins with providing letter by the user, if it is included in guessed word - appropriate letters will be visible on correct places.
- After this user will be given an opportunity to guess entire word by selecting y or n option (yes or no)
- Once user will guess the word - program will end.
- After reaching 10 attempts without guessing the word, programme will provide correct answer and will end.

Game is written using table, for, if and while loops. Guessed letters are stored in a table. 
Error handling for entering multiple letters, digits or capital letters is in place.
