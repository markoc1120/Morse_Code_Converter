from converter import Converter

conv = Converter()
is_running = True

print('MORSE CODE CONVERTER')

while is_running:
    text_to_code = input('I will convert your text to morse code, type your text (if you include special charachters'
                         ' which cannot be translated those will be removed): ')
    print(f"Your text in morse code: {conv.encrypt(text_to_code)}")
    again = input("Type 'y' to do another one, or 'n' to quit: ")
    if again == 'n':
        is_running = False
