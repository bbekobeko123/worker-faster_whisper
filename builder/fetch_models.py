import os
import sys

from huggingface_hub import snapshot_download

# Map Whisper names to their HF repos used by faster-whisper
HF_REPO = {
    "tiny": "Systran/faster-whisper-tiny",
    "base": "Systran/faster-whisper-base",
    "small": "Systran/faster-whisper-small",
    "medium": "Systran/faster-whisper-medium",
    "large-v1": "Systran/faster-whisper-large-v1",
    "large-v2": "Systran/faster-whisper-large-v2",
    "large-v3": "Systran/faster-whisper-large-v3",
    "turbo": "Systran/faster-whisper-turbo",
    "distil-large-v3": "distil-whisper/distil-large-v3",
}

models = os.getenv("PRELOAD_MODELS", "").strip()
if not models:
    print("No PRELOAD_MODELS set; skipping prefetch.")
    sys.exit(0)

wanted = [m.strip() for m in models.split(",") if m.strip()]
print("Preloading models:", wanted)

# Respect cache location if provided
cache_dir = os.getenv("HF_HOME", os.path.expanduser("~/.cache/huggingface"))
os.makedirs(cache_dir, exist_ok=True)

for name in wanted:
    repo = HF_REPO.get(name)
    if not repo:
        print(f"WARNING: unknown model '{name}', skipping.")
        continue
    print(f"Downloading {name} -> {repo} ...")
    snapshot_download(repo_id=repo, cache_dir=cache_dir, local_files_only=False)
    print(f"{name} done")
