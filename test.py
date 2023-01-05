from flask import Flask
import os
import time
app = Flask(__name__)
@app.route('/api/stream', methods=['GET'])
def handle_streaming_thread_init():
    time.sleep(10)
    return 'OK', 200
app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8081)))
