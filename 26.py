# Задача 26: Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def exponentiation(a, b):
    exp = 1
    for i in range(b):
        exp = exp * a
    return exp

print(exponentiation(3, 5))