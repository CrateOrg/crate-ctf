import sys
import socket
import random
import string

DEBUG = False
FLAG = b"cratectf{myportnoyourportokourport}\n"

def debug_msg(msg: str):
	if DEBUG:
		print(msg)


def generate_random_string(length: str = 100):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))


def get_socket_random_port(port_min: int, port_max: int, timeout: int = 10) -> socket.socket:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    while True:
        try:
            port = random.randint(port_min, port_max)
            s.settimeout(timeout)
            s.bind(("0.0.0.0", port))
            return s
        except OSError:
            continue


def main():
    s = get_socket_random_port(20000, 49999, 30)
    rnd_srcport = random.randint(5000, 30000)
    random_string = generate_random_string()

    message = f"""Hello messenger! 
Please deliver the following important message to me within a few seconds, on the port {s.getsockname()[1]}. 
In order for me to authenticate you, make sure you connect from the port {rnd_srcport}.

{random_string}
"""
    print(message)

    s.listen(1)
    try:
        conn, addr = s.accept()
    except socket.timeout:
        print("Sorry, time's up!")
        sys.exit()

    debug_msg(f"got connection from {addr[0]}:{addr[1]}")
    with conn:
        if addr[1] == rnd_srcport:
            try:
                conn.settimeout(10)
                data = conn.recv(1024)
            except Exception as e:
                data = ""
            if data is not None:
                if len(data) == 0:
                    conn.sendall(b'Sorry, time\'s up!\n')
                elif data.decode('utf-8')[:100] == random_string:
                    conn.sendall(FLAG)
                else:
                    conn.sendall(b'Sorry, i don\'t know what you\'re talking about\n')
        else:
            conn.sendall(b'Sorry, I don\'t trust you when you come from that port.\n')
        try:
            conn.shutdown(socket.SHUT_RDWR)
            conn.close()
        except Exception as e:
            pass


if __name__ == "__main__":
    main()


