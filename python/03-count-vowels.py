# Today's Challenge:
# Write a function to count the number of vowels in a given string

def vowel_counter(str):
  vowels = 'aeiou'
  count = 0

  for letter in str:
    if letter.lower() in vowels:
      count += 1

  return f'There are {count} vowels in the string "{str}"'

str1 = "TOTALLY"
str2 = "potato"
str3 = "Oh no"
str4 = "yEs"

print(vowel_counter(str1))
print(vowel_counter(str2))
print(vowel_counter(str3))
print(vowel_counter(str4))
