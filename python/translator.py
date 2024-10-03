import sys

# Mapping letters, numbers, spaces to braille code
braille_map = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 
    'e': "O..O..", 'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 
    'i': ".OO...", 'j': ".OOO..", 'k': "O...O.", 'l': "O.O.O.", 
    'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.", 'p': "OOO.O.", 
    'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 
    'y': "OO.OOO", 'z': "O..OOO",
    '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", 
    '5': "O..O..", '6': "OOO...", '7': "OOOO..", '8': "O.OO..", 
    '9': ".OO...", '0': ".OOO..", ' ': "......"
}

# Markers for capital and number 
capital_marker = ".....O"
number_marker = ".O.OOO"

# Reversing the braille map for brailled to english conversion
reverse_braille_map = {value: key for key, value in braille_map.items()}

def english_to_braille(text):
    result = []
    is_number = False

    for char in text:
        # Checking if we need to add a number marker
        if char.isdigit() and not is_number:
            result.append(number_marker)
            is_number = True

        # Checks for capitals 
        if char.isalpha():
            if char.isupper():
                result.append(capital_marker)
            is_number = False  
            char = char.lower()

        result.append(braille_map.get(char, ""))

    return ''.join(result)

def braille_to_english(braille):
    result = []
    is_capital = False
    is_number = False
    i = 0

    while i < len(braille):
        # Extract 6 characters from the Braille string
        symbol = braille[slice(i, i+6)]

        if symbol == capital_marker:
            is_capital = True
        elif symbol == number_marker:
            is_number = True
        elif symbol in reverse_braille_map:
            char = reverse_braille_map[symbol] # Get the matching English character.
            if is_number:
                result.append(char)
                is_number = False # Reset number state
            elif is_capital:
                result.append(char.upper())
                is_capital = False # Reset capital state
            else:
                result.append(char)
        else:
            result.append(' ') 
        i += 6

    return ''.join(result)

def main():
    # Get input from command-line arguments
    input_text = ' '.join(sys.argv[1:])
    
    if 'O' in input_text or '.' in input_text:
        # braille input converted to english
        print(braille_to_english(input_text))
    else:
        # english input converted to braille
        print(english_to_braille(input_text))

if __name__ == "__main__":
    main()
  
