import time

while True:
    hora_atual = time.strftime("%H:%M:%S")
    print(f"Hora atual: {hora_atual}")
    time.sleep(1)
