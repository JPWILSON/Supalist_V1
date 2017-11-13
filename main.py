from flask import Flask, render_template, request, url_for, redirect, flash, jsonify

app = Flask(__name__)

@app.route('/')
def Lists():
	return "List of restaurants"