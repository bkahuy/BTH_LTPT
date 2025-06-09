import threading
import random
import time
from datetime import datetime

# Tham số cấu hình
N = int(input("Nhập số phần tử (N): "))
k = int(input("Nhập số luồng (K): "))
h = int(input("Nhập số luồng (H): "))

# Cấu trúc chia sẻ
A = []  # danh sách dùng thay cho Queue
lock = threading.Lock()  # bảo vệ danh sách A
empty_slots = threading.Semaphore(N)  # semaphore chờ chỗ trống
filled_slots = threading.Semaphore(0)  # semaphore chờ phần tử

# In giờ hiện tại đẹp
def current_time():
    return datetime.now().strftime("%H:%M:%S")

# Luồng producer
def producer_thread(index):
    while True:
        time.sleep(random.uniform(0.5, 2))  # chờ ngẫu nhiên
        value = random.randint(1, 1000)

        empty_slots.acquire()
        with lock:
            A.append(value)
        filled_slots.release()

        print(f"P{index}: {value} - {current_time()}")

# Luồng consumer: tìm số lớn nhất trong A và xóa nó
def consumer_thread(index):
    while True:
        time.sleep(random.uniform(1, 3))

        filled_slots.acquire()
        with lock:
            if A:
                max_val = max(A)
                A.remove(max_val)  # xóa phần tử lớn nhất
            else:
                max_val = None
        empty_slots.release()

        if max_val is not None:
            print(f"C{index}: {max_val} - Max found and removed - {current_time()}")

# Khởi động các luồng producer
for i in range(k):
    threading.Thread(target=producer_thread, args=(i + 1,), daemon=True).start()

# Khởi động các luồng consumer
for i in range(h):
    threading.Thread(target=consumer_thread, args=(i + 1,), daemon=True).start()

# Giữ chương trình chạy vô hạn
while True:
    time.sleep(1)
