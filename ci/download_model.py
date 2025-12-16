import os
import mlflow
from mlflow.store.artifact.models_artifact_repo import ModelsArtifactRepository

# Ensure you have MLflow installed: pip install mlflow

MODEL_NAME = os.environ["MODEL_NAME"]
MODEL_VERSION = os.environ["MODEL_VERSION"]
LOCAL_PATH = "model"

# Set the MLflow tracking URI to "databricks" so it authenticates correctly
mlflow.set_tracking_uri("databricks")

print(f"📦 Downloading model {MODEL_NAME} version {MODEL_VERSION}")

# Define the MLflow model URI using the "models:/" scheme
model_uri = f"models:/{MODEL_NAME}/{MODEL_VERSION}"

# Create the destination directory if it doesn't exist
os.makedirs(LOCAL_PATH, exist_ok=True)

# Use the ModelsArtifactRepository to download the artifacts
# The "" as the first argument downloads the entire root of the model's artifacts
try:
    local_path = ModelsArtifactRepository(model_uri).download_artifacts("", dst_path=LOCAL_PATH)
    print(f"✅ Model downloaded successfully to {local_path}")
except Exception as e:
    print(f"❌ Error during download: {e}")

