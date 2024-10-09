import asyncio
import pymodbus.client as ModbusClient
from pymodbus.exceptions import ModbusException
# Connect to the server
client = ModbusClient.AsyncModbusTcpClient('192.168.1.121', port=5020)  
async def run_async_TCP_client():
    
    await client.connect()
    await client.write_coil(1, True, slave=1)
    try: 
        rr = await client.write_coil(1, True, slave = 1)
    except ModbusException as exc:
        client.close()
        return




asyncio.run(run_async_TCP_client())
