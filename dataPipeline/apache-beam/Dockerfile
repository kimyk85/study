FROM apache/beam_python3.10_sdk:2.47.0

COPY ./apache-beam/pubsubprint.py /tmp/pubsubprint.py
COPY ./key/google-service-key.json /tmp/google-service-key.json # 구글 클라우드의 IAM에서 발급받은 json 키 지정
ENTRYPOINT ["python","tmp/pubsubprint.py" ] # 컨테이너가 바로 종료되는 것을 방지하기 위해 파이썬 파일을 실행. 해당 파이썬 파일은 pubsub 메세지를 계속 대기하기 때문에 종료되지 않고 계속 동작