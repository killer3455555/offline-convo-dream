from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Robin Web</title>
      <style>
        body {
          background-color: #000;
          color: white;
          font-family: 'Courier New', monospace;
          text-align: center;
          margin: 0;
          padding: 20px;
        }
        h1 {
          color: #ff00ff;
          text-shadow: 0 0 20px #ff00ff;
          margin-bottom: 5px;
        }
        h3 {
          color: #fff;
          margin-bottom: 30px;
        }
        .btn {
          display: block;
          width: 300px;
          margin: 20px auto;
          padding: 15px;
          background: #00faff;
          color: #000;
          text-decoration: none;
          font-weight: bold;
          border-radius: 8px;
          box-shadow: 0 0 15px #00faff, 0 0 40px #00faff;
          transition: 0.3s;
        }
        .btn:hover {
          background: #00c8c8;
          box-shadow: 0 0 25px #00faff, 0 0 60px #00faff;
        }
      </style>
    </head>
    <body>
      <h1>🤍 MUDDasir WEB 🤍</h1>
      <h3>( ALL OPTION )</h3>

      <a class="btn" href="/convo">◄ 1 - CONVO SERVER ►</a>
      <a class="btn" href="/backup">◄ 2 - BACKUP CONVO ►</a>
      <a class="btn" href="/check">◄ 3 - TOKEN CHECK VALIDITY ►</a>
      <a class="btn" href="/uids">◄ 4 - FETCH ALL UID WITH TOKEN ►</a>
      <a class="btn" href="/page">◄ 5 - FETCH PAGE TOKENS ►</a>
      <a class="btn" href="/group">◄ 6 - GROUP NAME LOCKER ►</a>
    </body>
    </html>
    '''

# Example dummy routes
@app.route('/convo')
def convo():
    return "<h2 style='color:lime'>🚀 Convo Server Page</h2>"

@app.route('/backup')
def backup():
    return "<h2 style='color:orange'>📦 Backup Convo Page</h2>"

@app.route('/check')
def check():
    return "<h2 style='color:yellow'>🔑 Token Check Page</h2>"

@app.route('/uids')
def uids():
    return "<h2 style='color:cyan'>🆔 Fetch UID Page</h2>"

@app.route('/page')
def page():
    return "<h2 style='color:violet'>📃 Page Tokens Page</h2>"

@app.route('/group')
def group():
    return "<h2 style='color:red'>🔒 Group Name Locker Page</h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
