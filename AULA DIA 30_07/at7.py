import time

while True:
    hora_atual = time.strftime("%H:%M:%S", time.localtime())
    print(f"Hora atual: {hora_atual}")
    time.sleep(1)
