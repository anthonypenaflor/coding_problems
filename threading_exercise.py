import concurrent.futures
import threading
import time


def do_request(statements):

    print(f"{statements}")


def threading_ex():

    threads = []

    for _ in range(10):
        t = threading.Thread(target=do_request)
        t.start()
        threads.append(t)

    for i in range(len(threads)):
        threads[i].join()


def multiprocess():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(do_request, statements)


def multithreading():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(do_request, statements)


if __name__ == '__main__':
    statements = ["Hello,", "how", "are", "you", "today"]
    # threading_ex()

    # multiprocess
    t1 = time.perf_counter()
    multiprocess()
    t2 = time.perf_counter()
    print(f'Finished in {t2 - t1} seconds')

    # multithreading
    t3 = time.perf_counter()
    multithreading()
    t4 = time.perf_counter()
    print(f'Finished in {t4 - t3} seconds')

