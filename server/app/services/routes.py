from flask import Flask, request, jsonify
# from app import app


@app.route('/')
@app.route('/index')
def index():
    return 'This is Enigma API Service!'


