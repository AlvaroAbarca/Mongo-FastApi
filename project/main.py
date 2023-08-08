from fastapi import FastAPI, Body, Request, Header, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse
from db.motor import get_server_info

from pydantic import BaseModel
from typing import Dict, Optional

from datetime import datetime


# from db.models import Notification, Account
import asyncio
import os
import motor.motor_asyncio

# Nest Asyncio Fix
import nest_asyncio
nest_asyncio.apply()

# datetime.utcfromtimestamp(value).strftime('%Y-%m-%d %H:%M:%S')

app = FastAPI()


MONGO_URL = os.getenv("MONGO_URL", "mongodb://root:example@mongo:27017/")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL, serverSelectionTimeoutMS=5000)
db = client['test_database']


class RequestData(BaseModel):
    key: str | None = "default"
    resource: str | None = "default"
    data: dict | list[dict] | None = {}
    str_data: str | None = ""
    

@app.post("/api/test_data/", status_code=200)
async def meli_notifications(requestData: RequestData):
    """
        Task to recieve Notifications from Meli
    """

    # data = notification.dict() 
    # data['id_meli'] = data.pop('id')
    # notification_record = await NotificationRecord.create(**data)
    # data['notification_pk'] = notification_record.pk
    result = await db['test_collection'].insert_one(requestData.dict())
    return JSONResponse({
        'msg': 'Recibido.'
    })


"""
    websocket: WebSocket request: Request, 
    token = request.headers.get("Authorization", None)

    token = websocket.headers.get("Authorization", None)
    print(token)
    if token is None:
        return JSONResponse({
            "detail": "Token not found"
        }, 401)
    token = token.split(" ")[1] if "Bearer" in token else token
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return JSONResponse({
            "detail": "Token expired o expirado"
        }, 401)
    except jwt.InvalidSignatureError:
        return JSONResponse({
            "detail": "Token invalido o expirado"
        }, 401)

    for key, value in payload.items():
        if key in ['iat', 'exp']:
            payload[key] = datetime.utcfromtimestamp(value).strftime('%Y-%m-%d %H:%M:%S')

    
    await websocket.accept()
    try:
        data = await websocket.receive_text()
        await websocket.send_json(data, mode="binary")
    except WebSocketDisconnect:
        print("WebSocket Disconect")
        pass

    await websocket.accept()

    # return JSONResponse({
    #     'msg': 'Recibido.',
    #     'payload': payload,
    #     'notifications': notifications_list
    # })
"""