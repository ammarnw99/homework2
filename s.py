import socket,threading

Q ={
 "1) What color is the banana ?\na.blue\nb.yellow\n": "b",
 "2) What color is the apple ?\na.blue\nb.red\n": "b",
 "3) What color is the pear ?\na.blue\nb.green\n": "b",
 "4) What color is the tomato ?\na.red\nb.blue\n": "a", 
 "5) What color is the potato?\na.Brown\nb.red\n": "a", 
 "6) What color is the cucumber?\na.green\nb.red\n": "a", 
 "7) What color is the cherry ?\na.red\nb.blue\n": "a", 
 "8) What color is apricot?\na.blue\nb.orange\n": "b", 
 "9) What color is the peach ?\na.red\nb.blue\n": "a", 
 "10) What color is the watermelon ?\na.red\nb.blue\n": "a", 
 "11) What color is the sky ?\na.red\nb.blue\n": "b", 
 "12) What color is the sun ?\na.red\nb.yellow\n": "b", 
 "13) What is the color of gold ?\na.red\nb.yellow\n": "b", 
 "14) What color is lemon?\na.red\nb.yellow\n": "b", 
 "15) What color is strawberry?\na.blue\nb.red\n": "b", 
 "16) What color is the berry?\na.yellow\nb.black\n": "b", 
 "17) What color is the grape?\na.yellow\nb.black\n": "b", 
 "18) What color is the pomegranate?\na.blue\nb.red\n": "b", 
 "19) What color is the pineapple?\na.blue\nb.yellow\n": "b", 
 "20) What color is the kiwi?\na.blue\nb.green\n": "b"}
scores = {}

def h_c(c_socket, address):
    for question in Q.keys():
        c_socket.send(question.encode())
        answer = c_socket.recv(1024).decode()

        if answer == Q[question]:
            scores[address] = scores.get(address, 0) + 1

    if address in scores:
        score_mess = 'Your score: {}/{}'.format(scores[address], len(Q))
        c_socket.send(score_mess.encode())

    c_socket.close()

def s_server():
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_socket.bind(('127.0.0.1', 2222))
    s_socket.listen(5)
    print('Server started')

    while True:
        c_socket, address = s_socket.accept()
        print('New client', address)

        c_thread = threading.Thread(target=h_c, args=(c_socket, address))
        c_thread.start()


s_server()
