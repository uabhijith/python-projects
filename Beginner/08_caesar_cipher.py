alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
def caesar(text, shift, direction):
    text1 = ""
    if direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet: #only alphabets are changed
            position = alphabet.index(char)
            new_position = position + shift
            text1 += alphabet[new_position]
        else:
            text1 += char
    print(f"The {direction}d text is: {text1}")


again="yes"
while again=="yes":
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type shift number:\n"))
                    # if shift is more than 26!
    shift %= 26
    caesar(text, shift, direction)
    again=input("Type 'yes' if you want to go again. otherwise type no !").lower()

