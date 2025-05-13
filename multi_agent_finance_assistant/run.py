import subprocess
import threading

def run_fastapi():
    subprocess.run(["uvicorn", "orchestrator.fastapi_app:app", "--host", "0.0.0.0", "--port", "8000"])

def run_streamlit():
    subprocess.run(["streamlit", "run", "streamlit_app/main.py", "--server.port=8501"])

# Run both in parallel
if __name__ == "__main__":
    t1 = threading.Thread(target=run_fastapi)
    t2 = threading.Thread(target=run_streamlit)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
