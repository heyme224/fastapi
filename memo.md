#fastapi 를 사용해보자

##환경 구성

```bash
#python 가상환경 만들기
python -m venv venv

#가상환경 활성화
.\venv\Scripts\activate

#필요한 패키지 설치
pip install fastapi uvicorn

#app 시작하기 (main.py 파일 안에 있는 app 객체를 참조)
uvicorn main:app --reload
```

```bash
#현재 환경을 requirements.txt 파일에 기록하기(의존성 기록하기)
pip freeze > requirements.txt

#requirements.txt 파일을 이용해서 의존성을 다른 곳에서 설치하는 방법
pip install -r requirements.txt
```