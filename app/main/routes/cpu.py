from flask import Blueprint, render_template
import threading

bp = Blueprint("cpu", __name__)

cpu_threads = []

def consume_cpu():
    while True:
        [x**2 for x in range(10000)]

@bp.route('/cpu')
def cpu():
    t = threading.Thread(target=consume_cpu)
    t.daemon = True
    t.start()
    cpu_threads.append(t)
    return f"CPU load increased. Total threads: {len(cpu_threads)}"
