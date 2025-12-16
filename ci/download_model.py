import os
from databricks.sdk import WorkspaceClient
from databricks.sdk.service import ml

MODEL_NAME = os.environ["MODEL_NAME"]
MODEL_VERSION = os.environ["MODEL_VERSION"]

client = WorkspaceClient()

# 1️⃣ Get model version info from Unity Catalog
mv = client.model_versions.get(
    name=MODEL_NAME,
    version=MODEL_VERSION
)

# 2️⃣ Download model artifacts
# This is the UC artifact location
artifact_uri = mv.storage_location

print(f"📦 Downloading model artifacts from: {artifact_uri}")

client.files.download(
    source_path=artifact_uri,
    destination_path="model",
    overwrite=True
)

print("✅ Model downloaded successfully")
