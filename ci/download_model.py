import os
from databricks.sdk import WorkspaceClient

MODEL_NAME = os.environ["MODEL_NAME"]      # e.g. mlops_dev.model_test.model_deploy
MODEL_VERSION = os.environ["MODEL_VERSION"]  # e.g. 136

client = WorkspaceClient()

# ✅ CORRECT SDK CALL (positional args)
mv = client.model_versions.get(
    MODEL_NAME,
    MODEL_VERSION
)

artifact_uri = mv.storage_location
print(f"📦 Downloading model from: {artifact_uri}")

client.files.download(
    source_path=artifact_uri,
    destination_path="model",
    overwrite=True
)

print("✅ Model downloaded successfully")
