import os
from databricks.sdk import WorkspaceClient

MODEL_NAME = os.environ["MODEL_NAME"]
MODEL_VERSION = os.environ["MODEL_VERSION"]

client = WorkspaceClient()

print(f"📦 Downloading model {MODEL_NAME} version {MODEL_VERSION}")

# ✅ CORRECT UC DOWNLOAD METHOD
client.model_versions.download(
    name=MODEL_NAME,
    version=MODEL_VERSION,
    dst_path="model"
)

print("✅ Model downloaded successfully to ./model")
