import subprocess

def run_model(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "gemma:2b", prompt],
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Model error: {e}"