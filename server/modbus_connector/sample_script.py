__author__ = 'mpetyx'
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import pprint

COMport='/dev/tty.usbserial-ftE2BL20'
numRegisters=1
slaveUnit=1

def check_register(regIndex):
    client = ModbusClient(port=COMport,stopbits=1,bytesize=8,baudrate=9600, timeout=1, method='rtu')
    client.connect()
    result = client.read_holding_registers(regIndex, numRegisters, unit=slaveUnit)
    pprint.pprint(result.registers)
    print hex(result.registers[0])
    client.close()


def write_register(regIndex):
    client = ModbusClient(port=COMport,stopbits=1,bytesize=8,baudrate=9600, timeout=1, method='rtu')
    client.connect()
    client.write_coil(regIndex,0xff00)
    client.write_register(regIndex,0xff00)
    # client.write_register(regIndex,value=True)

    client.close()


# check_register(0x0004)
# for i in [49150,49151,49152,49153,49154,49155,49156,49157,49158,49159,49160]:
#     write_register(i)

write_register(0x3041)
write_register(12353)

# check_register(521)


# digital transform to binary
# analog transform to decimal
# input_table transform to hex to get result

# for index in range(0,1):
#     try:
#         check_register(0x0004)
#         # check_register(format(index,'#06x'))
#         print format(index,'#06X')
#     except:
#         continue