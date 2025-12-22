import os
import mlflow

# 1. Force use of Unity Catalog and Databricks
mlflow.set_tracking_uri("databricks")
mlflow.set_registry_uri("databricks-uc")

# 2. Extract env vars
MODEL_NAME = os.environ.get("MODEL_NAME")
MODEL_VERSION = os.environ.get("MODEL_VERSION")
LOCAL_PATH = "model"

print(f"📦 Downloading model {MODEL_NAME} version {MODEL_VERSION}")

# 3. Use the standardized models:/ URI
model_uri = f"models:/{MODEL_NAME}/{MODEL_VERSION}"

os.makedirs(LOCAL_PATH, exist_ok=True)

try:
    # download_artifacts is the most stable way to pull from UC
    local_path = mlflow.artifacts.download_artifacts(artifact_uri=model_uri, dst_path=LOCAL_PATH)
    print(f"✅ Model downloaded successfully to {local_path}")
except Exception as e:
    print(f"❌ Error during download: {e}")
    # Force the script to fail so the GitHub Action stops
    exit(1)