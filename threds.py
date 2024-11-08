import threading
import time

def thread_task(thread_name, sleep_time):
    print(f"Поток {thread_name} начинает выполнение.")
    time.sleep(sleep_time)  # Имитация выполнения задачи
    print(f"Поток {thread_name} завершил выполнение.")


threads = []

for i in range(5):
    thread_name = f"Thread-{i+1}"
    sleep_time = i + 1  # Разное время ожидания для каждого потока
    thread = threading.Thread(target=thread_task, args=(thread_name, sleep_time))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Все потоки завершили выполнение.")
