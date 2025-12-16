import os
from databricks.sdk import WorkspaceClient

MODEL_NAME = os.environ["MODEL_NAME"]
MODEL_VERSION = os.environ["MODEL_VERSION"]

client = WorkspaceClient()

mv = client.model_versions.get(
    name=MODEL_NAME,
    version=MODEL_VERSION
)

artifact_uri = mv.storage_location
print(f"📦 Downloading model from: {artifact_uri}")

client.files.download(
    source_path=artifact_uri,
    destination_path="model",
    overwrite=True
)

print("✅ Model downloaded successfully")
