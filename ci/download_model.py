import os
import mlflow

MODEL_NAME = os.environ["MODEL_NAME"]
MODEL_VERSION = os.environ["MODEL_VERSION"]

mlflow.set_tracking_uri(os.environ["DATABRICKS_HOST"])

local_path = mlflow.artifacts.download_artifacts(
    artifact_uri=f"models:/{MODEL_NAME}/{MODEL_VERSION}",
    dst_path="model/"
)

print(f"Model downloaded to {local_path}")
