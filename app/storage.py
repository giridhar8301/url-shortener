from app.utils import generate_short_code
from datetime import datetime
import threading

# in-memory store
store = {}
lock = threading.Lock()

def save_url(original_url):
    with lock:
        while True:
            code = generate_short_code()
            if code not in store:
                break

        store[code] = {
            "url": original_url,
            "clicks": 0,
            "created_at": datetime.utcnow().isoformat()
        }

    return code, f"http://localhost:5000/{code}"

def get_url_data(code):
    return store.get(code)

def increment_clicks(code):
    with lock:
        if code in store:
            store[code]["clicks"] += 1
