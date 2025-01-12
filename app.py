from flask import Flask, render_template

app = Flask(__name__)

# Route untuk halaman index (root)
@app.route('/')
def index():
    return render_template('index.html')

# Route untuk halaman perhitungan
@app.route('/perhitungan.html')
def perhitungan():
    return render_template('perhitungan.html')

if __name__ == '__main__':
    app.run(debug=True)
