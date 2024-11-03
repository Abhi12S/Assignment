below is the code explanation for  program1.words.py (compute the frequency of the words from the input.
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


second code is program is 
