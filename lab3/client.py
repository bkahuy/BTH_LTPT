import socket
import pickle
import random


def generate_array(n):
    return [random.randint(1, 100) for i in range(n)]


def main():
    SERVER_IP = '172.20.10.2' 
    PORT = 12345
    n = int(input("Nhập số phần tử (n): "))
    array = generate_array(n)
    print(f"[CLIENT] Đã tạo mảng {len(array)} phần tử.")
    print(f"[CLIENT] Đã tạo mảng: {array}")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, PORT))

    # Gửi mảng
    client.send(pickle.dumps(array))

    # Nhận kết quả
    result = pickle.loads(client.recv(1024))
    print(f"[CLIENT] phần tử cp mảng là: {result}")

    client.close()

if __name__ == "__main__":
    main()

