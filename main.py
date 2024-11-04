from cypher import cypher

# The presence of vowels identifies if user input is not morse code that needs decoding.
vowels = ["a", "e", 'i', "o", "u"]

needs_encoding = False

encoded_msg = ""

user_input = input("Messages can be either encoded or decoded. Enter your message bellow.\n").lower()

for vowel in vowels:
    if vowel in user_input:
        needs_encoding = True

if needs_encoding:
    # If needs_encoding, iterate over user_input and append cypher to encoded message.
    # Checks for the character in the cypher and appends the corresponding encryption to encoded_msg.
    for character in user_input:
        for i in range(len(cypher)):
            if character == cypher[i][0]:
                encoded_msg += cypher[i][1]
                if character != " ":
                    encoded_msg += "   "

    print(f"Your encoded messages is as fallows:\n{encoded_msg}")

# For decoding, string is split into words and for each word we decode each letter.
# Space is added after each word before decoding the next word.
else:
    words_to_encode = user_input.split("       ")
    letters_to_encode = []
    decoded_msg = ""
    for word in words_to_encode:
        letters_to_encode = ""
        letters_to_encode = word.split("   ")
        for letter in letters_to_encode:
            for i in range(len(cypher)):
                if letter == cypher[i][1]:
                    decoded_msg += cypher[i][0]
        decoded_msg += " "
    print(f"Your decoded message is as fallows:\n{decoded_msg}")
