#1
#def help_me():
 #   print("Save me please I need your help с кр по проге")
#help_me() #функцию надо вызвать, а не просто объявить, тогда результат считается.

#2
#s = "abc"
#print(len(s)) - ,budet schitat'

#3
#def help_me(n, m):
  #  print(n)
   # print(m)
#help_me(5, 6) #сколько объектов объявляем - столько должно быть при вызове функции

#4
#n = 7
#m = 8 #переменные в функциях не имеют отношения к переменным вне функции,то, что происходит в функции остается внутри функции
#def help_me(n, m):
 #   n=9
  #  m= 10
   # print(n)
    #print(m)
#help_me(5,6)
#print(n, m)

#5
#n = 7
#m = 8 #переменные в функциях не имеют отношения к переменным вне функции,то, что происходит в функции остается внутри функции
#def help_me(n, m):
 #  x = n+m
  # print(n)
   #print(m)
#help_me(5,6)
#print(x)#переменная икс задана внутри функции и не видима программе поэтому ошибка

#6
#n = 7
#m = 8 #переменные в функциях не имеют отношения к переменным вне функции,то, что происходит в функции остается внутри функции
#def help_me(n, m):
  #  x =n+m
 #   return x
#x = help_me(5,6)
#print(x)

#7
def need_help(n, m):
    x = n+m
    return x
def help_need(n, m):
    y = n - m
    return y
def need_help_too_much():
    n = int(input("Add sth: "))
    m = int(input("Add sth: "))
    x = need_help(n, m)
    y = help_need(x, m)
    print(y)
need_help_too_much()
