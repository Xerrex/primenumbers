def printprimenumber(n):
    valuelist=[]

    if type(n)!=int:
        raise ValueError('number Must be integer')
    elif n==1:
        return 'Input must be greater than 1'
    elif n<1:
        return 'Input values should not be negatives'
    else:
        for number in range(2,n+1):
            """
            gets a the numbers between the range of 2 to n
            """
            if number==2:
                """
                add 2 before hand
                """
                valuelist.append(number)


            for divisor in range(2,number):
                """
                check if the number has a divisor from 2 to number -1
                if none the number is a prime number
                """
                if number%divisor==0:
                    break
                elif number not in valuelist:
                    valuelist.append(number)



        return valuelist



print(printprimenumber(10))
