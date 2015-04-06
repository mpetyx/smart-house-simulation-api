import minimalmodbus

instrument = minimalmodbus.Instrument('/dev/tty.usbserial-ftE2BL20', 1) # port name, slave address (in decimal)

## Read temperature (PV = ProcessValue) ##
temperature = instrument.read_register(6) # Registernumber, number of decimals
print temperature

## Change temperature setpoint (SP) ##
# NEW_TEMPERATURE = 95
# instrument.write_register(24, NEW_TEMPERATURE, 1) # Registernumber, value, number of decimals for storage