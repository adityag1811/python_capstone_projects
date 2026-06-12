morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----', ',': '--..--',
    '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-'
}



# Reversed the dictionary to iterate in case morse code is to be converted to text
reversed_dict = {value:key for key,value in morse_code.items()}


def morse(choice,text):
    output_text = []
    if choice == "tm":
        for char in text:
            if char not in morse_code:
                output_text.append("/")

            else:
                output_text.append(morse_code[char])
        print(" ".join(output_text))
    elif choice == "mt":
        to_decode = text.split()
        for char in to_decode:
            if char == "/" or char ==" ":
                output_text.append(" ")
            elif char not in reversed_dict:
                output_text.append(" ")
                print(f"Skipping the unknown character '{char}'")
            else:
                output_text.append(reversed_dict[char])
        print("".join(output_text))



should_continue = True

while should_continue:

    user_choice = input("To convert text to morse enter 'tm' and to convert morse to text enter 'mt' : ")
    if user_choice not in ["tm","mt"]:
        print("please enter either 'tm' or 'mt': ")
        continue
    elif user_choice == "tm":
        user_text = input("Please enter a word/s and we shall convert it to a morse code text and vice-versa: ").upper()
    else:
        user_text = input("Please enter a word/s and we shall convert it to a morse code text and vice-versa: ")

    morse(choice=user_choice,text=user_text)

    restart = input("Type 'yes' if you want to go again or else type 'no' : ")
    if restart == 'no':
        should_continue = False
        print("Goodbye")






