# Docker

작업 환경설정과 관련된 것들은 신경쓰지않고 개발에만 집중할 수 있도록 해준다.
각 앱에 필요한 파일들을 독립된 컨테이너에 담아두기 때문에 한 서버에서 여러 서비스를 운영하는 것이 손쉽게 가능.
서버 확장 시에 컨테이너 자체를 가져와 서버를 증설하면되기 때문에 빠르고 효율적으로 서버관리 가능.

이미지를 만들고 -> 배포하고 -> 이미지를 받아 컨테이너를 구동한다

1.Dockerfile
앱 실행시키기 위해서 필요한 파일 명시
dependencies 명시
환경변수 설정
스크립트 설정

2.Image
작성한 Docker파일로 Image 생성가능
실행하려는 앱에 필요한 파일, dependencies, configuration등을 포함하고있다.
만들어진 image는 변경 불가능하다.

3.Container
위에서 만든 Image를 고립된 환경에서 실행할 수 있도록하는 환경
컨테이너안에서 앱이 실행된다
OOP로 비유하자면 Image는 Class, 각각의 Container는 Instance이다.

## 실행방법

깃과 유사
로컬환경에서 Image 만들고 -> Container Registry에 Push한다 -> 다른 개발자들은 내가 만든 Image를 Container Registry로 부터 Pull 하여 사용한다.
(실행 시 도커와 같은 컨테이너 엔진 설치 필요)

## 정리

1. 로컬에서 Dockerfile을 작성한 후 Build하여 Image를 생성한다
2. Container Registry에 Image를 Push한다.
3. 서버에서 Container Registry로부터 Image를 Pull로 받아온다.
4. 받아온 Image를 이용하여 컨테이너를 실행한다
