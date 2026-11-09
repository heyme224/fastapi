#hello/main/py

import socket

from fastapi import FastAPI
# fastapi  객체 생성
app = FastAPI()

# GET 방식 최상위 경로 요청에 대해서 응답을 처리하는 비동기 함수

@app.get("/")
async def root():
    #dict 나 list type을 리턴해주면 해당 객체에 담긴 정보를 json형식의 문자열로 변환해서 fastapi가 응답함
    return {"message":"Hello from fastapi"}

@app.get("/health")
async def health():
    #dict 나 list type을 리턴해주면 해당 객체에 담긴 정보를 json형식의 문자열로 변환해서 fastapi가 응답함
    return {"status":"ok"}
@app.get("/whoareyou")
async def who():
    socket.gethostname
    