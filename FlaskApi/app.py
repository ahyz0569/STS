from flask import Flask, jsonify, escape, request, render_template

from PIL import Image
from io import BytesIO
import base64

app = Flask(__name__)


# app.route 를 사용해 매핑해준다.
# render_template -> 사용해 templates의 html 파일을 불러오겠다는 뜻

@app.route('/main')
def hello():
    name = request.args.get("name", "World")
#    return f'Hello, {escape(name)}!'
    return render_template('main.html')

@app.route('/testapi',methods=["POST","GET"])
def test():
    # data = request.getJson()
    # print(data)
    # print(request.get_data())
    image = base64.b64decode(request.get_data())
    im=Image.open(BytesIO(image))
    print(im)
    # return jsonify(message="응답 메시지")
    return "응답메시지"

@app.route('/testjson')
def json():
    # flask 에서 기본적으로 제공하는 jsonify함수를 통해 값을 json형태로 전환할 수 있다.
    print(jsonify(name='JKS'))
    return jsonify(name='JKS')

if __name__ == '__main__':
    app.run(debug=True)