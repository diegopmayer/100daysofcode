import random
from json import load


# getting the random word from the list
word_list = ['ardvark', "baboon", "camel"]
chosen_word = random.choice(word_list)

# hangman drawed from json file
print(f"The chosen word is {chosen_word}")
with open('code/007/draw_hang.json', 'r') as file:
    draw_hang = load(file)


display =[]
word_len = len(chosen_word)
end_of_game = False
lives = 6

# creating the rnge of "_" to display values
for _ in range(word_len):
    display.append("_")

# guess letter from user game
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print("You've already type this letter, try another one.")

    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")
        break

    if guess not in chosen_word:
        lives -= 1
        print(draw_hang[str(lives)])
        if lives == 0:
            end_of_game = True
            print("Game Over")
            break