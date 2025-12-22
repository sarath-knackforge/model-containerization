import os
import mlflow

# Force MLflow to use Unity Catalog for the model registry
mlflow.set_registry_uri("databricks-uc")
mlflow.set_tracking_uri("databricks")

MODEL_NAME = os.environ["MODEL_NAME"]
MODEL_VERSION = os.environ["MODEL_VERSION"]
LOCAL_PATH = "model"

print(f"📦 Downloading model {MODEL_NAME} version {MODEL_VERSION}")

# Define the MLflow model URI
model_uri = f"models:/{MODEL_NAME}/{MODEL_VERSION}"

os.makedirs(LOCAL_PATH, exist_ok=True)

try:
    # Use the higher-level mlflow.artifacts API which is more robust
    local_path = mlflow.artifacts.download_artifacts(artifact_uri=model_uri, dst_path=LOCAL_PATH)
    print(f"✅ Model downloaded successfully to {local_path}")
except Exception as e:
    print(f"❌ Error during download: {e}")
    # Re-raise the error so the GitHub Action fails if the download fails
    raise e