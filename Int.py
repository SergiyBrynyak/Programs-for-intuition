# Intuition training program
import random
print (
    """
Program for training intuition.
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
# series of 100 attemps, in testing mobe only 10.
while n < 10:
 zagad = str (random.randrange (2))
 print('Card №', n + 1, 'of 10')
 # Next command for testing! Displays generated number
 # print ('Fell =', zagad)
 r = input('Input "0" or "1"! For exit press enter "3"!')
 n += 1
 if r == zagad:
         sym += 1
     # For exit
 elif r == '3':
         break
     # Check: if the user does not introduced anything 
 elif not r:
         print('\nPlease repeat input, "0" or "1"! For exit press enter "3"!')
         n -= 1
 elif r == '1' or r == '0':
         print("Don't thinking! Listen the voice of intuition!")
     # Check: if the user incorect input
 else:
         n -= 1
         print('Your input is incorrect! Input "0" or "1"! For exit press enter "3"!')
print('\n\nResult: correct -', sym, '%', 'incorrect -', 10 - sym, '%')
input('\nPress Enter for exit..')
         
