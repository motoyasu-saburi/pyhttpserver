import socket


LOCAL_IP = "127.0.0.1"
BIND_PORT = 8080


with socket.socket(
    socket.AF_INET, # AF = IPv4
    socket.SOCK_STREAM # TCP/IP
  ) as soc:

  soc.bind((LOCAL_IP, BIND_PORT))
  # 接続
  soc.listen(1)

  # Connection するまで待つ TODO ここの Loop が Connection が終わるまで待つ部分と重複してるのでまとめる
  while True:
    # Connect 成功後、Connectionと Address を取得
    conn, addr = soc.accept()
    with conn:
      while True:
        # connection からデータを少しずつ受け取る
        data = conn.recv(1024)
        if not data:
          break
        print('data : {}, addr: {}'.format(data, addr))
        # Client にデータを返す (b -> byte でないといけない）
        conn.sendall(b'Received: ' + data)

