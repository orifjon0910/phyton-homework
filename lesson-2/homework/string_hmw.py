#1
name = str(input("What is your name? "))
birth = int(input("When were you born? "))
age = int(input("Age: "))
print("Your name is " + name + " and you were born in " + str(birth) + " and you are " + str(age) + " years old.")

#2
txt = 'LMaasleitbtui'
car1 = txt[::2]   # Even-index characters: L, a, s, e, t, t, i → "Lasetti"
car2 = txt[1::2]  # Odd-index characters: M, a, l, i, b, u   → "Malibu"
print("Car names:", car1, "and", car2)

#3
a = input("Enter a string: ")
print("Length:", len(a))
print("Uppercase:", a.upper())
print("Lowercase:", a.lower())

#4
s = input("Enter a string: ")
if s == s[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
   
#5
s = input("Enter a string: ")
v = sum(ch.lower() in "aeiou" for ch in s)
c = sum(ch.isalpha() and ch.lower() not in "aeiou" for ch in s)
print("Vowels:", v, "\nConsonants:", c)

#6
main_str = input("Enter the main string: ")
sub_str = input("Enter the substring to check: ")

if sub_str in main_str:
    print("The main string contains the substring.")
else:
    print("The main string does not contain the substring.")

#7
sentence = input("Enter a sentence: ")
old_word = input("Word to replace: ")
new_word = input("Replace it with: ")

updated_sentence = sentence.replace(old_word, new_word)
print("Updated sentence:", updated_sentence)

#8
s = input("Enter a string: ")
print("First character:", s[0])
print("Last character:", s[-1])

#9
s = input("Enter a string: ")
print("Reversed string: ", s[::-1])

#10
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Number of words:", len(words))

#11
s = input("Enter a string: ")
if any(char.isdigit() for char in s):
    print("The string contains digits.")
else:
    print("The string does not contain any digits.")

#12
words = ["apple", "banana", "cherry"]
separator = "-"
print(separator.join(words))

#13
text = input("Enter a string: ")
print(text.replace(" ", ""))

#14
str1 = input("Enter the first sring: ")
str2 = input("Enter the second string: ")
if str1 == str2:
  print("These strings are equal")
else: 
  print("These strings are not equal")

#15
sentence = input("Enter a sentence: ")
acronym = "".join(word[0].upper() for word in sentence.split())
print("Acronym:", acronym)

#16
s = input("Enter a string: ")
ch = input("Enter a character to remove: ")
print("Resulting string:", s.replace(ch, ""))

#17
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
print("Modified string:", "".join('*' if ch in vowels else ch for ch in s))

#18
s = input("Enter a string: ")
start = input("Start with: ")
end = input("Ends with: ")
s.startswith(start) and s.endswith(end)
print("The string starts and ends with the given words.")