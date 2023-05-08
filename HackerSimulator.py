#password hack simulator
import random
import time

money = random.randint(8000, 99999)

pass_wordlist = ["^", "@", "%", "%", "g", "f", "!", "h", "i", "j", "k", "l", "m", "9", "+", "6", "2", "1", ">", "4", "u", "v", "w", "x", "y"]
pass_word = random.sample(pass_wordlist, random.randint(5, 7))
pass_word = "".join(pass_word)

pass_word1 = random.sample(pass_wordlist, random.randint(5, 7))
pass_word1 = "".join(pass_word1)

pass_word2 = random.sample(pass_wordlist, random.randint(5, 7))
pass_word2 = "".join(pass_word2)

pass_word3 = random.sample(pass_wordlist, random.randint(5, 7))
pass_word3 = "".join(pass_word3)

pass_word4 = random.sample(pass_wordlist, random.randint(5, 7))
pass_word4 = "".join(pass_word4)

pass_word5 = random.sample(pass_wordlist, random.randint(5, 7))
pass_word5 = "".join(pass_word5)

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
  print('[5] Dictionary attack')
  print('[6] Man In The Middle')
  print('[7] Rat (Remote Access Trojan)')
  print('[8] Guess The Password')
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
    print('you go to the website and run your brute force tool and start cracking')
    print('you wait days for the attack to be completed...')
    time.sleep(4)
    if random.randint(1, 20) != 1:
      print(' ')
      print('you failed to brute force into the password! you are now ip blacklisted from the')
      print('website! you connected to a vpn and now you can retry:')
      print(' ')
    else:
      print(' ')
      print('you actually did it! you successfully brute forced the password!')
      print(f'the last password guessed is {pass_word}, you can now guess it!')
      print(' ')

  if hack =="3":
    print('you send the target a keylogger through email..')
    time.sleep(2)
    if random.randint(1, 4) != 1:
      print('they deleted the email!')
    else:
      print('they opened the file and you start logging their keys...')
      time.sleep(2)
      print(f'''
      
      after a week of logging their keys you come up with 6 possible passwords:
      
      1: {pass_word1}
      2: {pass_word2}
      3: {pass_word}
      4: {pass_word4}
      5: {pass_word3}
      6: {pass_word5}
      
      ''')

  if hack =="4":
    print('you send them an email claiming you are the company and demands the password...')
    time.sleep(2)
    if random.randint(1, 9) != 1:
      print('the email ended up in their spam folder and later was deleted!')
    else:
      print('they actually fell for it! you got their password!')
      print(f'this seems too easy! their password is {pass_word}')


  if hack =="5":
    print('You use the rockyou txt wordlist to attack the password and wait days for the result')
    time.sleep(2)
    if random.randint(1, 25) != 1:
      print('You failed to get in!')
    else:
      print('Wow! you managed to crack the password!')
      print(f'the last guessed password is {pass_word}')

  if hack =="6":
    print('you intercept the users messages and wait...')
    time.sleep(3)
    if random.randint(1, 5) != 1:
      print('the user never sends his password..')
    else:
      print(f'''
      You come across his password in one of his emails to the company (what an idiot)
      the email is:
      
      "Hello bank people, I found a bug in your system,
      whenever I deposit money I loose 100 dollars! please give me back my money!
      my username is: user123
      and my password is: {pass_word}
      please recover my cash!"
      
      you can now guess the password! {pass_word}
      ''')

  if hack =="7":
    print('you send the user a RAT (remote access trojan)...')
    time.sleep(2)
    if random.randint(1, 4) != 1:
      print('the file was deleted by windows defender!')
    else:
      print('they opened the file and you accessed their chrome passwords..')
      if random.randint(1, 3) != 1:
        print('they dont have the password stored inside their chrome passwords!')
      else:
        print(f'You found the password! it is: {pass_word}')

  if hack =="8":
    guess = input('Guess The Password: ')
    if guess ==pass_word:
      print(f'''
      You got it! you now have access to:
      {money} USD!
      ''')
      time.sleep(2)
      if (input("Type q to quit, anything else for another round: ") == "q"):
        break
  
    else:
      print(' ')
      print('Wrong!')
