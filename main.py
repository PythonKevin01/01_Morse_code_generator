from code import morse_code

while True:
    user = str(input("What is your morse code message?: ").lower())
    code = ""
    for letter in user:
        code += morse_code[letter] + " "
    print(code)





