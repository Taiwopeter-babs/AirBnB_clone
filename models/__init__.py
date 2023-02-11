#!/usr/bin/python3
"""
    Intializes the package
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
