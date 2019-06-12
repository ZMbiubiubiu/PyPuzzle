def find_characters(file):
    characters = []
    with open(file, 'r') as f:
        for line in f:
            for char in line:
                if char.isalpha():
                    characters.append(char)
    return ''.join(characters)

def find_characters_surrounded_by_three_big_guy(characters):
    words = []
    import re
    pattern = re.compile('[^A-Z][A-Z]{3}([a-z]{1})[A-Z]{3}[^A-Z]')
    results = pattern.finditer(characters)
    for match in results:
        words.append(match.group(1))
    return ''.join(words)


def main(file):
    characters = find_characters(file)
    words = find_characters_surrounded_by_three_big_guy(characters)
    print(words)
    

if __name__ == "__main__":
    main('3.txt')