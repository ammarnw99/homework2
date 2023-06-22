import socket

def s_client():
    server_add = ('localhost', 2222)
    c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c_socket.connect(server_add)
    
    for i in range (20):
        ques = c_socket.recv(1024).decode()
        print("Question:", ques)
        ans = input("Your answer (a or b): ")
        c_socket.sendall(ans.encode())
    
    finish_score = c_socket.recv(1024).decode()
    print("score" , finish_score)


s_client()
