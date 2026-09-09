import time
import urllib.request

URL = "https://buildlabs-task1.onrender.com/health"

try:
    start_time = time.time()

    response = urllib.request.urlopen(URL, timeout=30)

    end_time = time.time()

    response_time = round((end_time - start_time) * 1000, 2)

    if response.status == 200:
        print("STATUS: UP")
        print(f"HTTP Status: {response.status}")
        print(f"Response Time: {response_time} ms")
    else:
        print("STATUS: DOWN")
        print(f"HTTP Status: {response.status}")

except Exception as error:
    print("STATUS: DOWN")
    print(f"Error: {error}")