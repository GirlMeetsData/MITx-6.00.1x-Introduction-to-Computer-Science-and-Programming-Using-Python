low = 0
high = 100
ans = int((low+high)/2.0)

print("Please think of a number between 0 and 100!")

while True:
  print("Is your secret number " + str(ans) + '?')
  print("Enter 'h' to indicate the guess is too high.", end = " ")
  print("Enter 'l' to indicate the guess is too low.", end = " ")
  print("Enter 'c' to indicate I guessed correctly.", end = " ")
  response = input("Enter your response")
  if response == 'h':
    high = ans
    ans = int((low+high)/2.0)
  elif response == 'l':
    low = ans 
    ans = int((low+high)/2.0)
  elif response == 'c':
    print("Game over. Your secret number was: "+ str(ans))
    break
  else:
    print("Sorry, I did not understand your input.")         
