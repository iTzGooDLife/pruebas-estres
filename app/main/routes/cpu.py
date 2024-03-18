from flask import Blueprint, render_template
import threading

bp = Blueprint("cpu", __name__)


def consume_cpu():
    # range = 1000000 # Se congestiona, pero no tanto, con un considerable volumen de request si
    rango = 1000000
    return [x**5 for x in range(rango)]

@bp.route('/cpu')
def cpu():
    t = threading.Thread(target=consume_cpu)
    t.daemon = True
    t.start()
    return "CPU load increased."
