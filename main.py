import pandas


def create_phonetic():
    data = pandas.read_csv("nato_phonetic_alphabet.csv")

    phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

    user_input = input("Enter a word: ").upper()

    try:
        phonetic_code = [phonetic_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only alphabet letters please")
        create_phonetic()
    else:
        print(phonetic_code)


create_phonetic()
