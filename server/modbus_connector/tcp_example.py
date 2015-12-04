from pymodbus.client.sync import ModbusTcpClient as ModbusClient

# import logging
# logging.basicConfig()
# log = logging.getLogger()
# log.setLevel(logging.DEBUG)
import pprint

# client = ModbusClient('143.233.186.1', port=502)
#client = ModbusClient(method='ascii', port='/dev/pts/2', timeout=1)
#client = ModbusClient(method='rtu', port='/dev/pts/2', timeout=1)
# client.connect()

# rr = client.read_holding_registers(0x0017,1,1)
# rr = client.read_holding_registers(17, 1)
# print rr
# print rr.function_code
# print rr.bits
# # pprint.pprint(rr.registers)
#
# client.close()

def check_register(regIndex):
    client = ModbusClient(host='143.233.186.1', port=502)
    client.connect()
    # result = client.read_holding_registers(regIndex, 1, unit=1)
    result = client.read_coils(52,1)
    print result
    pprint.pprint(result.registers)
    print hex(result.registers[0])
    client.close()

client = ModbusClient(host='143.233.186.1', port=502)
client.connect()

# Read All Values
# for i in range(93,96,1):
#
#     input_register = client.read_input_registers(i, 1, unit=1)
#     holding_register = client.read_holding_registers(i, 1, unit=1)
#
#     if input_register.function_code < 0x80:
#         print "Value on input_register:"
#         print i
#         print hex(i)
#         pprint.pprint(input_register.registers)
#         # break
#         print
#     if holding_register.function_code < 0x80:
#         print "Value on holding_register:"
#         print i
#         print hex(i)
#         pprint.pprint(holding_register.registers)
#         # break
#         print


write_holding_register = client.write_register(56, 1 , unit=1)
print write_holding_register


