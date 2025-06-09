import xmlrpc.client

# Kết nối đến server RPC
proxy = xmlrpc.client.ServerProxy("http://172.20.10.7:8001/")

# Nhập N từ người dùng
N = int(input("Nhập N: "))

# Gọi phương thức X từ server
ket_qua = proxy.X1(N)

# Hiển thị kết quả
print("Các số nguyên tố từ 2 đến", N, "là:", ket_qua)
10