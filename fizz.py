
for number in range (1,101):
    if number% 5 ==0:
        if number% 3 !=0:
            print('buzz')
        if number%3== 0:
            print('fizzbuzz')   
    elif number % 3==0:
        if number% 5!=0:
             print('fizz')    
    else:
        print(number)