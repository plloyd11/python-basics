def yell(text):
    text = text.upper()
    number_of_chars = len(text)
    result = text + "!" * (number_of_chars // 2)
    print(result)

yell("You suck ass!")

def display_blanks(word):
    blanks = "-" * len(word)
    print(blanks)