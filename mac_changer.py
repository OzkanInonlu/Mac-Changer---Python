import subprocess as sb
import optparse as opt
import time

def get_inputs():
    p_object = opt.OptionParser()
    p_object.add_option("-i", "--int", dest="interface")
    p_object.add_option("-m", "--m", dest="mac_address")
    return p_object.parse_args()


def change_mac(interface, mac_address):
    sb.call(["ifconfig", interface, "down"])
    sb.call(["ifconfig", interface, "hw", "ether", mac_address])
    sb.call(["ifconfig", interface, "up"])
    time.sleep(2)
    print("Success")
    time.sleep(2)
    sb.call(["ifconfig", interface])


(user_inputs, arg) = get_inputs()
interface=user_inputs.interface
mac_address=user_inputs.mac_address
change_mac(interface,mac_address)
