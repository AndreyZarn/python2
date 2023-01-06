# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
 
def input_num():
   while True:
       try:
           inp = input('Введите вещественное число: ')
           if inp.isdigit():
               return inp
           #else:
               #print('Ошибка')
       except:
           print('Это не вещественное число')
 
 
num = input_num()
sum = 0
for i  in str(num):
   if i != '.':
       sum += int(i)
 
 
print(sum)
 
 
 
 
