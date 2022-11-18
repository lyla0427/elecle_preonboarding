# elecle_preonboarding
django-celery pre-onboarding project for elecle

# Mission
- Django 에 Celery 를 연동해 간단한 비동기 Task 를 실행하는 서비스를 Docker 로 띄워보자.
- docker-compose up 커맨드로 서비스를 띄운 후, 브라우져에서 http://localhost:8088/hello 를 호출하면, 브라우져에선 Give me 3 seconds 텍스트를 출력하고, 그 상태로 10초를 더 기다리면 터미널상으로 Thank You 텍스트가 출력되어야 한다.

# 구조
![async](https://user-images.githubusercontent.com/72369222/202623778-41f045d1-27b1-4f72-85e9-20cb9b5bffbe.png)

# prerequisite
- language: python 3.8
- docker-compose

# 서비스 구동 방법
- ```docker-compose up```
- http://localhost:8088/hello 호출
- 브라우저에서 Give me 3 seconds 텍스트 출력되는 것 확인 
- 터미널에 Thank You 텍스트 출력 되는 것 확인
- 결과 화면:
<img width="837" alt="Screen Shot 2022-11-18 at 2 51 43 PM" src="https://user-images.githubusercontent.com/72369222/202630539-f566ec66-e3f0-4dd9-925b-2b3e35bd8e9c.png">

----
# 미션 수행 과정
**1. 장고 프로젝트 셋업**
  - pre_onboarding이라는 장고 프로젝트 생성
  - "Give me 3 seconds"라는 HttpResponse를 리턴하는 ```hello()``함수(fbv) 작성. /hello 엔드포인트와 연결.
**2. 장고에 celery 연동**
  - ```pip install celery```
  - settings에 celery 관련 환경 설정 추가. 여기에서는 모두 redis 엔드포인트! 
    - CELERY_BROKER_URL: 태스크를 수행할 메세지 브로커 
    - CELERY_RESULT_BACKEND: 태스크 결과를 저장할 데이터 베이스
  - pre_onboarding/task.py
    - celery 라이브러리의 인스턴스 정의. celery를 장고 프로젝트 내에서 사용할 수 있도록 해줌.
    - 수행할 task 정의. 실행하면 10 초 뒤 'Thank You'를 리턴하는 ```print_hello()```함수 정의.
  - pre_onboarding/__init__.py
    - celery 관련 모듈 인식하도록 설정. @shared_task 데코레이터가 사용할 앱을 자동으로 로드시키기 위함. 이 프로젝트에서는 @app.task 데코레이터를 사용하기 때문에 생략해도 됨!
  - pre_onboarding/views.py
    - ```hello()``함수에 ```print_hello.delay()``` 코드 추가. 
**3. dockerfile 작성**
  - python:3.8-slim-buster로 베이스 이미지 지정
  - PYTHONUNBUFFERED=1로 환경변수 설정. 파이썬 실행 결과에 대한 real-time 로그를 터미널로 볼 수 있게 함.
  - /django로 작업 디렉토리 지정
  - 호스트에 있는 파일을 docker 이미지의 파일 시스템으로 복사
  - 필요한 패키지 설치
**4. docker-compose.yml 작성**
  - docker-compose로 celery, django, redis 컨테이너 3개 함께 구동
  - django와 redis는 dockerfile 이미지 재사용하여 빌드
  
# 마주친 에러 
<details><summary>the module was not found</summary>


![Screen Shot 2022-11-14 at 7 13 48 PM](https://user-images.githubusercontent.com/72369222/202641725-e8e087c0-4e1e-4613-81dc-b0922ca5036e.png)

pre_onboarding 디렉토리를 못 찾는다는 뜻. 호스트에는 존재하지만 컨테이너에는 존재하지 않는 파일이기 때문에 못 찾는 것 같아 Dockerfile에 COPY . . 명령 추가
</details>

<details><summary>cannot connect to redis</summary>

![Screen Shot 2022-11-14 at 7 17 18 PM](https://user-images.githubusercontent.com/72369222/202641746-73018baa-2f0c-4c2e-8f13-92c312df192f.png)
각각의 컨테이너로 돌아가고 있는 redis 서버 ip에 연결을 해야 하는데 settings 파일에 로컬호스트로 설정이 되어 있어 안되는 상황. settings 파일에서 도메인 부분을 컨테이너 이름(redis_server)로 수정 
</details>



