# Today's Challenge:
# Write a program to find the sum of all elements in a list.

def sumOfAll(nums):
  i = 0
  total = 0
  while i < (len(nums)):
    total += nums[i]
    i += 1

  return total

print(sumOfAll([1, 2, 3, 4, 5]))
print(sumOfAll([0]))
print(sumOfAll([10, -20, -50, 20]))
