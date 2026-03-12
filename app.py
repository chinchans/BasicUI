from flask import Flask, render_template_string, request

app = Flask(__name__)

PAGE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8"/>
    <title>Mini Flask UI</title>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
    <style>
      body { font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif; margin: 2rem; }
      .card { max-width: 520px; margin: auto; padding: 1.5rem; border: 1px solid #ddd; border-radius: 12px; }
      h1 { font-size: 1.25rem; margin: 0 0 1rem; }
      input, button { padding: .6rem .8rem; font-size: 1rem; }
      input { width: 100%; box-sizing: border-box; margin-bottom: .8rem; }
      button { background: #0a66c2; color: #fff; border: none; border-radius: 8px; cursor: pointer; }
      button:hover { background: #084f97; }
      .result { margin-top: 1rem; padding:.8rem; background:#f6f8fa; border-radius:8px; }
    </style>
  </head>
  <body>
    <div class="card">
      <h1>Say Hello 👋</h1>
      <form method="post">
        <input name="name" placeholder="Enter your name" required />
        <button type="submit">Greet</button>
      </form>
      {% if message %}
      <div class="result">{{ message }}</div>
      {% endif %}
    </div>
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    message = None
    if request.method == "POST":
        name = request.form.get("name", "").strip() or "there"
        message = f"Hello, {name}! Welcome to NextGenR&D Team. "
    return render_template_string(PAGE, message=message)

if __name__ == "__main__":
    # Bind to 0.0.0.0 so it's reachable from the container port mapping
    app.run(host="0.0.0.0", port=8000, debug=False)

