#dorkdox v 0.0.1
#Coded by qolhf
#run python3 install.py before running this
#read terms.txt

try:
  import os
  import sys
  import time
  from pygoogling.googling import GoogleSearch # Google search library
  import colorama
  from colorama import Fore, Style
except:
  print("\n[!] Some python modules are missing!")

os.system('clear')
print(Fore.RED)
os.system('figlet Dork Dox')
print()
print('''
1) Enter Name
2) Enter Phone Number
3) Enter Email
4) Enter Nickname
5) Enter Username
''')
print()
print('6) Credits')
print('7) Exit')
print()
print('Enter An Option..')  
cmd = input('dorkdox@dorkdox:~# ')
  
if cmd == '1':
  os.system('clear')
  os.system('figlet Name Search')
  print("Enter The Name")
  name = input('dorkdox@dorkdox:~# ')
  os.system('clear')
  print("Searching.")
  os.system('clear')
  time.sleep(1)
  print("Searching..")
  os.system('clear')
  time.sleep(1)
  print("Results For "+name+"")
  os.system('clear')
  google_search = GoogleSearch("allintext:"+name+"")
  google_search.start_search(max_page=1) # prints first page of google resulrs
  print(google_search.search_result) # will print the url as list of string
  print(google_search.search_result) # the result will be added to current result
  print("If you want to follow any of these URLs, simply paste them into your browser!")
  print()
  print("Have a good day!")
  sys.exit()

  

if cmd == '2':
  os.system('clear')
  os.system('figlet Phone Number Search')
  print("Enter The Phone Number")
  email = input('dorkdox@dorkdox:~# ')
  os.system('clear')
  time.sleep(1)
  print("Results For "+email+"")
  time.sleep(1)
  os.system('clear')
  google_search = GoogleSearch("allintext:"+email+"")
  google_search.start_search(max_page=1) # prints first page of google resulrs
  print(google_search.search_result) # will print the url as list of string
  print(google_search.search_result) # the result will be added to current result
  print("If you want to follow any of these URLs, simply paste them into your browser!")
  print()
  print("Have a good day!")
  sys.exit()
    
if cmd == '3':
  os.system('clear')
  os.system('figlet Email Search')
  print("Enter The Email")
  email = input('dorkdox@dorkdox:~# ')
  os.system('clear')
  time.sleep(1)
  print("Results For "+email+"")
  time.sleep(1)
  os.system('clear')
  google_search = GoogleSearch("allintext:"+email+"")
  google_search.start_search(max_page=1) # prints first page of google resulrs
  print(google_search.search_result) # will print the url as list of string
  print(google_search.search_result) # the result will be added to current result
  print("If you want to follow any of these URLs, simply paste them into your browser!")
  print()
  print("Have a good day!")
  sys.exit() 

if cmd == '4':
  os.system('clear')
  os.system('figlet Nickname Search')
  print("Enter The Nickname")
  nick = input('dorkdox@dorkdox:~# ')
  os.system('clear')
  time.sleep(1)
  print("Results For "+nick+"")
  time.sleep(1)
  os.system('clear')
  google_search = GoogleSearch("allintext:"+nick+"")
  google_search.start_search(max_page=1) # prints first page of google resulrs
  print(google_search.search_result) # will print the url as list of string
  print(google_search.search_result) # the result will be added to current result
  print("If you want to follow any of these URLs, simply paste them into your browser!")
  print()
  print("Have a good day!")
  sys.exit() 

if cmd == '5':
  os.system('clear')
  os.system('figlet Username Search')
  print("Enter The Username")
  user = input('dorkdox@dorkdox:~# ')
  os.system('clear')
  time.sleep(1)
  print("Results For "+user+"")
  time.sleep(1)
  os.system('clear')
  google_search = GoogleSearch("allintext:"+user+"")
  google_search.start_search(max_page=1) # prints first page of google resulrs
  print(google_search.search_result) # will print the url as list of string
  print(google_search.search_result) # the result will be added to current result
  print("If you want to follow any of these URLs, simply paste them into your browser!")
  print()
  print("Have a good day!")
  sys.exit() 

if cmd == '6':
  os.system('clear')
  def creditsbanner():
    os.system('toilet --font mono12 -F border -F gay Credits')
  creditsbanner()
  print()
  print()
  print(Fore.RED + "Menu coded by qolhf")
  time.sleep(1)
  print()
  print()
  print(Fore.RED + "Assistance by ACK and WhitePhantom")
  time.sleep(1)
  print()
  print()
  print(Fore.RED + "Credits go to rapidovh for giving me the idea of DorkDox")
  time.sleep(1)
  print()
  print()
  print(Fore.RED + "Any other credits go to Google and StackOverflow lol")
  print(Fore.WHITE)

if cmd == '7':
  print(Fore.GREEN + "We are sad to see you go, but come back?")
  print(Fore.WHITE)
  sys.exit()  