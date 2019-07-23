while True:
  try:
    summ = float(input('Введите сумму:'))
    break
  except ValueError:
    print('Неверный ввод')  
years = 1
percent = 0
def check():
  while True:
    prog1 = input('Программа(просто цифра):')
    prog2 = input('Подтвердите программу:')
    if prog1 == prog2:
      return prog2
      break
    else:
      print('Подтверждение не пройдено')  


while True:
  print("Выбирите программу\n1) 1 год, 7 % \n2) 3 года 8,5 % \n3) 5 лет 10 %")
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
    print('указанная программа не существует, или удалена')    
summ = round((summ + round(((summ * percent)/100),2))*years,2)
print('СУММА НА КОНЕЦ ПРОГРАММЫЖ',summ)
print('Заберёт ли клиент деньги после окончания программы')
while True:
  answer = input('да/нет:')
  if answer == 'да' or answer == 'Да' or answer == 'ДА':
    break
  elif answer == 'нет' or answer == 'Нет' or answer == 'НЕТ' :
    try:
      plusyears = int(input('на какой срок денежные средства останутся?'))
    except ValueError:
      print('Неверный тип данных')
    for i in range(plusyears):
      print('год после окончания',i+1)
      percent = round(percent/2,2)
      if percent < 0.1:
        percent = 0.1
      print('процент',percent)
      summ = round((summ + round(((summ * percent)/100),2))*years,2)
      print('Сумма',summ)
    break  
  else:
    print('неизвестный ответ')    