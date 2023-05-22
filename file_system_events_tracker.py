import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/jm/Downloads"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Olá, {event.src_path} foi criado!")

    def on_deleted(self, event):
        print(f"Opa! Alguém excluiu {event.src_path}!")

    def on_modified(self, event):
        print(f"Opa! Alguém modificou {event.src_path}!")

    def on_moved(self, event):
        print(f"Opa! Alguém moveu {event.src_path}!")

eventHandle = FileEventHandler()
observer = Observer()
observer.schedule(eventHandle, from_dir, recursive = True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("executando...")
except KeyboardInterrupt:
    print("interrompido!")
    observer.stop()