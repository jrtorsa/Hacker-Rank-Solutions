import decimal

arr = [-4, 3, -9, 0, 4, 1,]

def plusMinus(arr):
    arr_len = len(arr)
    counter1 = 0
    counter2 = 0
    counter3 = 0

    for i, v in enumerate(arr, 0):
        if v > 0:
            counter1 += 1
        if v < 0:
            counter2 += 1
        if v == 0:
            counter3 += 1
        
        # result = format(counter1/ arr_len, '.6f'), format(counter2/ arr_len, '.6f'), format(counter3/ arr_len, '.6f')
        result = decimal.Decimal(format(counter1/ arr_len, '.6f'))
        result2 = decimal.Decimal(format(counter2/ arr_len, '.6f'))
        result3 = decimal.Decimal(format(counter3/ arr_len, '.6f'))

    return print(result, '\n',result2, '\n',result3) 
    
plusMinus(arr)