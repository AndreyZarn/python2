# Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06
 
 
def input_num1():
   while True:
       try:
           inp = int(input('Введите целое число: '))
           if type(inp) == int:
               return inp
 
       except:
           print('Это не целое число')
 
num = input_num1()
list = []
 
i = 1
u = 0
while i < int(num)+1:
   u = round((1 + 1/i)**i, 2)
   list.append(u)
   i = i+1
 
print(list)
sum = 0
for i in list:
  sum = sum + i
 
print(sum)
 
 
 
 
