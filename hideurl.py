import os
import colorama
from colorama import Fore, Style
import pyfiglet
from pyfiglet import figlet_format
import time
import urllib.request




#banner
os.system("clear")
banner = figlet_format('hideurl', font='starwars')
print(Fore.RED + banner)
print(Style.RESET_ALL)
print("Made By t0a5ted                                          version 1.0" + "\n\n\n")

#collect user input for url
def askforurl():
	global url
	website_is_up = ""
	longurl = input(Fore.BLUE + "Enter URL to Hide: ")
	print(Style.RESET_ALL)
	try:
		global status_code
		status_code = urllib.request.urlopen(longurl).getcode()
	except:
		print(Fore.RED + "\nURL Does Not Exist or Website Not Online\n")
		askforurl()

	else:
		website_is_up = status_code == 200



	
	
	if any(i in longurl for i in ('https://', 'http://', ' ')) == False or website_is_up == "False":
		print(Fore.RED + "\nNot a Valid URL (Add \"https://\" or \"http://\" if you haven't) OR URL Host Not Online\n\n")
		print(Style.RESET_ALL)
		askforurl()
	else:
		print(Fore.GREEN + "\nValid URL!")
		print(Style.RESET_ALL)
		global url
		url = longurl 


#collect user input of keywords
def askforaddons():
	addons = input(Fore.BLUE + "Enter Key Words (Seperate Key Words with \"-\"): ")
	print(Style.RESET_ALL)
	total = 0
	for i in addons:
		total = total + 1

	if total < 11:
		if any(i in addons for i in (' ')) == True:
			print(Fore.RED + "\nDo Not Use Spaces To Connect Key Words...Use \"-\" instead\n\n")
			print(Style.RESET_ALL)
			askforaddons()
		else:
			print(Fore.GREEN + "\nValid Key Words!")
			print(Style.RESET_ALL)
			global keywords
			keywords = addons
			shortenurl()

	else:
		print("\nMaximum 10 Characters Allowed (including dashes)\n")
		askforaddons()
#url shortener if user wants key words
def shortenurl():
	global url
	global keywords
	print(Fore.GREEN + "\n\n-----------SUCCESSFUL-----------")
	print(Style.RESET_ALL)
	newurl = os.popen('curl \"da.gd/s/?url=' + url + "&shorturl=" + keywords + "\"").read()
	print("\nNew Hidden URL: " + newurl)
	

#ask if user wants to add key words
def keywordsornah():
	askforkeywords = input("Do you want to add Key Words? (y/n): ")
	if askforkeywords == "y":
		askforaddons()
	elif askforkeywords == "n":
		shortenurl2()
	else:
		print(Fore.RED + "\n\nType \"y\" for yes and \"n\" for no....its not that hard")
		print(Style.RESET_ALL)
		keywordsornah()


#url shortener if user does not want key words
def shortenurl2():
	print(Fore.GREEN + "\n\n-----------SUCCESSFUL-----------")
	print(Style.RESET_ALL)
	result = os.popen('curl da.gd/s/?url=' + url).read()
	print("\nNew Hidden URL: " + result)





askforurl()

keywordsornah()









