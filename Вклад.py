while True:
  try:
    summ = float(input('������� �����:'))
    break
  except ValueError:
    print('�������� ����')  
years = 1
percent = 0
def check():
  while True:
    prog1 = input('���������(������ �����):')
    prog2 = input('����������� ���������:')
    if prog1 == prog2:
      return prog2
      break
    else:
      print('������������� �� ��������')  


while True:
  print("�������� ���������\n1) 1 ���, 7 % \n2) 3 ���� 8,5 % \n3) 5 ��� 10 %")
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
    print('��������� ��������� �� ����������, ��� �������')    
summ = round((summ + round(((summ * percent)/100),2))*years,2)
print('����� �� ����� ����������',summ)
print('������ �� ������ ������ ����� ��������� ���������')
while True:
  answer = input('��/���:')
  if answer == '��' or answer == '��' or answer == '��':
    break
  elif answer == '���' or answer == '���' or answer == '���' :
    try:
      plusyears = int(input('�� ����� ���� �������� �������� ���������?'))
    except ValueError:
      print('�������� ��� ������')
    for i in range(plusyears):
      print('��� ����� ���������',i+1)
      percent = round(percent/2,2)
      if percent < 0.1:
        percent = 0.1
      print('�������',percent)
      summ = round((summ + round(((summ * percent)/100),2))*years,2)
      print('�����',summ)
    break  
  else:
    print('����������� �����')    