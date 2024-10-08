import pymodbus.client as ModbusClient  
from pymodbus import (
    ExceptionResponse,
    ModbusException,
    pymodbus_apply_logging_config,
) 
import time 
import asyncio

baudrate = 9600 #wybrany z palca
port = 5020

        
async def run_async_simple_client(port ):
    client = ModbusClient.AsyncModbusSerialClient(
        port,
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
    print("connection established, reading data")


    try:
        await client.read_holding_registers()
    except ModbusException as exc:
        print(f"Recieved exception {exc}")
        client.close()
        return
