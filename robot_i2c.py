from smbus import SMBus

addr = 0x8 # bus address
bus = SMBus(1) # indicates /dev/ic2-1


def send_i2c_message(data):
    try:
        bus.write_byte(addr, data)
        print("sent")
    except Exception as e:
        print(e)
        print("Error!!, unable to send")
