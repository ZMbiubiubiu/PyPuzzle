def find_characters(file):
    characters = []
    with open(file, 'r') as f:
        for line in f:
            for char in line:
                if char.isalpha():
                    characters.append(char)
    return ''.join(characters)

def main(file):
    result = find_characters(file)
    print(result)

main('2.txt')