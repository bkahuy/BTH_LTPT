import threading
import random
from datetime import datetime
import math

N = int(input("Nhập số phần tử (N): "))
K = int(input("Nhập số luồng (K): "))

def is_perfect_square(n):
    return int(math.isqrt(n)) ** 2 == n

A = [random.randint(1, 1000) for _ in range(N)]
A[N] = 4
results = [[] for _ in range(K)]  # Lưu kết quả từ mỗi luồng

def print_perfect_squares(id, start, end):
    perfect_squares_in_segment = [A[i] for i in range(start, end) if is_perfect_square(A[i])]
    results[id] = perfect_squares_in_segment  # Ghi kết quả vào danh sách chung

    now = datetime.now()
    time_str = now.strftime("%H:%M:%S.%f")[:-3]
    
    if perfect_squares_in_segment:
        for num in perfect_squares_in_segment:
            print(f"T{id+1} ({start}-{end}): {num} - {time_str} \n")
    else:
        print(f"T{id+1} ({start}-{end}): Không có số chính phương - {time_str} \n")

threads = []

for i in range(K):
    start = i * (N // K)
    end = N if i == K - 1 else (i + 1) * (N // K)
    t = threading.Thread(target=print_perfect_squares, args=(i, start, end))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Tổng hợp và in kết quả
all_results = [num for sublist in results for num in sublist]
print(f"Danh sách số chính phương: {all_results}")
