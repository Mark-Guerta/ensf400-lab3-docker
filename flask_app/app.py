from flask import Flask, render_template
import random

app = Flask(__name__)

images = [
    "https://upload.wikimedia.org/wikipedia/commons/7/7e/Panhard_EBR_150808_01.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/USAF_X32B_250.jpg/1200px-USAF_X32B_250.jpg",
    "https://1000logos.net/wp-content/uploads/2020/08/Python-Logo.jpg",
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")