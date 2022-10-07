while True:                                                                       #Проверка на дурака
    try:
        n=int(input('Введите граничное число массива: '))                                  
        break
    except ValueError:
         print('Вы должны ввести число! Попробуйте снова!')
if n%2 ==0:
    print('Ошибка')
a=[0]*n
for i in range(n):
    a[i]=int(input())
print(a)
p=0
for i in range(n):
    if a[i]>a[len(a)//2]:
        p+=1
print(p)    
