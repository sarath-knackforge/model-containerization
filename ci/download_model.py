import os
import mlflow

# --------------------------------------------------
# CI ONLY: enable Databricks + Unity Catalog access
# --------------------------------------------------
mlflow.set_tracking_uri("databricks")
mlflow.set_registry_uri("databricks-uc")

# Values passed from GitHub Actions
model_name = os.environ["MODEL_NAME"]
model_version = os.environ["MODEL_VERSION"]

# Unity Catalog model URI
model_uri = f"models:/{model_name}/{model_version}"

# Local directory where model will be downloaded
local_dir = "model"

print(f"📦 Downloading model from {model_uri}")

mlflow.artifacts.download_artifacts(
    artifact_uri=model_uri,
    dst_path=local_dir
)

print(f"✅ Model downloaded locally to ./{local_dir}")
