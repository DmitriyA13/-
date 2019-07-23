while True:
  try:
    summ = float(input('Enter the amount:'))
    break
  except ValueError:
    print('Invalid input')  
years = 1
percent = 0
def check():
  while True:
    prog1 = input('Program. Just a num:')
    prog2 = input('Confirm the program:')
    if prog1 == prog2:
      return prog2
      break
    else:
      print('Verification failed')  


while True:
  print("Choose a program\n1) 1 year, 7 % \n2) 3 years 8,5 % \n3) 5 years 10 %")
  prog = check()
  if prog == '1':
    percent = 7
    break
  elif prog == '2':
    percent = 8.5
    years = 3
    break
  elif prog == '3':
    percent = 10
    years = 5
    break  
  else:
    print('specified program does not exist or has been deleted')    
summ = round((summ + round(((summ * percent)/100),2))*years,2)
print('AMOUNT AT THE END OF THE PROGRAM:',summ)
print('Will the client take the money after the end of the program')
while True:
  answer = input('Yes/No:')
  if answer == 'yes' or answer == 'Yes' or answer == 'YES':
    break
  elif answer == 'no' or answer == 'No' or answer == 'NO' :
    try:
      plusyears = int(input('For how long the money will remain?'))
    except ValueError:
      print('Invalid data type')
    for i in range(plusyears):
      print('year after graduation',i+1)
      percent = round(percent/2,2)
      if percent < 0.1:
        percent = 0.1
      print('percent',percent)
      summ = round((summ + round(((summ * percent)/100),2))*years,2)
      print('Amount',summ)
    break  
  else:
    print('unknown answer')    
