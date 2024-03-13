#from flask import Flask
from flask import Blueprint
import threading
import time

bp = Blueprint("memory", __name__)

memory_threads = []

def consume_memory():
    my_list = []
    while True:
        my_list.append(' ' * 10**6)
        time.sleep(1)

@bp.route('/memory')
def memory():
    t = threading.Thread(target=consume_memory)
    t.daemon = True
    t.start()
    memory_threads.append(t)
    return f"Memory load increased. Total threads: {len(memory_threads)}"
