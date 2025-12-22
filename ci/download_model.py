import os
import requests
from databricks.sdk import WorkspaceClient

MODEL_NAME = os.environ["MODEL_NAME"]
MODEL_VERSION = os.environ["MODEL_VERSION"]

client = WorkspaceClient()

print(f"📦 Downloading model {MODEL_NAME} version {MODEL_VERSION}")

resp = client.model_versions.get_download_uri(
    name=MODEL_NAME,
    version=MODEL_VERSION
)

url = resp.artifact_uri

with requests.get(url, stream=True) as r:
    r.raise_for_status()
    with open("model.zip", "wb") as f:
        for chunk in r.iter_content(8192):
            f.write(chunk)

import zipfile
with zipfile.ZipFile("model.zip") as z:
    z.extractall("model")

print("✅ Model downloaded and extracted")
