import netifaces

for card in netifaces.interfaces():
    print(card)
    try:
        # get all NIC addresses
        temp = netifaces.ifaddresses(\
                card)[netifaces.AF_INET][0]['addr']
        print(temp)
        temp = netifaces.ifaddresses(card)
        print(temp)
    except BaseException:
        pass            

