def rozrah (sym_rez, card):
 """Counting results"""
# if you have result 50\50 it means that your intuition not working now
# if you have result 60\10 or 10\60 it means that your intuition working on 20%
 sym = int(0)
 for i in range(len(sym_rez)):
  sym += sym_rez[i]
 if sym < card:
  real_sym = -((card - sym)*100)/card
 elif sym == card:
  real_sym = 0   
 else:
  real_sym = ((sym - card) * 100)/card
 return real_sym

def correct_nepr (sym):
 """Finding value of incorect answers"""
 nepr = int(0)
 if sym == 0:
     nepr = 100
 elif sym < 0:
     nepr = -(100 + sym)
 else:
     nepr = 100 - sym
 return nepr

def real_print (rez):
 """ Printing results"""
 print('\n\nSummary Results:')
 sym100 = int(rozrah(rez, 50))
 print('------------------------------------------------------------------')
 print('Large range of 100 cards (correct | incorrect):')
 print('------------------------------------------------------------------')
 print('[', sym100, '/', correct_nepr(sym100), '%]')
 print('\n------------------------------------------------------------------')

 rez50_1 = rez [:50]
 rez50_2 = rez [50:]
 sym50_1 = int(rozrah(rez50_1, 25))
 sym50_2 = int(rozrah(rez50_2, 25))
 print('Two intervals of 50 cards (correct | incorrect):')
 print('------------------------------------------------------------------')
 print('[', sym50_1, '/', correct_nepr(sym50_1),
       '%][', sym50_2,'/', correct_nepr(sym50_2),'%]')
 print('\n------------------------------------------------------------------')

 rez20_1 = rez [:20]
 rez20_2 = rez [20:40]
 rez20_3 = rez [40:60]
 rez20_4 = rez [60:80]
 rez20_5 = rez [80:]
 sym20_1 = int(rozrah(rez20_1, 10))
 sym20_2 = int(rozrah(rez20_2, 10))
 sym20_3 = int(rozrah(rez20_3, 10))
 sym20_4 = int(rozrah(rez20_4, 10))
 sym20_5 = int(rozrah(rez20_5, 10))
 print('5 small intervals of 20 cards (correct | incorrect):')
 print('------------------------------------------------------------------')
 print('[', sym20_1, '/', correct_nepr(sym20_1),
       '%][', sym20_2,'/', correct_nepr(sym20_2),
       '%][', sym20_3,'/', correct_nepr(sym20_3),
       '%][', sym20_4,'/', correct_nepr(sym20_4),
       '%][', sym20_5,'/', correct_nepr(sym20_5),
       '%]'
       )
 print(
     """
* If you have better result on small intervals it means that
  your intuition working a little time and then be tired.
**If you have a lot of "-" values it may means, that you have
  inverse intuition (if your intuition said "yes" in real it
  means "no"). This is often been in beginners.
     """
     )
 print('\nList of your correct(1) and incorrect(0) answers:')
 print(rez20_1)
 print(rez20_2)
 print(rez20_3)
 print(rez20_4)
 print(rez20_5)
 print(
"""
(If you have correct(1) and incorrect(0) answers 50/50 it
means that your intuition not working now)
""")
#
# Intuition training program
import random
print (
    """
Program for training or testing intuition.
The program generated two number '1' or '0',
and you have to guess what fell. You have 100
attemps. Then the program show you results of
your training.
    """
    )
n = 0
sym = int(0)
# r - variable input
r = ''
rez = []
# series of 100 attemps
while n < 100:
 zagad = str (random.randrange (2))
 print('Card №', n + 1, 'of 100')
 # Next command for testing! Displays generated number
 # print ('Fell =', zagad)
 # Next command for testing! Generate "inpute"
 # r = str (random.randrange (2))
 r = input('Input "0" or "1"! For exit press enter "3"!')
 n += 1
 if r == zagad:
         rez.append(1)
     # For exit
 elif r == '3':
         break
     # Check: if the user does not introduced anything 
 elif not r:
         print('\nPlease repeat input, "0" or "1"! For exit press enter "3"!')
         n -= 1
 elif r == '1' or r == '0':
         rez.append(0)
         print("Don't thinking! Listen the voice of intuition!")
     # Check: if the user incorect input
 else:
         n -= 1
         print('Your input is incorrect! Input "0" or "1"! For exit press enter "3"!')
real_print(rez)
input('\nPress Enter for exit..')
         
