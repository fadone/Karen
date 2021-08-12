import time

from sonybraviaremote import TV, TVConfig


# called the very first time you attempt to connect to your
# tv... the tv will display a pincode that you need to enter
# after the first connection attempt, you'll never have to do this again
def on_auth():
    return input('Pincode: ')


# ip address of your tv... the device name is the name under which
# your program will be registered... note that if you change the device
# name, you have to re-auth
config = TVConfig('192.168.146.205', 'Karen')
tv = TV.connect(config, on_auth)

if tv.is_on():
    print("TV Connected!")
    print(tv.irc_codes())
    while True:
        choice = int(input("Enter Choice:\n"
                           "1. Next Channel\n"
                           "2. Previous Channel\n"
                           "3. Volume Up\n"
                           "4. Volume Down\n"
                           "0. Exit\n: "))
        if choice == 1:
            tv.next_channel()
        elif choice == 2:
            tv.previous_channel()
        elif choice == 3:
            tv.volume_up()
        elif choice == 4:
            tv.volume_down()
        elif choice == 0:
            break
        else:
            print("Wrong choice!")

else:
    print("TV Disconnected!")
# tv.is_on() # true/false
# tv.wake_up()
# tv.power_off()
# tv.netflix()
# tv.home()
# tv.enter()
# tv.confirm()
# tv.pause()
# tv.play()
# tv.confirm()
# tv.mute()
# tv.volume_up()
# tv.volume_down()
from bravia_tv import BraviaRC

ip_address = '192.168.146.205'

# IP address is required. The active NIC's mac will be acquired dynamically
# if mac is left None.
braviarc = BraviaRC(ip_address)

# The pin can be a pre-shared key (PSK) or you can
# receive a pin from the tv by making the pin 0000
pin = '5004'

# Connect to TV
braviarc.connect(pin, 'kbot', 'Karen')

if braviarc.is_connected():
    print("TV Connected!")
    tv._send_irc_code("Channel Up")
else:
    print("Not connected!")

# Hello, looking at this code I have managed to find a way to implement a channel change.
# ch = int (input ("Channel to change:"))
# for _ in range (0, len (str (ch))):
#     tv._send_irc_code ("Num" + str (ch) [_])
#     time.sleep ( 0.5)
# Remember to import the time library, using import time. I hope it has served you.
