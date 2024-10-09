import pymodbus.client as ModbusClient  
from pymodbus import (
    ExceptionResponse,
    ModbusException,
    pymodbus_apply_logging_config,
) 
import time 
import asyncio

#baudrate = 9600 #wybrany z palca
#port = 5020

        
async def run_async_simple_client():
    client = ModbusClient.AsyncModbusSerialClient(
        port = "dev/tty",
        baudrate = 9600,
        bytesize = 8,
        parity = "N",
        stopbits = 1
    )

    #start the client
    print("connect to server")
    await client.connect()
    #test if the client has been connnected 
    assert client.connected 


    try:
        rr = await client.read_holding_registers(1)
        print(rr)
        time.sleep(1)
    except ModbusException as exc:
        print(f"Recieved exception {exc}")
        client.close()
        return
asyncio.run(run_async_simple_client())
