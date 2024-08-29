from counterfit_connection import CounterFitConnection
import time
from counterfit_shims_seeed_python_dht import DHT
import requests

# Kết nối tới CounterFit
CounterFitConnection.init('127.0.0.1', 5000)

# Khởi tạo cảm biến DHT (loại 11) với pin kết nối là 5
sensor = DHT("11", 5)

# URL và access token của ThingsBoard
THINGSBOARD_HOST = 'http://localhost:8080'
ACCESS_TOKEN = 'd34nmcteqvv3a4wwu5dw'

# URL API của ThingsBoard
url = f"{THINGSBOARD_HOST}/api/v1/{ACCESS_TOKEN}/telemetry"

print('Hello World!')

while True:
    # Đọc dữ liệu từ cảm biến
    humidity, temp = sensor.read()
    
    # In ra màn hình để kiểm tra
    print(f'Temperature: {temp}°C, Humidity: {humidity}%')
    
    # Định dạng dữ liệu để gửi tới ThingsBoard
    data = {
        "Nhiệt Độ": temp,
        "Độ Ẩm": humidity
    }

    # Gửi dữ liệu tới ThingsBoard
    response = requests.post(url, json=data)
    
    # Kiểm tra phản hồi từ ThingsBoard
    if response.status_code == 200:
        print("Data sent successfully!")
    else:
        print(f"Failed to send data. Status code: {response.status_code}")

    # Chờ 10 giây trước khi gửi dữ liệu lần nữa
    time.sleep(10)
