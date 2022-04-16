def run():
    word = input("put your word: ")

    if(check_word(word)):
        print(f"your word ( {word} ) is a palindromo")
    else:
        print(f"your word ( {word} ) not is a palindromo")

def check_word(original_word):
    parse_word = original_word.replace(' ','')
    parse_word = parse_word.lower()
    parse_word = parse_word[::-1]
    if(parse_word == original_word):
        return True
    else:
        return False

if __name__ == '__main__':
    run()
    