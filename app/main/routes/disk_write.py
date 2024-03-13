from flask import Blueprint, render_template

bp = Blueprint("disk_write", __name__)

def create_random_file(filename, size_in_mb):
    size_in_bytes = size_in_mb * 1024 * 1024
    try:
        with open('/dev/urandom', 'rb') as source:
            with open(filename, 'wb') as target:
                buffer = source.read(size_in_bytes)
                target.write(buffer)
    except NameError:
        print(NameError)

@bp.route('/disk_write')
def disk_write():
    size = 100
    name = "random_file"
    create_random_file(name, size)
    return f"Created a random file named {name} of size {size}MB :)"


