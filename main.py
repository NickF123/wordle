# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def read_file():
    # opening the file in read mode
    with open("wordle.txt", "r") as my_file:
        data = my_file.read()
        my_file.close()

    return data.split("\n")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    words = read_file()

green_letters = input("What is the first attempt green letters, enter emptys with asterisks? Ex s***e").lower()
known_letters = input("Input a comma seperated list of letters that are known (yellow letters): ").lower().split(',')
eliminated_letters = input(
    "Input a comma seperated list of letters that are eliminated (gray letters): ").lower().split(',')

# eliminates words that don't match the green letter pattern
for i in range(len(words)):
    word = words[i]

    # eliminates words that don't have required green letters in correct position
    for j in range(0, len(word)):
        if green_letters[j] == '*':
            continue
        if word[j] != green_letters[j]:
            words[i] = '0'  # any words set to '0' are emliminated as candidates
            break

    # eliminates any words that do have eliminated or gray letters
    for e in range(0, len(eliminated_letters)):
        if eliminated_letters[e] in word:
            words[i] = '0'

    #eliminates any word that does not contain known or yellow letters
    for k in range(0, len(known_letters)):
        if known_letters[k] not in word:
            words[i] = '0'  # any words set to '0' are emliminated as candidates
            break
        else:
            continue

# prints all words not eliminated by the seive which are all the possible candidate words this round
for word in words:
    if word != '0':
        print(word)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
