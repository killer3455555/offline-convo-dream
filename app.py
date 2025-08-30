from flask import Flask, request

app = Flask(__name__)

# ---------------- HOME PAGE ----------------
@app.route('/')
def home():
    return """
    <html>
    <head>
      <style>
        body { background:#000; text-align:center; font-family:monospace; }
        h1 { color:#ff00ff; text-shadow:0 0 15px #ff00ff; }
        .btn {
          display:block; width:300px; margin:15px auto; padding:15px;
          background:#00faff; color:black; text-decoration:none; font-weight:bold;
          border-radius:8px; box-shadow:0 0 15px #00faff,0 0 40px #00faff;
        }
        .btn:hover { background:#00c8c8; }
      </style>
    </head>
    <body>
      <h1>🤍 ROBIN WEB 🤍</h1>
      <h3 style="color:white">( ALL OPTION )</h3>

      <a class="btn" href="/convo">◄ 1 - CONVO SERVER ►</a>
      <a class="btn" href="/backup">◄ 2 - BACKUP CONVO ►</a>
      <a class="btn" href="/check">◄ 3 - TOKEN CHECK VALIDITY ►</a>
      <a class="btn" href="/uids">◄ 4 - FETCH ALL UID WITH TOKEN ►</a>
      <a class="btn" href="/page">◄ 5 - FETCH PAGE TOKENS ►</a>
      <a class="btn" href="/group">◄ 6 - GROUP NAME LOCKER ►</a>
    </body>
    </html>
    """

# ---------------- FETCH UID PAGE ----------------
@app.route('/uids', methods=['GET', 'POST'])
def uids():
    if request.method == 'POST':
        token = request.form.get('token')

        # ⚠️ Yahan tum apna Graph API call laga sakte ho
        # Dummy UID list example
        dummy_uids = [
            "100012345678901",
            "100098765432109",
            "100011112223334"
        ]

        html = "<h2 style='color:cyan'>🆔 UID List for Token:</h2>"
        html += f"<p style='color:yellow'>{token}</p><ul>"
        for uid in dummy_uids:
            html += f"<li style='color:lime'>{uid}</li>"
        html += "</ul><br><a href='/uids'>🔙 Back</a>"
        return html

    return """
    <html>
    <head>
      <style>
        body { background:#000; color:white; font-family:monospace; text-align:center; }
        .box {
          background:rgba(255,255,255,0.1);
          padding:20px; margin:40px auto; border-radius:10px;
          width:350px; box-shadow:0 0 20px cyan;
        }
        input {
          width:90%; padding:10px; margin:10px 0;
          border-radius:8px; border:none;
        }
        button {
          padding:12px; width:95%;
          background:cyan; border:none; border-radius:8px;
          font-weight:bold; cursor:pointer;
        }
        button:hover { background:#00c8c8; }
      </style>
    </head>
    <body>
      <div class="box">
        <h2>🔍 Fetch UID with Token</h2>
        <form method="POST">
          <input type="text" name="token" placeholder="Enter Access Token" required><br>
          <button type="submit">Fetch UIDs</button>
        </form>
      </div>
    </body>
    </html>
    """

# ---------------- OTHER PAGES ----------------
@app.route('/convo')
def convo():
    return "<h2 style='color:lime'>🚀 Convo Server Page</h2>"

@app.route('/backup')
def backup():
    return "<h2 style='color:orange'>📦 Backup Convo Page</h2>"

@app.route('/check')
def check():
    return "<h2 style='color:yellow'>🔑 Token Check Page</h2>"

@app.route('/page')
def page():
    return "<h2 style='color:violet'>📃 Page Tokens Page</h2>"

@app.route('/group')
def group():
    return "<h2 style='color:red'>🔒 Group Name Locker Page</h2>"

# ---------------- RUN APP ----------------
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
