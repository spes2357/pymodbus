from pymodbus.client import ModbusSerialClient
client = ModbusSerialClient("/dev/ttyUSB0")

client.connect()

response = client.read_holding_registers(address = 0,count = 16, slave =1)
print(response.registers)
client.close()

