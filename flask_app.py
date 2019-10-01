from settings import confirmation_string
from flask import Flask, request, abort
import messageHandler

app = Flask(__name__)


@app.route("/", methods=["POST"])
def bot():
    resp = request.json()
    if 'type' not in resp.keys():
        return abort(400)
    if resp['type'] == 'confirmation':
        return confirmation_string
    elif resp['type'] == 'message_new':
        print(resp)
        messageHandler.create_answer(peer_id=resp['object']['peer_id'],
                                     message=resp['object']['text'].lower(),
                                     attachment=resp['object']['attachments'])
        return 'ok'
    else:
        return 'ok'


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)

