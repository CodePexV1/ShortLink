from flask import Flask, render_template, request, redirect
import sqlite3, random, string

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect('database.db')
    return conn

def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form['url']
        short = generate_short_url()

        conn = get_db()
        conn.execute("INSERT INTO urls (original, short) VALUES (?, ?)", (original_url, short))
        conn.commit()
        conn.close()
        return render_template('success.html', short_url=request.host_url + short)

    return render_template('index.html')

@app.route('/<short>')
def redirect_short_url(short):
    conn = get_db()
    cursor = conn.execute("SELECT original FROM urls WHERE short = ?", (short,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return redirect(result[0])
    return 'URL not found', 404

if __name__ == '__main__':
    with get_db() as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY, original TEXT, short TEXT)')
    app.run(debug=True)
