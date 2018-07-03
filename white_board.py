
def even_fibo(number):
    fibo_l = []
    result_l = []
    latest_fibo_num = 0
    roop = 1
    while latest_fibo_num < number:
        if roop == 1:
            fibo_l.append(0)
            roop += 1
            continue
        if roop == 2:
            fibo_l.append(1)
            latest_fibo_num = 1
            roop += 1
            continue
        latest_fibo_num = fibo_l[-1] + fibo_l[-2]
        fibo_l.append(latest_fibo_num)
        if latest_fibo_num % 2 == 0:
            result_l.append(latest_fibo_num)
        roop += 1
    print(fibo_l)
    print(result_l)

even_fibo(2)