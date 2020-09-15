from main import Decalander, Decatime
from time import sleep
from threading import Timer, Event


def print_now():
    date = Decalander.today()
    time = Decatime.now()
    print(date, time, end="\r")


if __name__ == "__main__":
    delay = 1 / Decatime.RATIO
    ticker = Event()
    while not ticker.wait(delay):
        print_now()
