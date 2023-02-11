from google.api_core.exceptions import AlreadyExists, InvalidArgument
from google.cloud.pubsub import PublisherClient, SchemaServiceClient
from google.pubsub_v1.types import Encoding

# TODO(developer): Replace these variables before running the sample.
# project_id = "your-project-id"
# topic_id = "your-topic-id"
# schema_id = "your-schema-id"
# Choose either BINARY or JSON as valid message encoding in this topic.
# message_encoding = "BINARY"

publisher_client = PublisherClient()
topic_path = publisher_client.topic_path(project_id, topic_id)

schema_client = SchemaServiceClient()
schema_path = schema_client.schema_path(project_id, schema_id)

if message_encoding == "BINARY":
    encoding = Encoding.BINARY
elif message_encoding == "JSON":
    encoding = Encoding.JSON
else:
    encoding = Encoding.ENCODING_UNSPECIFIED

try:
    response = publisher_client.create_topic(
        request={
            "name": topic_path,
            "schema_settings": {"schema": schema_path, "encoding": encoding},
        }
    )
    print(f"Created a topic:\n{response}")

except AlreadyExists:
    print(f"{topic_id} already exists.")
except InvalidArgument:
    print("Please choose either BINARY or JSON as a valid message encoding type.")
