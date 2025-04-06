<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>📘 Shorty - Project ReadMe</title>
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      background: #f9f9f9;
      color: #333;
      margin: 0;
      padding: 2rem;
      line-height: 1.7;
    }
    h1, h2, h3 {
      color: #4f46e5;
    }
    code, pre {
      background: #eee;
      padding: 0.2rem 0.5rem;
      border-radius: 5px;
    }
    .screenshot {
      width: 100%;
      max-width: 600px;
      border-radius: 10px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.1);
      margin: 1rem 0;
    }
    .feature-list li {
      margin: 0.4rem 0;
    }
    a {
      color: #4f46e5;
    }
    .section {
      margin-top: 2rem;
    }
  </style>
</head>
<body>

  <h1>🔗 Shorty — A Modern URL Shortener Built with Flask</h1>
  <img src="screenshots/shorty-preview.png" alt="Shorty Preview" class="screenshot">

  <div class="section">
    <h2>✨ Features</h2>
    <ul class="feature-list">
      <li>✅ Clean, responsive UI</li>
      <li>🔗 Shorten any long URL instantly</li>
      <li>✍️ Optional custom aliases</li>
      <li>📈 Built-in analytics (click tracking)</li>
      <li>🌙 Light/Dark mode toggle</li>
      <li>🚀 Ready for deployment (Render, Heroku, etc.)</li>
    </ul>
  </div>

  <div class="section">
    <h2>📸 Screenshots</h2>
    <h3>Homepage</h3>
    <img src="screenshots/home.png" alt="Home Page" class="screenshot">
    <h3>Stats Page</h3>
    <img src="screenshots/stats.png" alt="Stats Page" class="screenshot">
  </div>

  <div class="section">
    <h2>🚀 Getting Started</h2>
    <h3>🔧 Prerequisites</h3>
    <pre><code>python --version</code></pre>

    <h3>🛠️ Installation</h3>
    <pre><code>
git clone https://github.com/your-username/shorty-url-shortener.git
cd shorty-url-shortener
pip install flask
python app.py
    </code></pre>
    <p>Then open your browser to <code>http://127.0.0.1:5000</code></p>
  </div>

  <div class="section">
    <h2>🌍 Deployment</h2>
    <p>You can deploy Shorty easily on:</p>
    <ul>
      <li><a href="https://render.com">Render</a></li>
      <li><a href="https://heroku.com">Heroku</a></li>
      <li><a href="https://railway.app">Railway</a></li>
    </ul>
    <p>Just create a <code>requirements.txt</code> with:</p>
    <pre><code>flask</code></pre>
  </div>

  <div class="section">
    <h2>🧠 Tech Stack</h2>
    <ul>
      <li><strong>Backend:</strong> Python + Flask</li>
      <li><strong>Frontend:</strong> HTML5, CSS3, Vanilla JS</li>
      <li><strong>Database:</strong> SQLite3 (file-based)</li>
    </ul>
  </div>

  <div class="section">
    <h2>🪄 Credits</h2>
    <p>Made with ❤️ by <a href="https://github.com/your-username">Your Name</a></p>
    <p>Icons from <a href="https://emojione.com">EmojiOne</a></p>
    <p>UI inspired by minimalism ✨</p>
  </div>

  <div class="section">
    <h2>📜 License</h2>
    <p>This project is open-source under the <a href="#">MIT License</a>.</p>
  </div>

</body>
</html>
