def calculateCharges(c1,c2,c3,c4,c5):
    c1 -= 3
    c2 -= 3
    c3 -= 3
    c4 -= 3
    c5 -= 3
    
    
    if c1 <= 0:
        print('You have no charge to pay')
    else:
        price = c1 * 0.5

        print(price)

    if c2 <= 0:
        print('You have no charge to pay')
    else:
        price = c1 * 0.5

        print(price)

    if c3 <= 0:
        print('You have no charge to pay')
    else:
        price = c1 * 0.5

        print(price)

    if c4 <= 0:
        print('You have no charge to pay')

    else:
        price = c1 * 0.5

        print(price)

    if c5 <= 0:
        print('You have no charge to pay')

    else:
        price = c1 * 0.5

        print(price)

calculateCharges(1,2,3,4,5)