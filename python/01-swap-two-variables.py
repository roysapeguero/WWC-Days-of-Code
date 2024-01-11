# Today's Challenge:
# Create a program that swaps the values of two variables.

def swap_two_variables(var1, var2):

  print('before', var1, var2)
  var1, var2 = var2, var1
  print('after', var1, var2)

swap_two_variables('hello', 'world')
