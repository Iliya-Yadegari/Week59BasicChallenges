def multiple(first,second):
    answer = second / first

    if answer ==  round(answer):
        print('It is a multiple')
    else:
        print('It is not a multiple')
        
multiple(2,4)