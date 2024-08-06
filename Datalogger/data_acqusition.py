from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import time

# Configure according to the NMID300-1 NMID300-2 LUMEL NR30IoT and SENECA T20PM100-MU meters
# This code attepmts to be compatible with NMID30-1 and read a sample voltage 

port = '/dev/ttyUSB0'  # Replace with desired port
baudrate = 9600
bytesize = 8
parity = 'N'
stopbits = 1
timeout = 1

# Create a Modbus client object
client = ModbusClient(
    method='rtu',
    port=port,
    baudrate=baudrate,
    bytesize=bytesize,
    parity=parity,
    stopbits=stopbits,
    timeout=timeout
)


client.connect()

try:
    while True:
        # Define the Modbus register address to read from
        register_address = 1  # Replace with the actual register address

        # Read the holding register value from the device
        response = client.read_holding_registers(register_address, 1, unit=1)

        # Check if the request was successful
        if not response.isError():
            # Extract the voltage value from the response
            voltage = response.registers[0] / 10  # Assuming the voltage is stored as an integer with one decimal place

            # Print the voltage value
            print("Voltage: ", voltage, "V")
        else:
            print("Error reading Modbus register:", response)

        # Wait for a specified time interval
        time.sleep(1)

except KeyboardInterrupt:
    # Close the Modbus connection on keyboard interrupt
    client.close()
