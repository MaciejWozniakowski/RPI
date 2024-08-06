from pymodbus.client.sync import ModbusTcpClient

# Connect to the server
client = ModbusTcpClient('192.168.1.100', port=5020)  # Replace with your server IP
client.connect()

# Read Holding Registers (example)
result = client.read_holding_registers(0, 10, unit=1) 
print(result.registers)

# Write to a Holding Register (example)
client.write_register(1, 25, unit=1)  

# Close the connection
client.close() 
