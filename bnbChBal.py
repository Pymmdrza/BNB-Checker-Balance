# Programmer MMDRZA 
# Website : Mmdrza.Com 
# Email : x4@Mmdrza.Com
#
# Donate ========================================= 
# BTC ADDRESS : 16p9y6EstGYcnofGNvUJMEGKiAWhAr1uR8
# USDT(TRC20) : TSb4w985WJ2zdDtTvex6jjFLejqZHGK5ez
# ================================================
import time
import random
import requests
import datetime
from colorama import Fore, Style

count = 1
addcc = str(input('|||||||[  INSERT TARGET WALLET FOR CHECKiNG  > '))
stpcc = str(input('|||||||[     SLEEP TIME BETWEEN EACH REVIEW  > '))
            print('|||||||[BinanceSmartChain Wallet Checker Balance\n====================||[ M M D R Z A . C o M ]||====================\n')

while True:
    tc = datetime.datetime.now()
    bnbadd = str(addcc)
    # Start Details API KEY Bscscan ======================================        
    apibnb1 = "&apikey=[INSERT YOUR API ON BscScan.io]" # Your BscScan API
    apibnb2 = "&apikey=[INSERT YOUR API ON BscScan.io]" # Your BscScan API
    apibnb3 = "&apikey=[INSERT YOUR API ON BscScan.io]" # Your BscScan API
    apibnb4 = "&apikey=[INSERT YOUR API ON BscScan.io]" # Your BscScan API
    apibnb5 = "&apikey=[INSERT YOUR API ON BscScan.io]" # Your BscScan API
    apibnb6 = "&apikey=[INSERT YOUR API ON BscScan.io]" # Your BscScan API
    # Start Details API KEY Bscscan ======================================        
    mylist1 = [str(apibnb1), str(apibnb2), str(apibnb3), str(apibnb4), str(apibnb5), str(apibnb6)]  # 6 API KEYS
    apikeysbnb = random.choice(mylist1)
    blocs1 = requests.get("https://api.bscscan.com/api?module=account&action=balance&address=" + bnbadd + apikeysbnb)
    ress1 = blocs1.json()
    balancebnb = dict(ress1)["result"]
    print(Fore.WHITE,str(count),Fore.GREEN,'Address =',Fore.WHITE, str(bnbadd),Fore.RED, ' Balance =',Fore.YELLOW, str(balancebnb),Fore.BLUE,' LastCheck',Fore.GREEN,str(tc),Style.RESET_ALL)
    count += 1
    time.sleep(float(stpcc))
    if int(balancebnb) > 0:
        count += 100
        print(str(count),'Balance  = ', str(balancebnb))
        print('ADDRESS  = ', bnbadd)
        print('Balance  = ', str(balancebnb))
        print('================================================')
        print('================================================')
        print('================================================')
        print('Found Found Found Found Found Found Found Found Found Found Found Found ')
        print('BNB Address           :  ', bnbadd)
        print('Balance  = ', str(balancebnb))
        print('Found Found Found Found Found Found Found Found Found Found Found Found ')
        print('================================================')
        print('================================================')
        print('================================================')
        if count == 1000000:
            print(str(count),'BALANCE =',str(balancebnb))
        break
        
        # Programmer MMDRZA 
        # Website : Mmdrza.Com 
        # Email : x4@Mmdrza.Com
        #
        # Donate ========================================= 
        # BTC ADDRESS : 16p9y6EstGYcnofGNvUJMEGKiAWhAr1uR8
        # USDT(TRC20) : TSb4w985WJ2zdDtTvex6jjFLejqZHGK5ez

