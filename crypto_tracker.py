import urllib, json
import sys

from __builtin__ import raw_input
from termcolor import colored
import os
import glob
import webbrowser


def jumbo():
    print(colored("                                                      .::.", "cyan"))
    print(colored("                                                   .:'  .:", "cyan"))
    print(colored("                                         ,MMM8&&&.", "magenta") + colored(":'   .:'", "cyan"))
    print(colored("                                        MMMMM88&&&&", "magenta") + colored("  .:'", "cyan"))
    print(colored("                                       MMMMM88&&&&&&", "magenta") + colored(":'", "cyan"))
    print(colored("                                       MMMMM88&&&&&&", "magenta"))
    print(colored("                                     .:", "cyan") + colored("MMMMM88&&&&&&", "magenta"))
    print(colored("                                   .:'  ", "cyan") + colored("MMMMM88&&&&", "magenta"))
    print(colored("                                 .:'   .:", "cyan") + colored("'MMM8&&&'", "magenta"))
    print(colored("                                 :'  .:'", "cyan"))
    print(colored("                                 '::' ", "cyan"))
    print("")
    print(colored("__________.__                        __    _________                        __         .__    .___", "cyan"))
    print(colored("\______   \  | _____    ____   _____/  |_  \_   ___ \_______ ___.__._______/  |_  ____ |__| __| _/", "cyan"))
    print(colored(" |     ___/  | \__  \  /    \_/ __ \   __\ /    \  \/\_  __ <   |  |\____ \   __\/  _ \|  |/ __ | ", "cyan"))
    print(colored(" |    |   |  |__/ __ \|   |  \  ___/|  |   \     \____|  | \/\___  ||  |_> >  | (  <_> )  / /_/ | ", "magenta"))
    print(colored(" |____|   |____(____  /___|  /\___  >__|    \______  /|__|   / ____||   __/|__|  \____/|__\____ | ", "magenta"))
    print(colored("                    \/     \/     \/               \/        \/     |__|                       \/ ", "magenta"))


def nav():
    os.system("clear")
    jumbo()
    print("     ========================================================================================")
    print("     ====================    Welcome to Coinmarketcap.com rankings     ======================")
    print("     ========================================================================================")


def foot():
    print("     ========================================================================================")
    print("     ====================      Version 2.0.0 (Limit 3 Accounts)       =======================")
    print("     ========================================================================================")


def menu():
    nav()
    print("     ====================   1.) Check Rankings   2.) Add Wallet        ======================")
    print("     ====================   3.) Check Wallet     4.) Exit              ======================")
    print("     ====================   5.) Visit Planet Cryptoid                  ======================")
    foot()
    rank = raw_input(" ")
    menu_controller(rank)


def menu_controller(rank):
    if int(rank) == 1:
        check_ranks()
    elif int(rank) == 2:
        add_wallet()
    elif int(rank) == 3:
        ask_wallet()
    elif int(rank) == 4:
        os.system("clear")
        exit()
    elif int(rank) == 5:
        url = "https://www.planetcryptoid.tech"
        webbrowser.open_new(url)
    else:
        not_cool()


def not_cool():
    print("Not a valid option, try again?")
    raw_input("     ==================         Enter anything to return to menu         ====================")
    menu()


def wallet_controller(answer, wallet):
    if int(answer) == 1:
        check_wallet(wallet)
    elif int(answer) == 2:
        check_wallet(wallet)
    elif int(answer) == 3:
        check_wallet(wallet)
    else:
        not_cool()


def ask_wallet():
    nav()
    print("     ==================                Wallet's Available                ====================")
    wallets = glob.glob('wallets/*.json')
    empty = 0
    try:
        print("1.) " + dic2pretty(wallets[0]))
    except IndexError:
        empty += 1
    try:
        print("2.) " + dic2pretty(wallets[1]))
    except IndexError:
        empty += 1
    try:
        print("3.) " + dic2pretty(wallets[2]))
    except IndexError:
        empty += 1

    if empty == 3:
        print(" ")
        print("No wallets to display (Add a wallet from the Menu)")
        print(" ")
        raw_input("     ==================         Enter anything to return to menu         ====================")
        menu()
    else:
        answer = raw_input("     ======== Wallet Select: ")
        if int(answer) == 1:
            wallet_controller(answer, wallets[0])
        elif int(answer) == 2:
            wallet_controller(answer, wallets[1])
        elif int(answer) == 3:
            wallet_controller(answer, wallets[2])
        else:
            not_cool()


def dic2pretty(wallet):
    walleto = wallet[8:]
    walleto = walleto.split(".")[0]
#    walleto = walletz[:2]
#   This is a test commit
    return walleto


def check_wallet(wallet):
    file = wallet
    with open(file) as json_data:
        d = json.load(json_data)
        os.system("clear")
        wallet_stats(d, wallet)


def wallet_stats(d, wallet):
    jumbo()
    nav()
    print("     ====================                Wallet:  " + dic2pretty(wallet) + "             ======================")
    print("     ====================      =Rank= ===Name=== ==Price==  ==1h %==   ======================")
    data = calculate(str(d[0]['btc']), str(d[0]['eth']), str(d[0]['xrp']))
    btc_per = color(data[0]['btc_per'])
    eth_per = color(data[0]['eth_per'])
    xrp_per = color(data[0]['xrp_per'])
    print("     ====================         1    Bitcoin    $" + str(round(data[0]['btc_usd'], 2)) + "   " + btc_per)
    print("     ====================         2    Ethereum   $" + str(round(data[0]['eth_usd'], 2)) + "   " + eth_per)
    print("     ====================         3    Ripple     $" + str(round(data[0]['xrp_usd'], 2)) + "   " + xrp_per)
    total = data[0]['btc_usd'] + data[0]['eth_usd'] + data[0]['xrp_usd']
    print("     ----------------------------------------------------------------------------------------")
    print("     ====================                Total Value: $" + str(round(total, 2)) + "         ======================")
    print(" ")
    raw_input("     ==================         Enter anything to return to menu         ===================")
    menu()


def add_wallet():
    nav()
    print("     ====================       Add Wallet Alpha(limited 3 coins)      ======================")
    print("     ====================         Enter a Name for your Wallet         ======================")
    name = raw_input("Wallet Name: ")
    btc = raw_input("Bitcoin Value : ")
    eth = raw_input("Ethereum Value : ")
    xrp = raw_input("Ripple Value : ")
    file = "wallets/" + name + ".json"
    print(name)
    data = [{"name": name, "btc": btc, "eth": eth, "xrp": xrp}]
    with open(file, 'w') as outfile:
        json.dump(data, outfile)
    print("     ==================                  Wallet Created                  ====================")
    raw_input("     ==================         Enter anything to return to menu         ====================")
    menu()


def check_ranks():
    nav()
    print("     ================== How many Crypto's would you like listed?(1-879) ====================")
    ranks = raw_input(" ")
    url = "https://api.coinmarketcap.com/v1/ticker/?limit=" + str(ranks)
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    i = 0
    rank = 1
    while i < int(ranks):
        percent = float(data[i]['percent_change_1h'])
        rankString = str(rank) + "). "
        print(rankString + data[i]['name'] + " | " + data[i]['price_usd'] + " | " + color(percent))
        rank += 1
        i += 1

    btc_price = str(data[0]['price_usd'])

    raw_input("     ==================         Enter anything to return to menu         ====================")
    menu()


def calculate(btc, eth, xrp):
    url = "https://api.coinmarketcap.com/v1/ticker/?limit=3"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    btc_usd = float(btc) * float(data[0]["price_usd"])
    eth_usd = float(eth) * float(data[1]["price_usd"])
    xrp_usd = float(xrp) * float(data[2]["price_usd"])
    rankz = [{"btc_usd": btc_usd, "eth_usd": eth_usd, "xrp_usd": xrp_usd,
              "btc_per": data[0]['percent_change_1h'], "eth_per": data[1]['percent_change_1h'],
              "xrp_per": data[2]['percent_change_1h']}]
    return rankz


def color(percent):
    if percent > 0:
        percent_data = colored(str(percent) + "%", "green")
    else:
        percent_data = colored(str(percent) + "%", "red")
    return percent_data


def save_wallet(data, filename):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)


def main(argv):
    menu()


if __name__ == "__main__":
    main(sys.argv)

