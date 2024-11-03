Below is the code explanation for  program1.words.py (compute the frequency of the words from the input.
The output should output after sorting the key alphanumerically.)

Splits a Sentence into Words
Sorts the Words in Alphabetical Order
Counts Each Unique Word
Stores Each Word and Its Count as a Tuple in a List
Prints Each Unique Word with Its Count


..> list_a = word.split() splits the sentence into individual words, creating a list of words

..> sorted(list_a) sorts the list list_a in alphabetical order and also declared count and result variable

count = list_a.count(char) counts occurrences of char in list_a.
pair = (char, count) creates a tuple pair with the word and its count.
if (pair not in result): checks if the pair is already in result. If not, it appends pair to result and Finally, this loop iterates over each (word, count) pair in result and prints it.


2 . second code program is program3.password.py (A website requires the users to input username and password to register.
Write a program to check the validity of password input by users.)

Following are the criteria for checking the password:
○ At least 1 letter between [a-z]
○ At least 1 number between [0-9]
○ At least 1 letter between [A-Z]
○ At least 1 character from [$#@]
○ Minimum length of transaction password: 6
○ Maximum length of transaction password: 12
Your function should accept a sequence of comma separated passwords
and will check them according to the above criteria. Passwords that
match the criteria are to be printed, each separated by a comma


code explanation:

Length Check: Ensures password length is between 6 and 12 characters.
Character Count Checks: Counts occurrences of:
Lowercase letters
Uppercase letters
Digits
Special characters
Validation Condition: If all conditions are met (at least one of each required character type), the password is printed.

The script iterates through list_of_passwords, checking each password




