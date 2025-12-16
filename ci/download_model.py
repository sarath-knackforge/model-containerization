import os
import requests
from databricks.sdk import WorkspaceClient

MODEL_NAME = os.environ["MODEL_NAME"]
MODEL_VERSION = os.environ["MODEL_VERSION"]

client = WorkspaceClient()

print(f"📦 Preparing download for {MODEL_NAME} v{MODEL_VERSION}")

# 1️⃣ Get presigned download URL for UC model
resp = client.model_versions.get_download_uri(
    name=MODEL_NAME,
    version=MODEL_VERSION
)

download_url = resp.artifact_uri
print("🔗 Got presigned download URL")

# 2️⃣ Download model artifacts as ZIP
zip_path = "model.zip"

with requests.get(download_url, stream=True) as r:
    r.raise_for_status()
    with open(zip_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

print("✅ Model ZIP downloaded")

# 3️⃣ Extract
import zipfile
with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall("model")

print("✅ Model extracted to ./model")
