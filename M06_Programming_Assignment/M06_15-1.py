import multiprocessing as mp

def currentTime(seconds):
    from time import sleep
    from datetime import datetime
    sleep(seconds)
    print(f'Time passed: {seconds} seconds, now the time is: {datetime.utcnow()}')

if __name__ == '__main__':
    import random
    for i in range(3):
        seconds = random.random()
        process = mp.Process(target=currentTime, args=(seconds,))
        process.start()