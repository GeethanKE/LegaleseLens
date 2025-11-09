import subprocess
import json

MODEL_NAME = "gemma3:12b"  # You can change to gemma:12b if you pulled it in Ollama

def query_model(prompt):
    """Send prompt to local Ollama model and return response text."""
    try:
        result = subprocess.run(
            ["ollama", "run", MODEL_NAME, prompt],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error querying model: {e.stderr or str(e)}"
