from flask import Blueprint, render_template

bp = Blueprint("disk_read", __name__)

def read_random_file(filename, size):

    with open(filename, 'rb') as source:
        buffer = source.read(size * 1024 * 1024)

@bp.route('/disk_read')
def disk_read():
    size = 500
    read_random_file('/dev/urandom', size)
    return f"A random file of size {size}MB was read :)"
