import sys
d_b = {
  0:0, 1:1, 2:2, 
  3:3, 4:4, 5:5, 
  6:6, 7:7, 8:8, 
  9:9, 10:'A', 11:'B', 
  12:'C', 13:'D', 14:'E', 
  15:'F', 16:'G', 17:'H', 
  18:'I', 19:'J', 20:'K', 
  21:'L', 22:'M', 23:'N', 
  24:'O', 25:'P', 26:'Q', 
  27:'R', 28:'S', 29:'T', 
  30:'U', 31:'V', 32:'W', 
  33:'X', 34:'Y', 35:'Z'
}

def from_decimal(d, b):
  toappend = []
  #check if decimal value is just zero
  if d == 0:
    print(0)
  
  if d > 1 and b > 1:
    #check if decimal value is within decimal value-type range
    if b < 10:
      while d:
        toappend.append(d%b)
        d //= b
    #if value is nondecimal type
    elif b > 10 and b < 37:
      while d:
        remainder = d%b
        hexim = d_b[remainder]
        toappend.append(hexim)
        d //= b 
    else:
      print("Base out of standard range!")
  else:
    print("Cannot use negative value for decimal & base!")
    
  mystring = ''.join(map(str, toappend))
  print(mystring[::-1])  #print final value, reverse slicing due to printing out value in correct order direction

def to_decimal(s, b):
  n = 0
  toappend = []
  result = []
  f_result = []
  toappend.extend(s)
  toappend = toappend[::-1]
  

  #to store needed value into list & convert corresponding alphab value into its numerical value based on base number system
  for i in toappend:
    for a in d_b:
      if i == d_b[a]:
        result.append(a)
        continue      
    result.append(i)
  
  #to remove alphabet character out of list, so number element in list can sum together
  for i in result:
    if str(i).isalpha():
      result.remove(i)

  #check if largest element in list is not less than or equal to base, if greater then throw error
  for i in result:
    if int(i) >= b:
      print("Error base greater than 35")
      exit()
    else:
      pass

  #multiplying each element with base value of incrementing exponent value starting from 0
  for i in result:
    each_val = int(i) * b**n
    n += 1
    f_result.append(each_val)

  #check if len of new list equal
  print(sum(f_result))

while True:
  try:
    opt = int(input("Choose to convert:\n1.Decimal-anybase\n2.Anybase-decimal\nEnter 1 or 2: "))
    if opt == 1:
      from_decimal(int(input("\nEnter decimal: ")), int(input("Enter base: ")))
    elif opt == 2:
      to_decimal(input("\nEnter decimal: ").upper(), int(input("Enter base: ")))
    else:
      print("Not in option.")
  except(TypeError):         
    print("There's an error in your value type!")
  except(SyntaxError):
    print("There's an error in your syntax!")
  except(ValueError):
    print("There's an error in your value!")
  finally:
    break