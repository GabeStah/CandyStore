print('WELCOME TO CARL\'S CANDY CLUB')

#Below is me working on trying to create some for loops.
"""
candies = ['Candy Corns', 'Chocolate Chews', 'Jelly Jumpers', 'Raspberry Roll Ups']
for candy in candies:
    #print(candy)

    
candy_price = ['1.20','1.89','2.35','2.50']
print(type(candy_price))
"""


#Here down is what I actually submitted. This passed all tests.
#I was ashamed to turn this in. This was a 'just write something
#to pass.' Maybe not a lot better, but I am capable of better code.

#Creating global variables far as the eye can see. I 'feel' that these would
#be better as either function or lists(dictionariy,tuple,sets I'm not sure)

#these are the 4 candy items we're working with from start to end
c1 = 'Candy Corns'
c2 = 'Chocolate Chews'
c3 = 'Jelly Jumpers'
c4 = 'Raspberry Roll Ups'


#c1p = candy 1 (defined above) and its price
c1p = float(1.20)
c2p = float(1.89)
c3p = float(2.35)
c4p = float(2.50)


#Getting the # of items wanted and saving to a variable.
num_of_c1 = int(input(f'How many {c1} at ${c1p:.2f} do you want? '))
num_of_c2 = int(input(f'How many {c2} at ${c2p:.2f} do you want? '))
num_of_c3 = int(input(f'How many {c3} at ${c3p:.2f} do you want? '))
num_of_c4 = int(input(f'How many {c4} at ${c4p:.2f} do you want? '))

#formula used to see how much was spent for # of items requested
formfortotalc1 = (c1p * num_of_c1)
formfortotalc2 = (c2p * num_of_c2)
formfortotalc3 = (c3p * num_of_c3)
formfortotalc4 = (c4p * num_of_c4)

#formatting the amountper item
itemc1money = (f'{c1p:.2f}')
itemc2money = (f'{c2p:.2f}')
itemc3money = (f'{c3p:.2f}')
itemc4money = (f'{c4p:.2f}')

#formatting the total
moneytotalc1 = (f'{formfortotalc1:.2f}')
moneytotalc2 = (f'{formfortotalc2:.2f}')
moneytotalc3 = (f'{formfortotalc3:.2f}')
moneytotalc4 = (f'{formfortotalc4:.2f}')

#I hate everything about below. A lot of that was derived from the commented link
#from geeks for geeks
print()
print('Here is your receipt')
candy = ['Candy Corns', 'Chocolate Chews', 'Jelly Jumpers', 'Raspberry Roll Ups']
quant = [num_of_c1, num_of_c2, num_of_c3, num_of_c4]
price = [itemc1money, itemc2money, itemc3money, itemc4money]
total = [moneytotalc1, moneytotalc2, moneytotalc3, moneytotalc4]

#I used his formatting with the range and what not. But I would prefer to have
#used f string literals. But it tells me can't pass string to format or some such.
#but seems like I should be able to just do something like ${total:5.2f} instead of
# ${total[i] :>5}

for i in range(0, 4): #https://www.geeksforgeeks.org/string-alignment-in-python-f-string/
    print(f"{candy[i] :>20}{quant[i] :>4} at $ {price[i] :>2} = $ {total[i] :>5}")
totalspent = (formfortotalc1 + formfortotalc2 + formfortotalc3 + formfortotalc4)  
currency = (f'{totalspent:.2f}')
totalitems = (num_of_c1 + num_of_c2 + num_of_c3 + num_of_c4)
totalitemsstr = str(totalitems)
taxis = 0.08
taxformula = (taxis * totalspent)
taxtotal = (f'{taxformula:.2f}')
grand_total = (taxformula + totalspent)
gt = (f'{grand_total:.2f}')

print(f'TOTAL {totalitemsstr:>18} items       $ {currency:>5}')
print(f'TAX (8%)                             $ {taxtotal:>5}')
print('==============================================')

print(f'GRAND TOTAL                         $  {gt:>5}')
print()
print()
print()
print()
print()



amount_paid = int(input('How much money did you receive? '))
due_back = (amount_paid - grand_total)
print(f'The amount due back is ${due_back:.2f}')
change = round(due_back * 100)
print('That is', change, 'cents')
print('Please give the customer the following:')

#when trying to get all of the below code into a function I was using
# https://tinyurl.com/1r9sejnc 
# https://www.youtube.com/watch?v=DGS6_5EAebs
# https://www.youtube.com/watch?v=2di3e7mOyCI&feature=emb_title
twenties = change // 2000;
change = change % 2000;

tens = change // 1000;
change = change % 1000;

fives = change // 500;
change = change % 500;

ones = change // 100;
change = change % 100;

quarters = change // 25;
change = change % 25;

dimes = change // 10;
change = change % 10;

nickels = change // 5;
change = change % 5;

pennies = change // 1;
change = change % 1;

zero = 0


def currency_give(): #https://www.youtube.com/watch?v=9Os0o3wzS_I 
    if (twenties > zero): #https://www.tutorialspoint.com/python/comparison_operators_example.htm
        print(f'{twenties} $20s')
    if (tens > zero):
        print(f'{tens} $10s')
    if (fives > zero):
        print(f'{fives} $5s')
    if (ones > zero):
        print(f'{ones} $1s')
    if (quarters > zero):
        print(f'{quarters} quarters')
    if (dimes > zero):
        print(f'{dimes} dimes')
    if (nickels > zero):
        print(f'{nickels} nickels')
    if (pennies > zero):
        print(f'{pennies} pennies')
        
currency_give()
