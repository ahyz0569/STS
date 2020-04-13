from flask import Flask, jsonify, escape, request, render_template

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.metrics.pairwise import linear_kernel
from PIL import Image
from io import BytesIO
from torchvision import transforms
from detecto import core, utils, visualize
import pandas as pd
import xml.etree.ElementTree as elemTree
import numpy as np
import csv
import pickle
import base64
import torch
import torchvision
import matplotlib.pyplot as plt
import matplotlib.patches as patches


app = Flask(__name__)

model = None
X = None
vectorize = None
data = None
ingre = None
# app.route 를 사용해 매핑해준다.
# render_template -> 사용해 templates의 html 파일을 불러오겠다는 뜻

# @app.route('/main')
# def hello():
#     name = request.args.get("name", "World")
# #    return f'Hello, {escape(name)}!'
#     return render_template('main.html')
def recommend(ingre_input,main):
    srch_vector = vectorize.transform([ingre_input])
    cosine_similar = linear_kernel(srch_vector, X).flatten()
    rank_idx = cosine_similar.argsort()[::-1]
    count = 0
    idx_filtering=[]
    for i in rank_idx:
        if cosine_similar[i] > 0:
            if main in ingre[i]:
                #ingre_for_cv.append(ingre[i])
                idx_filtering.append(i)
                count+=1
                if count>100:
                    break
                    
    df = pd.DataFrame(ingre[idx_filtering],columns=['ingre'])
    df['idx_filtering']=idx_filtering
    df['calc'] = 0.
  
    ingre_for_cv = df['ingre'].tolist()
    ingre_for_cv.append(ingre_input)
    
    vect = CountVectorizer(min_df=0,tokenizer=lambda x:x.split())
    vect.fit(ingre_for_cv)
    cv=vect.transform(ingre_for_cv).toarray()
    #print(vect.get_feature_names())
    for idx, val in enumerate(cv[0:-1]):
        df['calc'][idx]=(val*cv[-1]).sum()/val.sum()
        #print(idx, (val*cv[-1]).sum()/val.sum())
        
    df = df.sort_values(by=['calc'], axis=0, ascending=False)
    df = df.reset_index(drop=True)
    
    return df

def show_labeled_image(image, boxes, labels=None):    
    plt.rcParams.update({'font.size': 14})
    fig, ax = plt.subplots(figsize=(20, 10))
    fig.patch.set_visible(False)
    ax.axis('off')

    # If the image is already a tensor, convert it back to a PILImage and reverse normalize it
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
        rect = patches.Rectangle(initial_pos, width, height, linewidth=2, edgecolor='cyan', facecolor='none')
        if labels:
            ax.text(box[0], box[1] - 10, '{}'.format(labels[i]), color='black')
        ax.add_patch(rect)
    fig.savefig('static/images/detection_result.jpg', dpi=100)

@app.route('/testapi',methods=["POST","GET"])
def test():
    # data = request.getJson()
    # print(data)

    im = base64.b64decode(request.get_data())
    image=Image.open(BytesIO(im))
    #모든 객체를 찍음
    ##predictions = model.predict(image)
    #모든 객체중 정확도가 가장 높은 객체 감지
    predictions = model.predict_top(image)
    labels, boxes, scores = predictions
    detection_class2=list(set(labels))
    show_labeled_image(image, boxes, labels)

    with open('static/images/detection_result.jpg','rb') as img:
        response_img = base64.b64encode(img.read())
<<<<<<< HEAD
    print(type(response_img.decode('utf-8')))

    return jsonify(response_img = response_img.decode('utf-8') , labels = labels)

@app.route('/recomandApi',methods=["POST","GET"])
def recomand():
    # try:
    labels = request.get_data().decode("utf-8")
    labelsXml = elemTree.fromstring(labels)

    items = []
    items_KOR = ""
    for item in labelsXml.findall("./item"):
    	items.append(item.text)
    	print('*'+item.text+'*')

    for i in range(len(items)):
    	if(items[i] == "chilli"):
    		items[i] ="고추"
    	elif(items[i] == "pa"):
    		items[i] ="파"
    	elif(items[i] == "potato"):
    		items[i] = "감자"
    	elif(items[i] == "pa"):
    		items[i] ="파"
    	elif(items[i] == "egg"):
    		items[i] = "계란"
    	elif(items[i] == "onion"):
    		items[i] ="양파"
    	elif(items[i] == "pork meat"):
    		items[i] = "돼지고기"

    items_KOR = " ".join(items)
    print("하하하하: " + items_KOR)
    df=recommend(items_KOR,'돼지고기')
    print("type: ",type(data.iloc[df['idx_filtering'][0]]))
    print("list_type: ",type(data.iloc[df['idx_filtering'][0]].tolist()))

    for index , i in enumerate(data.iloc[df['idx_filtering'][0]]):
        if i!='':
            print(index ,":",i)
	# except:
	# 	recomandResult = ["한가지 이상의 음식을 촬영해주세요"]

	#int64변수가 있어서 send 오류
    return jsonify(recomandResult = data.iloc[df['idx_filtering'][0]].tolist())
=======

    return response_img


@app.route('/testModel',methods=["POST","GET"])
def test2():
    

    return "성공"

<<<<<<< HEAD
@app.route('/testjson')
def json():
    # flask 에서 기본적으로 제공하는 jsonify함수를 통해 값을 json형태로 전환할 수 있다.
    
    return jsonify(name="JKS")
=======
# @app.route('/testjson')
# def json():
#     # flask 에서 기본적으로 제공하는 jsonify함수를 통해 값을 json형태로 전환할 수 있다.
#     print(jsonify(name='JKS'))
#     return jsonify(name='JKS')
>>>>>>> 7e4921b43e106ec000075a8d78b420b3fffc64c9
>>>>>>> de88b8c3a223e1a10bf833309aec7c0e5e92f6a1


if __name__ == '__main__':
    labels = ['chilli', 'egg', 'pork meat', 'potato', 'pa', 'onion']
    vectorize = HashingVectorizer()
    data = pd.read_csv('static/recipeData/crawling_200407.csv')
    data = data.fillna(0)
    data["id"] = data['id'].astype("float")

    ingre = data['ingre_main_oneline']
    ingre = np.array(ingre.tolist())
    model = core.Model.load('static/model/ingredients_weights_ver01_0326.pth', labels)
<<<<<<< HEAD
    #load model
    with open('static/model/hv.pkl', 'rb') as f:
        X = pickle.load(f)
    app.run(debug=True , host='0.0.0.0')
=======
<<<<<<< HEAD
    app.run(debug=True)
=======
    app.run(debug=True , host='0.0.0.0')
>>>>>>> 7e4921b43e106ec000075a8d78b420b3fffc64c9
>>>>>>> de88b8c3a223e1a10bf833309aec7c0e5e92f6a1
