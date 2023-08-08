import os

import motor.motor_asyncio

MONGO_URL = os.getenv("MONGO_URL", "mongodb://root:example@mongo:27017/")
async def get_server_info():
    # replace this with your MongoDB connection string
    conn_str = MONGO_URL
    # set a 5-second connection timeout
    client = motor.motor_asyncio.AsyncIOMotorClient(conn_str, serverSelectionTimeoutMS=5000)
    try:
        print(await client.server_info())
    except Exception:
        print("Unable to connect to the server.")

    return client
        
