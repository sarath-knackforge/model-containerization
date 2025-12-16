import os
import mlflow

# REQUIRED for GitHub Actions + Unity Catalog
mlflow.set_tracking_uri("databricks")
mlflow.set_registry_uri("databricks-uc")

model_name = os.environ["MODEL_NAME"]
model_version = os.environ["MODEL_VERSION"]

model_uri = f"models:/{model_name}/{model_version}"

print(f"📦 Downloading model: {model_uri}")

local_path = mlflow.artifacts.download_artifacts(
    artifact_uri=model_uri
)

print(f"✅ Model downloaded to: {local_path}")
