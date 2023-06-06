# 구성도
 - Nginx 컨테이너의 docker logging로 fluentd 로그 전송
 - fluentd에서 Nginx의 Access Log만 필터하여 pubsub으로 전송하고 stdout 출력
 - pubsub에 수집된 로그를 apache-beam 코드로 가져와서 출력

# 구글 클라우드 설정
 - 구글 클라우드에서 pubsub 주제와 구독을 1개 생성
 - IAM에서 서비스 계정을 만들고 "게시/구독 편집자" 권한 부여

# 파일 내 설정값 변경
 - apache-beam/Docker 파일 내에 IAM에서 생성한 구글 서비스 키 지정
 - apache-beam/pubsubprint.py 파일 내에 토픽 경로와 컨테이너 내부의 구글 서비스 키 경로 지정
 - fluent/fluent.conf 파일 내의 match 디렉티브 내에 project에 구글 프로젝트 명, topic에 토픽명, key에 구글 서비스 키 컨테이너 경로 지정
 - docker-compose.yml 파일 내의 fluent에서 volume에 구글 서비스 키 지정

# docker-compose로 컨테이너 실행
 - cmd 창에서 docker-compose.yml 파일이 있는 폴더로 이동하여 ```docker-compose up -d``` 실행
 - 만약에 도커로 생성된 적이 있다면 아래 명령어로 중지와 삭제
   - ```docker-compose stop```
   - ```docker-compose rm```
 - yml 파일 수정 후 재생성 명령어: ```docker-compose up --build --force-recreate -d```

# Nginx 페이지 접속
 - 방법 1. 브라우저에서 localhost 접속
 - 방법 2. cmd 창에서 curl localhost 해서 코드 리턴

# Fluentd 로 처리된 nginx 접속 로그 확인
 - 도커 로그로 Fluentd로 유입된 데이터 확인. fleunt를 통해 pubsub으로 전송되는 로그를 stdout으로도 출력
   - ```docker logs -f c_fluent```

# pubsub에서 apache-beam으로 수집된 로그 확인
 - 도커 로그로 Fluentd 컨테이너와 동일한 로그가 출력되는지 확인
   - ```docker logs -f c_dataprocessing```
 