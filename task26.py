# Задача 26: Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def f(A,B):
    if B==1:
        return A
    elif B==0:
        return 1
    else:
        return A*f(A,B-1)


A=int(input("Enter A: "))
B=int(input("Enter B: "))
print(f"{A} в степени {B} = {f(A,B)}")