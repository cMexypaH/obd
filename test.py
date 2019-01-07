#!/usr/bin/env python

from time import time, sleep
import obd

last_call = 0
def cb_speed(response):
    global last_call
    print(response.value) 
    print("Time since last call: %d", time() - last_call)
    last_call = time()

if __name__ == "__main__":
    obd_connection = obd.Async("\.\COM4")
    obd_connection.watch(obd.commands.RPM, callback=cb_speed)
    obd_connection.watch(obd.commands.SPEED, callback=cb_speed)
    obd_connection.start()

    # Stop after 60s
    sleep(60)

    obd_connection.stop()
