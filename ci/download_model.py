import os
import mlflow

# CI ONLY
mlflow.set_registry_uri("databricks-uc")

model_name = os.environ["MODEL_NAME"]
model_version = os.environ["MODEL_VERSION"]

model_uri = f"models:/{model_name}/{model_version}"

print(f"📦 Downloading model from {model_uri}")

mlflow.artifacts.download_artifacts(
    artifact_uri=model_uri,
    dst_path="model"
)

print("✅ Model downloaded successfully")
