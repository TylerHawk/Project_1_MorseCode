# Morse Code Cryptography
## Via the Python terminal, text is encrypted and decrypted with morse code cypher.
### Understanding the project
![Documentation on morse code](/International_Morse_Code.svg)
<br>
Above are the rules to follow to encrypt my messages.
I chose to write dots as "." and dashes as "___" in my cypher. 
<br>
The program takes user input, determines if it needs to be encoded or decoded and produces and output.

### How to determine user needs

I check the user input for the presence of vowels. If present, the input needs encryption.

### Encryption

To encrypt, I iterated over each step in the user_input string. For each character, I iterate over the cypher code. 
If a match is found, the corresponding cypher is added to an output variable. 
Any characters not found in the cypher code are disregarded. 

### Decryption

Encrypted text is automatically detected. First, words are separated by the presence of 7 spaces.
Then for each word, each letter is separated by the presence of 3 spaces. 
Each encoded letter is matched with the corresponding letter in the cypher. 

### Summery

Final output is a program where a user can enter both, text, and morse code.
Output provides either encoded or decoded responses. <br>
I found decryption more involved because of the need to keep the words in groups. 
When I first wrote the code, I noticed that I was going to lose all my spaces between words. 
