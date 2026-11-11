# test01_jinja2/main.py

# fastapi 객체 생성
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# 템플릿 파일들이 위치하는 디렉토리 정보를 전달하면서 Jinja2Templates 객체를 생성한다.
templates = Jinja2Templates(directory="templates")

# response_class=HTMLResponse 옵션은 html 형식의 문자열을 응답하겠다는 의미
@app.get("/", response_class=HTMLResponse)
def index(req: Request): # Request type 객체가 매개변수에 전달된다.
    noticeList = ["교재가 오늘 도착했습니다","어쩌구","저쩌구"]


    result = templates.TemplateResponse(
        request=req, 
        name= "index.html",
        context={
            "fortuneToday" : "happy 하게 대박이나서 소원이 성취됨으로 웃음이 나요",
            "noticeList" : noticeList
        }
    )
    return result

#Get 방식 "/members" 요청에 대한 응답
@app.get("/members", response_class=HTMLResponse)
def members(req:Request):
    list=[
          {"num":1,"name":"김구라", "addr":"노량진"},
          {"num":2,"name":"해골","addr":"행신동"},
          {"num":2,"name":"원숭이","addr":"동물원"}
        ]
    return templates.TemplateResponse(
        request=req,
        name="members.html",
        context={"list":list}

    )
    