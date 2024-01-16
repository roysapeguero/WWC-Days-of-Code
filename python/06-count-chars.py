# Today's Challenge:
# Write a program to count the occurrences of a specific character in a string.

def countChar(str, target):
  count = 0

  for char in str:
    if char == target:
      count += 1

  return count

print(countChar("Good Luck", "o"))
print(countChar("Good Luck", "!"))
print(countChar("Good Luck", "G"))
