import time
print("Shh.. don't wake me, I am sleeping")
while True:
    for _ in range(5):
        print('z'*_)
        time.sleep(1)
    time.sleep(3)
