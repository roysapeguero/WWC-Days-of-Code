# Today's Challenge:
# Write a program to check if a number is positive, negative, or zero.

def get_sign(num):
  if num > 0:
    return "positive"
  elif num < 0:
    return "negative"
  else:
    return "zero"

print(get_sign(-1))
print(get_sign(10))
print(get_sign(0))
print(get_sign(-100))
