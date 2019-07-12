## 개요
GET / 로 접근시 Hello World! 를 출력하는 서버를 만들고 GitHub master 브랜치에 push 하면 자동으로 Jenkins를 통해 빌드 후 배포 되도록 구축한다.

## 제출물
1. 서버에 Unit Test 작성
2. Docker 컨테이너로 빌드, 배포
3. 브라우저로 접속시 Hello World가 표시되는 Url
4. 접속 가능한 Jenkins 서버 Url과 ID / Password
5. GitHub과 Jenkins를 연동하고 커밋 푸시되면 서버가 자동으로 업데이트 되도록 만들 것
6. 빌드 과정 및 결과에 대한 로그를 GitHub에서 확인할 수 있어야 함
7. CI/CD 파이프라인에서 Unit Test 있어야 함

## Docker image(recommend)
- [Jenkins Blueocean](https://hub.docker.com/r/jenkinsci/blueocean)

## 예시
![GitHub Jenkins Integration](/screenshots/s2.png?raw=true)
![Jenkins Pipeline](/screenshots/s3.png?raw=true)

## 제출 기한
하루