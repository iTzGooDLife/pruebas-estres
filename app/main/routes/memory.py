#from flask import Flask
from flask import Blueprint
import threading
import time
import gc

bp = Blueprint("memory", __name__)

def consume_memory():
    quantity = 10**7
    # return my_list.append(' ' * quantity)
    my_list = []
    for i in range(100):
        my_list.append(' ' * quantity)
    my_list.clear()
    del my_list
    """
    for _ in range(quantity):
        my_list.append(object())  
    # Liberar la lista para liberar la memoria
    my_list.clear()
    del my_list
    gc.collect()
    return
    """

@bp.route('/memory')
def memory():
    t = threading.Thread(target=consume_memory)
    t.daemon = True
    t.start()
    return "Memory load increased."
