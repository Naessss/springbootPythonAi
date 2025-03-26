# springbootPythonAi

### 개발환경
python 3.11
IDE : pycharm
### FastApi
- pip install fastapi uvicorn uvicorn
- FastAPI는 ASGI 표준을 따르는 웹 프레임워크임
FastAPI 애플리케이션은 비동기 처리를 기본으로 하며, Uvicorn과 같은 ASGI서버를 사용하여 높은 성능을 제공
- ASGI(Asynchronus Server Gateway Interface)는 파이썬에서 비동기 웹서버와 웹 어플리케이션 간의 인터페이스 표준
기존 WSGI(Web Server Gateway Interface)의 비동기 버전으로 파이썬에서 비동기 처리를 지원하는 웹 어플리케이션을 구축
### ASGI 특징
- 비동기 지원 : ASGI는 비동기 코드 실행을 지원하며 높은 성능과 동시성을 제공
웹소켓이나 서버 푸시와 같은 비동기 통신이 필요한 애플리케이션에 유용
- 범용성 : HTTP뿐만 아니라 WebSocket, gRPC와 같은 프로토콜을 지원
- 유연성 : ASGI 애플리케이션은 다양한 서버 및 프레임워크와 호환되며, 모듈식으로 구성

### FastAPI 서버 실행
main.py 실행 Terminal에서 uvicorn main:app --reload -- port 8001

![image](https://github.com/user-attachments/assets/79d6c960-0367-44c4-a1e6-eae65e52b903)
