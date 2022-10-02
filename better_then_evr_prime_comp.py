number = int(input("Enter number: "))
factors = []
for i in range(2,number):
    while number%i ==0:
        factors.append(i)
        number /= i
if number>1:
    factors.append(number)
str_of_factors = ''
sum = 0
if len(factors) >1:
    print("Is composite")
    for i in factors:
        i = str(i)
        str_of_factors += i + ' '
    print(f"factors of composite are : {str_of_factors}")
    for q in factors:
        sum += q
    print(f"Sum of factors is {sum}")
else:
    print("Is prime")
