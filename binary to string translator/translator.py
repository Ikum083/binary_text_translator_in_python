def main():
    while True:
        print("Binary Translator")
        print("1. Text to Binary")
        print("2. Binary to Text")
        print("3. End")
        trans_mode = int(input("> "))
        if trans_mode == 1:
            text_to_binary()
        elif trans_mode == 2:
            binary_to_text()
        elif trans_mode == 3:
            break
        else:
            print("Wrong input")

def text_to_binary():
    try:
        user_text = str(input("Input text here: "))
    except ValueError:
        print("Invalid input")
    final_binary = []

    for i in user_text:
        ascii_value = ord(i)
        print(ascii_value)
        final_binary.append(binary_translate(ascii_value))
        
    print("Your binary:", *final_binary)

def binary_to_text():
    final_text = ""

    try:
        user_binary = str(input("Input binary here: "))
    except ValueError:
        print("Invalid input")

    fixed_binary = "".join(user_binary.split())

    if len(fixed_binary) % 8 != 0:
        print("?")
    else:
        translated_binary = text_translate(fixed_binary)
        for d in translated_binary:
            final_text += chr(d)

    print(f"Your text is: {final_text}")

def binary_translate(ascii):
    binary = ""

    for a in reversed(range(8)):
        if ascii >= (2 ** a):
            ascii -= (2 ** a)
            print(a, ascii)
            binary += "1"
        else:
            print(a, ascii)
            binary += "0"

    return binary

def text_translate(binary):
    byte_groups = [binary[i:i + 8] for i in range(0, len(binary), 8)]

    final_ascii = []

    for b in byte_groups:
        iteration = 7
        ascii_num = 0
        for c in b:
            if iteration >= 0:
                if c == "1":
                    ascii_num += (2 ** iteration)
                    iteration -= 1
                else:
                    iteration -= 1
            else:
                continue
        final_ascii.append(ascii_num)

    return final_ascii

if __name__ == "__main__":
    main()