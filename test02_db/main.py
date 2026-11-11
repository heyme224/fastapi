from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from database import get_db
from sqlalchemy import text
from sqlalchemy.orm import Session

app = FastAPI()

templates = Jinja2Templates(directory="templates")

#result= get_db #함수

@app.get("/", response_class=HTMLResponse)
def index(req: Request):
    return templates.TemplateResponse(
        request=req,
        name="index.html",
        context={
            "noticeList":["오후 일정이 시작되었습니다", "제제이야", "GAE GAE EIYA"]
        }
    )

@app.get("/member",response_class=HTMLResponse) 
def getMembers(req:Request,db : Session=Depends(get_db)):
    query= text("""
        SELECT num,name,addr
        FROM member
        ORDER BY num ASC
    """)
    result = db.execute(query)
    #회원목록이 들어있는 list type이라고 생각하면 됨
    members=result.fetchall()

    return templates.TemplateResponse(
        request=req,
        name="member/list.html",
        context={
            "members":members
        }
    )
    