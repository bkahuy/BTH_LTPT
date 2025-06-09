from xmlrpc.server import SimpleXMLRPCServer

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def X(mang):
    try:
        tong = sum(int(x) for x in mang if la_so_nguyen_to(int(x)))
        return f"Tổng các số nguyên tố là: {tong}"
    except:
        return "Dữ liệu không hợp lệ"

server = SimpleXMLRPCServer(("0.0.0.0", 8001), allow_none=True)
server.register_function(X, "xu_ly_du_lieu")

print("RPC Server đang chạy trên cổng 8001...")
server.serve_forever()
