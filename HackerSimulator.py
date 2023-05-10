#password hack simulator
#works for replit on school computers
#NOT FINISHED
import random
import time


#shop
kali = 500
flipperz = 300
ddos = 20
winpc = 5000
wifia = 30
gpc = 10000
busb = 50
tvpn = 100


#jobs and money
usermoney = 10
lawnm = 15
ptj = 25
bc = 1000
bcl = 10000
ds = 20
bs = 15
sh = 20
cheat =  10000

#status
userstatus = 'old laptop'
userstatus1 = 'nothing'
userstatus2 = 'nothing'
userstatus3 = 'nothing'
userstatus4 = 'nothing'
userstatus5 = 'nothing'
userstatus6 = 'nothing'
userstatus7 = 'nothing'
userstatus8 = 'nothing'


print('welcome to hacker simulator!')
print('type in "r" to see the rules!')
print('first we need to make some money!')
print(' ')
print('how do you want to start off?')

while True:
  print(' ')
  print(' ')
  if usermoney < 1:
    print(f'game over! you went bankrupt!! your final amount of money: {usermoney}')
    print(' ')
    print(' ')
    time.sleep(5)
    exit()  
  print(' ')
  print(' ')
  print('starting jobs: ')
  print(' ')
  print('[1] mowing lawns -            (15 dollars per 5 seconds)')
  print('[2] part time job -           (25 dollars per 10 seconds)')
  print('[3] bitcoin -                 (1000 dollars per minute, high chance of losing 10000)')
  print('[4] drop shipping -           (20 dollars per 7 seconds)')
  print('[5] babysitting -             (15 dollars per 5 seconds)')
  print('[6] selling hardware -        (20 dollars per 10 seconds)')
  print('[7] dumpster diving -         (10-200 dollars per 15 seconds)')
  print(' ')
  print('misc:')
  print(' ')
  print('[8] shop')
  print('[9] status')
  print('[10] hack')
  print('[11] cheat code')
  print('[12] extentions page (bought from shop)')
  print(' ')
    
  start = input('select one: ')
  print(' ')
  print(' ')
	
  if start =="1":
    print('you mow a lawn...')
    time.sleep(5)
    print('congrats! you made 15 dollars!')
    usermoney = usermoney + lawnm
    print(f'money made so far: {usermoney}')
    print(' ')
    print(' ')


  if start =="2":
    print('you go to mcdonalds and work for a hour...')
    time.sleep(10)
    print('congrats! you made 25 dollars!')
    usermoney = usermoney + ptj
    print(f'money made so far: {usermoney}')
    print(' ')
    print(' ')

  if start =="3":
    print('your friend lets you borrow 500 dollars worth of bitcoin')
    print('please wait 1 minute..')
    time.sleep(60)
    if random.randint(1, 5) != 1:
      print(' ')
      print('you made 1000 dollars!!')
      usermoney = usermoney + bc
      print(f'money so far: {usermoney}')
      print(' ')
      print(' ')
    else:
      print('you lost 10000 dollars!! money doesnt come easy!')
      usermoney = usermoney - bcl
      print(f'money so far: {usermoney}')
      print(' ')    
      print(' ')
      
  if start =="4":
    print('you drop ship some random wish.com item')
    time.sleep(7)
    print('you sold 1 item!')
    usermoney = usermoney + ds
    print(f'money made so far: {usermoney}')
    print(' ')
    print(' ')
    
  if start =="5":
    print('you babysit some kids..')
    time.sleep(5)
    print('you got paid!')
    usermoney = usermoney + bs
    print(f'money made so far: {usermoney}')
    print(' ')
    print(' ')
    
  if start =="6":
    print('you sell some computer chips you have laying around..')
    time.sleep(10)
    print('you made 20 dollars!')
    usermoney = usermoney + sh
    print(f'money made so far: {usermoney}')
    print(' ')
    print(' ')

  if start =="7":
    dd = random.randint(10, 200)
    print('you go behind an apple store and dive in their dumpster..')
    print('please wait...')
    time.sleep(15)
    print(f'you made {dd} amount of money!')
    usermoney = usermoney + dd
    print(f'money made so far: {usermoney}')
    print(' ')
    print(' ')

  if start =="8":
    print('-----------------------------------------------------------------')
    print(f'your money: {usermoney}')
    print('shop:')
    print('[1] kali linux laptop (slow) (500 dollars)')
    print('[2] flipper zero (300 dollars)')
    print('[3] ddos toolkit (20 dollars)')
    print('[4] windows pc (fast) (5000 dollars)')
    print('[5] wifi adapter (for aircrack-ng) (30 dollars)')
    print('[6] gaming pc (for gaming) (super fast) (10000 dollars)')
    print('[7] badusb (50 dollars)')
    print('[8] tor vpn (less likely to be caught) (100 dollars)')
    print('-----------------------------------------------------------------')
    print(' ')
    shop = input('Buy something: ')
	
    if shop =="1":
      print('      ')
      print('      ')
      print('you chose: kali linux laptop')
      print(f'your money after this purchase will be: {usermoney - kali}')
      if usermoney > 500:
        if (input("Type p to purchase, anything else to go back ") == "p"):
         usermoney = usermoney - kali
        print('you bought a kali linux laptop!')
        userstatus1 = 'kalil'
      else:
          print('sorry! you dont have enough money!')
        
      print('      ')
      print('      ')
  
  
    if shop =="2":
      print('      ')
      print('      ')
      print('you chose: flipper zero')
      print(f'your money after this purchase will be: {usermoney - flipperz}')
      if usermoney > 300:
        if (input("Type p to purchase, anything else to go back ") == "p"):
         usermoney = usermoney - flipperz
        print('you bought a flipper zero!')
        userstatus2 = 'flz'
      else:
          print('sorry! you dont have enough money!')   
      print('      ')
      print('      ')
  
    if shop =="3":
      print('      ')
      print('      ')
      print('you chose: ddos toolkit')
      print(f'your money after this purchase will be: {usermoney - ddos}')
      if usermoney > 20:
        if (input("Type p to purchase, anything else to go back ") == "p"):
         usermoney = usermoney - ddos
        print('you bought a ddos toolkit!')
        userstatus3 = 'ddos'
      else:
          print('sorry! you dont have enough money!')   
      print('      ')
      print('      ')
  
  
    if shop =="4":
      print('      ')
      print('      ')
      print('you chose: windows pc (fast) ')
      print(f'your money after this purchase will be: {usermoney - winpc}')
      if usermoney > 5000:
        if (input("Type p to purchase, anything else to go back ") == "p"):
         usermoney = usermoney - winpc
        print('you bought a windows pc!')
        userstatus4 = 'windpc'
      else:
          print('sorry! you dont have enough money!')   
      print('      ')
      print('      ')
  
  
    if shop =="5":
      print('      ')
      print('      ')
      print('you chose: wifi adapter (for aircrack ng)')
      print(f'your money after this purchase will be: {usermoney - wifia}')
      if usermoney > 30:
        if (input("Type p to purchase, anything else to go back ") == "p"):
         usermoney = usermoney - wifia
        print('you bought a wifi adapter!')
        userstatus5 = 'wa'
      else:
          print('sorry! you dont have enough money!')   
      print('      ')
      print('      ')
  
    if shop =="6":
      print('      ')
      print('      ')
      print('you chose: gaming pc')
      print(f'your money after this purchase will be: {usermoney - gpc}')
      if usermoney > 10000:
        if (input("Type p to purchase, anything else to go back ") == "p"):
         usermoney = usermoney - gpc
        print('you bought a gaming pc!')
        userstatus6 = 'gamepc' 
      else:
          print('sorry! you dont have enough money!')   
      print('      ')
      print('      ')
  
    if shop =="7":
      print('      ')
      print('      ')
      print('you chose: badusb')
      print(f'your money after this purchase will be: {usermoney - busb}')
      if usermoney > 50:
        if (input("Type p to purchase, anything else to go back ") == "p"):
         usermoney = usermoney - busb
        print('you bought a badusb!')
        userstatus7 = 'badusb'
      else:
          print('sorry! you dont have enough money!')   
      print('      ')
      print('      ')

    
    if shop =="8":
      print('      ')
      print('      ')
      print('you chose: tor vpn')
      print(f'your money after this purchase will be: {usermoney - tvpn}')
      if usermoney > 100:
        if (input("Type p to purchase, anything else to go back ") == "p"):
         usermoney = usermoney - tvpn
        print('you bought a tor vpn!')
        userstatus8 = 'torvpn'
      else:
          print('sorry! you dont have enough money!')   
      print('      ')
      print('      ')
    
  if start =="11":
    print(' ')
    print(' ')
    print('cheat code 1: givcash (adds 10000 dollars to your account')
    print('more cheat codes possibly coming soon!')
    cheater = input('enter the cheat code: ')
    print(' ')
    if cheater =="givcash":
      usermoney = usermoney + cheat
      print('cheat success!')
    
      

  if start =="12":
    print('extentions page:')
    print('if nothing shows up you didnt buy and extentions from the shop!')

    if userstatus1 =='kalil':
      print(' ')
      print(' ')
      print('kali hacks (10-100 dollars per 5 seconds)')
      if (input("do you want to use this extention? (y/n): ") == "y"):
        print('what do you want to do?')
        print('[1] password hack (for a bank account, possible 300-5000 dollars)')
        print('[2] make a virus')
        print('[3] sql inject into websites and dump their database')
        kaly = input('select one: ')
      else: 
        if userstatus2 =='flz':
          print(' ')
          print(' ')
          print('flipper hacking (no money execpt chaos)')
          if (input("do you want to use this extention? (y/n): ") == "y"):
            print('not finished!')
        else:
          
          if userstatus3 =='ddos':
            print(' ')
            print(' ')
            print('ddos (down a server or something)')
            if (input("do you want to use this extention? (y/n): ") == "y"):
              print('not finished!')
          else:
            
            if userstatus4 =='windpc':
              print(' ')
              print(' ')
              print('fast hacking with windows pc (possible chance of money per 4 seconds)')
              if (input("do you want to use this extention? (y/n): ") == "y"):
                print('not finished!')
              else:
                
                if userstatus5 =='wa':
                  print(' ')
                  print(' ')
                  print('aircrack-ng (possible 30-100 dollars per 7 seconds)')
                  if (input("do you want to use this extention? (y/n): ") == "y"):
                    print('not finished!')
                  else:
                    
                    if userstatus6 =='gamepc':
                      print(' ')
                      print(' ')
                      print('gaming pc (make money by playing games, chance of 50000 dollars per 13 seconds)')
                      if (input("do you want to use this extention? (y/n): ") == "y"):
                        print('not finished!')
                      else:
                        
                        if userstatus7 =='badusb':
                          print(' ')
                          print(' ')
                          print('badusb (steal passwords and sell them, chance of 200 dollars)')
                          if (input("do you want to use this extention? (y/n): ") == "y"):
                            print('not finished!')
                          else:
  
                            if userstatus8 =='torvpn':
                              print(' ')
                              print(' ')
                              print('connect to tor vpn (lessens your chance of being caught)')
                              if (input("do you want to use this extention? (y/n): ") == "y"):
                                print('not finished!')
    



if kaly =="1":
  money = random.randint(300, 5000)
  
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
        usermoney = usermoney + money
        time.sleep(2)
        break
      else:
        print(' ')
        print('Wrong!')
      
  if kaly =="2":
    print(' ')
    print(' ')
    print('what type of virus?')
    print('[1] rat (remote access trojan)')
    print('[2] ransomware')
    print('[3] spyware')
    virus = input('enter one: ')
  if virus =="1":
    print('you stay up all night creating one and you post it online as a mod menu for gta...')
    time.sleep(4)
    if random.randint(1, 20) != 1:
      print(' ')
      print('the file was flagged as unsafe then later removed!')
      print(' ')
    else:
      print(' ')
    
