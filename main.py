from flask import Flask, request, make_response, send_file, render_template, url_for

app = Flask(__name__)
app.static_folder = 'static'
@app.route('/')
def home():
    app.static_folder = 'static'
    return render_template('index.html')

if __name__ == '__main__':
    app.run()