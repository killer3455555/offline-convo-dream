from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
      <style>
        body { background:#000; color:white; text-align:center; font-family:monospace; }
        .box {
          margin:50px auto; padding:20px; width:400px;
          background:rgba(255,255,255,0.1);
          border-radius:10px; box-shadow:0 0 20px cyan;
        }
        input { width:90%; padding:10px; margin:10px; border-radius:8px; border:none; }
        button { padding:12px; width:95%; background:cyan; border:none;
                 border-radius:8px; font-weight:bold; cursor:pointer; }
        button:hover { background:#00c8c8; }
      </style>
    </head>
    <body>
      <div class="box">
        <h2>📌 Fetch All Group UIDs</h2>
        <form method="POST" action="/groups">
          <input type="text" name="token" placeholder="Enter Access Token" required><br>
          <button type="submit">Get Group UIDs</button>
        </form>
      </div>
    </body>
    </html>
    """

@app.route('/groups', methods=['POST'])
def groups():
    token = request.form.get('token')

    try:
        # Facebook Graph API endpoint to fetch groups
        url = f"https://graph.facebook.com/v15.0/me/groups?access_token={token}"
        res = requests.get(url).json()

        if "error" in res:
            return f"<h3 style='color:red'>❌ Error: {res['error']['message']}</h3><a href='/'>🔙 Back</a>"

        groups = res.get("data", [])
        if not groups:
            return "<h3 style='color:orange'>⚠️ No groups found for this token.</h3><a href='/'>🔙 Back</a>"

        html = "<h2 style='color:cyan'>✅ Group UIDs:</h2><ul>"
        for g in groups:
            html += f"<li style='color:lime'>{g['id']} — {g.get('name','(No Name)')}</li>"
        html += "</ul><a href='/'>🔙 Back</a>"
        return html

    except Exception as e:
        return f"<h3 style='color:red'>⚠️ Exception: {e}</h3><a href='/'>🔙 Back</a>"

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
