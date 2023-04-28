# docker-compose로 컨테이너 실행
 - cmd 창에서 docker-compose.yml 파일이 있는 폴더로 이동하여 ```docker-compose up -d``` 실행
 - 만약에 도커로 생성된 적이 있다면 아래 명령어로 중지와 삭제
   - ```docker-compose stop```
   - ```docker-compose rm```

# Nginx 테스트
 - 방법 1. 브라우저에서 localhost 접속
 - 방법 2. cmd 창에서 curl localhost 해서 코드 리턴

# Fluentd 테스트
 - 리눅스 환경이나 WSL 접근하여 명령어 실행
   - ```curl -X POST -d 'json={"json":"message"}' http://127.0.0.1:9880/sample.test```
 - 도커 로그로 Fluentd로 유입된 데이터 확인
   - ```docker logs -f dataPipeline_fluentd```
 