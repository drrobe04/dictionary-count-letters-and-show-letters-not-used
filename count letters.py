#takes user input and converts it to a lower case string
user_input = input("Enter a sentence: ").lower()
#empty dictionary to store
stored_letters = {}
#set that defines what the alphabet is
alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}

#creates a loop to loop through the characters user entered    
for letter in user_input:
    if letter != " ":
        if letter in stored_letters:
            stored_letters[letter] += 1
        else:
            stored_letters[letter] = 1
print('Letter\t\tCount')
#a loop that prints the letters stored from the sentence with sorting
for letter in sorted(stored_letters):
    print(f'{letter}\t\t{stored_letters[letter]}')
#displays the characters that were not used by comparing it to the alphabet set and the letters stored that the user entered
print('these were the characters left out',alphabet.difference(stored_letters))