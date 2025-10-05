import threading
import time

fin= False

def worker():
    counter=0
    while not fin:
        time.sleep(1)
        counter +=1
        print(counter)

threading.Thread(target=worker, daemon=True).start()

input ("Press enter to quit")
fin=True    