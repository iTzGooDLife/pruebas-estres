from flask import Flask
from main.routes import helloWorld
from main.routes import cpu
from main.routes import memory 
from main.routes import disk_read
from main.routes import disk_write

def create_app():
    app = Flask(__name__)
    app.register_blueprint(helloWorld.bp)
    app.register_blueprint(cpu.bp)
    app.register_blueprint(memory.bp)
    app.register_blueprint(disk_read.bp)
    app.register_blueprint(disk_write.bp)
    return app

