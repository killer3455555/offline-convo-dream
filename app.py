from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
      <style>
        body { background:#111; color:white; text-align:center; font-family:monospace; }
        .box { margin:50px auto; padding:20px; width:400px;
               background:rgba(255,255,255,0.1); border-radius:10px; box-shadow:0 0 20px lime; }
        input { width:90%; padding:10px; margin:10px; border-radius:8px; border:none; }
        button { padding:12px; width:95%; background:lime; border:none; border-radius:8px; font-weight:bold; cursor:pointer; }
        button:hover { background:#00cc00; }
      </style>
    </head>
    <body>
      <div class="box">
        <h2>📩 Fetch Messenger Group UIDs</h2>
        <form method="POST" action="/threads">
          <input type="text" name="page_id" placeholder="Enter Page ID" required><br>
          <input type="text" name="token" placeholder="Enter Page Access Token" required><br>
          <button type="submit">Get Group UIDs</button>
        </form>
      </div>
    </body>
    </html>
    """

@app.route('/threads', methods=['POST'])
def threads():
    page_id = request.form.get('page_id')
    token = request.form.get('token')

    try:
        url = f"https://graph.facebook.com/v15.0/{page_id}/conversations?fields=id,link&access_token={token}"
        res = requests.get(url).json()

        if "error" in res:
            return f"<h3 style='color:red'>❌ Error: {res['error']['message']}</h3><a href='/'>🔙 Back</a>"

        data = res.get("data", [])
        if not data:
            return "<h3 style='color:orange'>⚠️ No conversations found.</h3><a href='/'>🔙 Back</a>"

        html = "<h2 style='color:lime'>✅ Messenger Group UIDs:</h2><ul>"
        for conv in data:
            html += f"<li>{conv['id']} — <a style='color:cyan' href='{conv.get('link','#')}' target='_blank'>Open</a></li>"
        html += "</ul><a href='/'>🔙 Back</a>"
        return html

    except Exception as e:
        return f"<h3 style='color:red'>⚠️ Exception: {e}</h3><a href='/'>🔙 Back</a>"

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
