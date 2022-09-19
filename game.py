from random import randint
from balance import many
slot = randint(1, 30)
bank = many

def game():
    global bank
    print('Welcome to KAZINO!!!')
    try:
        while 1:
            print(f'Your balance: {bank}')
            com = input('Choose\n1 Play \n2 Exit\n')
            if com == '1':
                insrt = int(input('Choose the slot: '))
                stav = int(input('Your bid: '))
                if insrt == slot and stav <= bank:
                    bank += (stav*5)
                    print('You win!')
                elif slot != insrt and stav <= bank:
                    if bank > 0 and stav <= bank:
                        bank -= stav
                        print('You lose!')
                elif bank == 0:
                    print('You losed your all money')
                    continue
                elif stav > bank:
                    print('You don not have enough funds!')
            elif com == '2':
                if bank < 1000:
                    print('You are a loser')
                    print('Game over!!!')
                    print(f'Your balance {bank}')
                    break
                elif bank > 1000:
                    print('You are a winner')
                    print('Game over!!!')
                    print(f'Your balance {bank}')
                    break
            else:
                print('No such action!')
    except TypeError:
        print('Something went wrong!')
    except ValueError:
        print('Write only numbers!')
    except Exception:
        print('Something went wrong')