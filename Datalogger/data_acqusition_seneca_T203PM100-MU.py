import time
from pymodbus.client.sync import ModbusSerialClient as ModbusClient

client = ModbusClient(
    method='rtu',
    port='',  #do zadecydowania z faktycznym miernikiem i raspberry 
    baudrate=9600,        
    parity='N',           
    stopbits=1,
    bytesize=8,
    timeout=1
)

client.connect()

def read_voltage():
    try:
        response = client.read_holding_registers(40099, 1, unit=1) #czytamy z miernika nr 1 stad unit=1 

        if not response.isError():
            voltage = response.registers[0]


            print(f"Voltage: {voltage} V")
        else:
            print("Failed to read from register")
    except Exception as e:
        print(f"Error: {e}")

# Main loop to read voltage periodically
try:
    while True:
        read_voltage()
        time.sleep(1)  # Read every 5 seconds (adjust as needed)
except KeyboardInterrupt:
    print("Exiting program...")
finally:
    # Close the Modbus client connection
    client.close()

