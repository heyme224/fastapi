from fastapi import Depends, FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
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
@app.get("/member/new",response_class=HTMLResponse)
def memberNewForm(req:Request):
    return templates.TemplateResponse(
        request=req,
        name="member/new.html"
    )

@app.post("/member/new",response_class=HTMLResponse)
def memberNew(req:Request,name:str=Form(...),addr:str=Form(...),db:Session=Depends(get_db)):
    query =text("""
        INSERT INTO member
        (name,addr)
        VALUES(:name, :addr)
""")
    db.execute(query,{"name":name,"addr":addr})
    db.commit()
    return templates.TemplateResponse(
        request=req,
        name="member/alert.html",
        context={
            "msg":f"{name}님의 정보를 저장했습니다",
            "url":"/member"
        }
    )
@app.get("/member/delete/{num}")
def deleteMember(num:int,db:Session =Depends(get_db)):
    query=text("""
        DELETE FROM member
        WHERE num=:num

""")
    db.execute(query,{"num":num})
    db.commit()
    return RedirectResponse("/member",status_code=302)

@app.get("/member/edit/{num}")
def editMember(req:Request,num:int,db:Session=Depends(get_db)):
     query=text("""
            SELECT num, name, addr
            FROM member
            WHERE num=:num    
    """)
     row=db.execute(query,{"num":num}).fetchone()

     return templates.TemplateResponse(
         request=req,
         name="member/edit.html",
         context={
             "row":row
         }
     )
@app.post("/member/update", response_class=HTMLResponse)
def updateMember(
    req: Request,
    num: int = Form(...),
    name: str = Form(...),
    addr: str = Form(...),
    db: Session = Depends(get_db)
):
    # DB에서 특정 번호(num)의 회원 정보를 수정(UPDATE)하는 SQL
    query = text("""
        UPDATE member 
        SET name = :name, addr = :addr 
        WHERE num = :num
    """)
    db.execute(query, {"name": name, "addr": addr, "num": num})
    db.commit()  # 수정 확정

    # 수정이 끝나면 회원 목록 페이지로 자동 이동
    return RedirectResponse("/member", status_code=302)