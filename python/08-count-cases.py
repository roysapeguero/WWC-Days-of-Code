# Today's Challenge:
# Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it.

def count_cases(str):
  upper_count = 0
  lower_count = 0

  for char in str:
    if char.upper() == char.lower():
      pass
    elif char.upper() == char:
      upper_count += 1
    elif char.lower() == char :
      lower_count += 1

  return { "uppercase":upper_count, "lowercase": lower_count }

print(count_cases("Hi!"))
print(count_cases("I'm Roysa."))
print(count_cases("Nice to mEEt you."))
