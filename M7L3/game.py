from random import choice, randint
import time
from Speach import *
levels = {
    "easy": ["dairy", "mouse", "computer"],
    "medium": ["programming", "algorithm", "developer"],
    "hard": ["neural network", "machine learning", "artificial intelligence"]

}

def play_game (level):
    score = 0
    words = levels.get(level, [])

    for i in range(3):
        random_word = choice(words)
        print(f'произносите слово{random_word}')
        recog_word = speach()
        print(recog_word)

        if random_word == recog_word:
            print('Абсолютно верно')
            score += 1
        else:
            print(f'Что-то не получилось. Правильное слово: {random_word}')

        time.sleep(2)

    print(f'Игра завершена! Ваш счёт: {score}/{len(words)}')

selected_level = input("Выберите уровень сложности (easy/medium/hard): ").lower()
play_game(selected_level)