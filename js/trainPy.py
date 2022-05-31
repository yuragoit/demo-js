import threading
import time

# We can literally cut this time by a magnitude of four if we run each process on its own thread


def paint_wall():
    print('Painting wall...')
    # Wait 30m
    time.sleep(2)
    print('Done painting wall')


walls_to_paint = 4

for k in range(0, walls_to_paint):
    t = threading.Thread(target=paint_wall)
    t.start()
