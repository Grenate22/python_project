correct_pin=input('Create your four digit pin: ')
while len(correct_pin)!=4 or (not correct_pin.isdigit()):
    print('not a 4 digit pin')
    correct_pin = input('Create your four digit pin:')
correct_pin=int(correct_pin)
print('press 1 to check Balance\npress 2 for Airtime Topup\npress 3 to Send Money')
user_input=int(input('press a digit for any operation you will like to perform :'))
Balance=1000


def balance():
    guess=3
    while guess!=0:
        pin = int(input("Enter your 4 digit pin: "))
        if pin ==correct_pin:
            return Balance
        else:
            return str(f'incorrect pin provided {guess-1} trials left')
        guess-=1
    else:
        return str('Your Account has been suspended')
def Airtime():
    mynumber=2349034767600
    print('press 1 to load for myslef\npress 2 to load New Number')
    userin=int(input('input a digit: '))
    if userin==1:
        print('Kindly enter the network operator\n\npress A for Airtel\npress B for MTN\npress C for Glo')
        airtime_input=input('Enter a letter: ')
        if airtime_input.upper()=='A':
            airtimeamout=input('How much do you want to recharge: ')
            print(f'If this is okay,respond with PAY to contiunue this process or respond with CANCEL to terminate this process\n\n.Network: AIRTEL\n.Phone number:{mynumber}\n.Amount:{airtimeamout}\n\nA.PAY\nB.CANCEL')
            airtimepaymentoption=input('PAY OR CANCEL: ')
            if airtimepaymentoption.upper()=='PAY':
                print(f'Your {mynumber} is recahrge with {airtimeamout}')
                curent_balance=int(Balance)-int(airtimeamout)
                return str(f'you have {curent_balance} left in your wallet ')


if user_input==1:
    print(balance())
elif user_input==2:
    print(Airtime())
elif user_input==3:
    print('coming back to you')
else:
    print('wrong input')
