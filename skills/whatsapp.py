import re
from os.path import basename
# import pywhatkit as kt

name = basename(__file__[:-3])
enable = True
command = [
    [name, "send_whatsapp_message", ["send"]],

]


def send_whatsapp_message(text):
    m = re.search('send (.+?)to(.+?)', text)
    if m:
        msg = m.group(1)
        to = text.split("to ")[1]
        kt.sendwhatmsg_instantly("+923088806636", msg)
    else:
        return "Wrong format!"
    return "Sending whatsapp message!"
