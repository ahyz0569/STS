from flask import Flask, jsonify, escape, request, render_template

from PIL import Image
from io import BytesIO
import base64


import torch
import torchvision
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from torchvision import transforms
from detecto import core, utils, visualize


app = Flask(__name__)

model = None

# app.route 를 사용해 매핑해준다.
# render_template -> 사용해 templates의 html 파일을 불러오겠다는 뜻

# @app.route('/main')
# def hello():
#     name = request.args.get("name", "World")
# #    return f'Hello, {escape(name)}!'
#     return render_template('main.html')


def show_labeled_image(image, boxes, labels=None):    
    fig, ax = plt.subplots(1)
    plt.rcParams.update({'font.size': 22})
    fig.set_size_inches(30, 20)
    # If the image is already a tensor, convert it back to a PILImage
    # and reverse normalize it
    if isinstance(image, torch.Tensor):
        image = reverse_normalize(image)
        image = transforms.ToPILImage()(image)
    ax.imshow(image)
    # Show a single box or multiple if provided
    if boxes.ndim == 1:
        boxes = boxes.view(1, 4)
    if labels is not None and not utils._is_iterable(labels):
        labels = [labels]
    # Plot each box
    for i in range(boxes.shape[0]):
        box = boxes[i]
        width, height = (box[2] - box[0]).item(), (box[3] - box[1]).item()
        initial_pos = (box[0].item(), box[1].item())
        rect = patches.Rectangle(initial_pos,  width, height, linewidth=1,
                                 edgecolor='r', facecolor='none')
        if labels:
            ax.text(box[0] + 5, box[1] - 5, '{}'.format(labels[i]), color='red')
        ax.add_patch(rect)
    # plt.show()    
    fig.savefig('static/images/test2.jpg', dpi=100)
#     fig.savefig('result.png')
    plt.close(fig)




@app.route('/testapi',methods=["POST","GET"])
def test():
    # data = request.getJson()
    # print(data)

    im = base64.b64decode(request.get_data())
    image=Image.open(BytesIO(im))
    predictions = model.predict(image)
    labels, boxes, scores = predictions
    detection_class2=list(set(labels))
    
    show_labeled_image(image, boxes, labels)

    with open('static/images/test2.jpg','rb') as img:
        response_img = base64.b64encode(img.read())

    return response_img


@app.route('/testModel',methods=["POST","GET"])
def test2():
    

    return "성공"

# @app.route('/testjson')
# def json():
#     # flask 에서 기본적으로 제공하는 jsonify함수를 통해 값을 json형태로 전환할 수 있다.
#     print(jsonify(name='JKS'))
#     return jsonify(name='JKS')


if __name__ == '__main__':
    labels = ['chilli', 'egg', 'pork meat', 'potato', 'pa', 'onion']
    model = core.Model.load('static/model/ingredients_weights_ver01_0326.pth', labels)
    app.run(debug=True , host='0.0.0.0')