
import time

# start of project
print('Welcome to our bank ')

# take the card number from user
CardNumber = input('plz enter the card Number ')
Pin = input('plz enter ur Pin ')

# create an list as indector for Pin matrix
Passwords = ['159357', '123456', '987654']

# create an tuple as indecator to exist acount
Account = ('1', '2', '3')

# create an list as indecator or the amount of AmountOfMoney in account  in EGY
AmountOfMoney = {'1': 200000, '2': 1000000, '3': 2500000}

# cheak if card number is valid
if CardNumber in Account and Pin in Passwords[Account.index(CardNumber)]:
    print('Please wait while your Transaction is processing')
    time.sleep(1)
    print('Welcome To Your Account')
    A = 'Y'
    while A == 'Y':
        # start to take the Op that user want to exqute in Atm
        Op = input(' Press 1 to Withdrow\n Press 2 to Deposit ')

        # if the user choose to withrow amount enter the withdrow system
        if Op == '1':
            # take the caranc from user to calculate the defrance in Currency
            Currency = input('PLease Choose Currancy:   $    EURO   EGY     ')
            if Currency == 'DOLLAR':
                X = input('plz enter the amount of AmountOfMoney')
                # calculate the amount using the defrance in Currency
                AmountOfMoney[CardNumber] -= (int(X)*30)
                print('Done ... ur amount now  =  ', AmountOfMoney[CardNumber])
                A = input(
                    'for anather Op press Y   / for end process press N   ')
            elif Currency == 'EURO':
                X = input('plz enter the amount of AmountOfMoney ')
                # calculate the amount using the defrance in Currency
                AmountOfMoney[CardNumber] -= (int(X)*34)
                print('Done ... ur amount now  =  ', AmountOfMoney[CardNumber])
                A = input(
                    'for anather Op press Y   / for end process press N   ')
            elif Currency == 'EGY':
                X = input('plz enter the amount of AmountOfMoney ')
                # calculate the amount using the defrance in Currency
                AmountOfMoney[CardNumber] -= int(X)
                print('Done ... ur amount now  = %d  EGY ',
                      AmountOfMoney[CardNumber])
                A = input(
                    'for anather Op press Y   / for end process press N   ')
        elif Op == '2':
            Currency = input('plz enter Currency   :   $    EURO   EGY      ')
            if Currency == 'DOLLAR':
                X = input('plz enter the amount of AmountOfMoney ')
                # calculate the amount using the defrance in Currency
                AmountOfMoney[CardNumber] += (int(X)*30)
                print('Done ... ur amount now  =  ', AmountOfMoney[CardNumber])
                A = input(
                    'for anather Op press Y   / for end process press N   ')
            elif Currency == 'EURO':
                X = input('plz enter the amount of AmountOfMoney ')
                # calculate the amount using the defrance in Currency
                AmountOfMoney[CardNumber] += (int(X)*34)
                print('Done ... ur amount now  =  ', AmountOfMoney[CardNumber])
                A = input(
                    'for anather Op press Y   / for end process press N   ')
            elif Currency == 'EGY':
                X = input('plz enter the amount of AmountOfMoney ')
                # calculate the amount using the defrance in Currency
                AmountOfMoney[CardNumber] += int(X)
                print('Done ... ur amount now  = %d EGY ',
                      AmountOfMoney[CardNumber])
                A = input(
                    'for anather Op press Y   / for end process press N   ')
        else:
            print('invalid Op')
            A = input('for anather Op press Y   / for end process press N   ')
else:
    print('Please wait while your Transaction is processing')
    time.sleep(1)
    print('invalied card number')
