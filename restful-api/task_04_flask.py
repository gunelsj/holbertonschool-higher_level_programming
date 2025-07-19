from flask import Flask, jsonify
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/posts', methods=['GET'])
def get_posts():
    try:
        with open('posts.csv', mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            posts = [row for row in csv_reader]
        return jsonify(posts)
    except FileNotFoundError:
        return jsonify({'error': 'posts.csv not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
