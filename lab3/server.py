import socket
import threading
import pickle
import math

def is_perfect_square(n):
    return int(math.isqrt(n)) ** 2 == n

def handle_client(conn, addr):
    print(f"[SERVER] Kết nối từ {addr}")
    
    #
    data = conn.recv(4096)
    array = pickle.loads(data)
    print(f"[SERVER] Nhận mảng {len(array)} phần tử từ {addr}")
    print(f"[SERVER] Nhận mảng {array}")

    #
    result = [x for x in array if is_perfect_square(x)]
    print(f"[SERVER] Tìm thấy {len(result)} phần tử là số chính phương từ {addr}")
    print(f"[SERVER] Các số chính phương: {result}")

    #
    conn.send(pickle.dumps(result))
    conn.close()

def main():
    HOST = '0.0.0.0' 
    PORT = 12345

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[SERVER] Đang lắng nghe trên cổng {PORT}...")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    main()