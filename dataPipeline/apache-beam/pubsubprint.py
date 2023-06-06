import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import os

TOPIC_PATH = "projects/google-project/topics/topic-name"  # 구글 클라우드의 Pubsub 토픽 이름

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/tmp/google-service-key.json"  # 컨테이너 내 구글 json 키 경로

import logging

logging.basicConfig(level=logging.INFO)
logging.getLogger().setLevel(logging.INFO)


class read_from_pubsub(beam.DoFn):
    def process(self, element):
        print(element)
        logging.info(element)
        return [element]
def run():
    pipeline_options = PipelineOptions()
    options = pipeline_options.view_as(beam.options.pipeline_options.StandardOptions)
    options.streaming = True
    p = beam.Pipeline(options=pipeline_options)

    data = p | beam.io.ReadFromPubSub(topic=TOPIC_PATH) | beam.ParDo(read_from_pubsub())
    result = p.run()
    result.wait_until_finish()


if __name__ == '__main__':
    run()
