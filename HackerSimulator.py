#password hack simulator
import random
import time
pass_wordlist = ["^", "@", "%", "%", "g", "f", "!", "h", "i", "j", "k", "l", "m", "9", "+", "6", "2", "1", ">", "`", "u", "v", "w", "x", "y"]
pass_word = random.sample(pass_wordlist, random.randint(5, 7))
pass_word = "".join(pass_word)
print('this is a password hacking simulator!')
print('i do not condone actual hacking')
print('the password has been set! going to the sim...')
print(" ")


while True:
  print(' ')
  print(' ')
  print('how will you hack the password?')
  print('[1] Sql injection')
  print('[2] Brute force')
  print('[3] Keylog')
  print('[4] Phish The Password')
  print('[6] guess the password')
  hack = input('select one: ')
  print(' ')
  print(' ')
  

  if hack =="1":
    print('you sql inject into the website that contains the password...')
    time.sleep(2)
    if random.randint(1, 14) != 1:
      print('you failed to hack into the database!')
    else:
      print(f'you have successfully hacked into the database! after hours of searching you finally come across the password... and the password is... {pass_word} you can now guess it correctly!')
  
  if hack =="2":
    print('you go to the website and run your brute force tool and start cracking it')
    
    
