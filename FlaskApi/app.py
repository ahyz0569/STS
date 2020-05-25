from flask import Flask, jsonify, escape, request, render_template

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, HashingVectorizer
from sklearn.metrics.pairwise import linear_kernel
from PIL import Image
from io import BytesIO
from torchvision import transforms
from detecto import core, utils, visualize
from sqlalchemy import create_engine


import pandas as pd
import xml.etree.ElementTree as elemTree
import mysql.connector
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



# def recommend(ingre_input, main):
#     srch_vector = vectorize.transform([ingre_input])
#     cosine_similar = linear_kernel(srch_vector, X).flatten()
#     rank_idx = cosine_similar.argsort()[::-1]
#     count = 0
#     idx_filtering = []
#     for i in rank_idx:
#         if cosine_similar[i] > 0:
#             if main in ingre[i]:
#                 # ingre_for_cv.append(ingre[i])
#                 idx_filtering.append(i)
#                 count += 1
#                 if count > 100:
#                     break

#     df = pd.DataFrame(ingre[idx_filtering], columns=['ingre'])
#     df['idx_filtering'] = idx_filtering
#     df['calc'] = 0.

#     ingre_for_cv = df['ingre'].tolist()
#     ingre_for_cv.append(ingre_input)

#     vect = CountVectorizer(min_df=0, tokenizer=lambda x: x.split())
#     vect.fit(ingre_for_cv)
#     cv = vect.transform(ingre_for_cv).toarray()
#     # print(vect.get_feature_names())
#     for idx, val in enumerate(cv[0:-1]):
#         df['calc'][idx] = (val * cv[-1]).sum() / val.sum()
#         # print(idx, (val*cv[-1]).sum()/val.sum())

#     df = df.sort_values(by=['calc'], axis=0, ascending=False)
#     df = df.reset_index(drop=True)

#     return df
def recommend(ingre_input):
    srch_vector = vectorize.transform([ingre_input])
    cosine_similar = linear_kernel(srch_vector, X).flatten()
    rank_idx = cosine_similar.argsort()[::-1]
    idx_filtering = rank_idx[0:101]
    df = pd.DataFrame(ingre[idx_filtering], columns=['ingre'])
    df['idx_filtering'] = idx_filtering
    df['calc'] = 0.
    df['len'] = 0.

    ingre_for_cv = df['ingre'].tolist()
    ingre_for_cv.append(ingre_input)

    vect = CountVectorizer(min_df=0, tokenizer=lambda x: x.split())
    vect.fit(ingre_for_cv)
    cv = vect.transform(ingre_for_cv).toarray()
    # print(vect.get_feature_names())
    for idx, val in enumerate(cv[0:-1]):
        df['calc'][idx] = (val * cv[-1]).sum() / val.sum()
        df['len'][idx] = len(df['ingre'][idx].replace('  ',' ').split(' '))
        # print(idx, (val*cv[-1]).sum()/val.sum())

    df = df.sort_values(by=['calc'], axis=0, ascending=False)
    df1 = df[df['calc']>=0.7]
    df1 = df1.sort_values(by=['calc','len'],axis=0,ascending=False)
    df2 = df[df['calc']<0.7]
    df2 = df2.sort_values(by=['calc','len'],axis=0,ascending=[False,True])
    df = pd.concat([df1,df2])
    df = df.reset_index(drop=True)

    return df

def show_labeled_image(image, boxes, labels=None, scores=None):
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
        rect = patches.Rectangle(initial_pos, width, height, linewidth=2.5, edgecolor='r', facecolor='none')
        if labels:
            ax.text(box[0] + 20, box[1] + 50, '{}'.format(labels[i]), color='r')
        ax.add_patch(rect)
    fig.savefig('static/images/detection_result.jpg', dpi=100)


# 식재료 이미지를 요청데이터로 받아와
# Detection모델을 실행하는 route
@app.route('/groceryDetection', methods=["POST", "GET"])
def groceryDetection():
    # request.get_data()를 통해 요청 데이터를 받아온다.
    # base64로 encoding한다.
    im = base64.b64decode(request.get_data())
    image = Image.open(BytesIO(im))

    # 모든 객체를 찍음
    ##predictions = model.predict(image)

    # 모든 객체중 정확도가 가장 높은 객체 감지
    predictions = model.predict_top(image)
    labels, boxes, scores = predictions
    show_labeled_image(image, boxes, labels, scores)

    # detection 결과 이미지를 불러와 base64로 encoding한다.
    with open('static/images/detection_result.jpg', 'rb') as img:
        response_img = base64.b64encode(img.read())
    print(type(response_img.decode('utf-8')))

    # json형태로 detection결과 이미지, 찾은 식재료 목록을 반환한다.
    return jsonify(response_img=response_img.decode('utf-8'), labels=labels)


# 요청데이터로 식재료 목록을 받는다.
# 식재료목록과 연관성이 높은 레시피를 반환한다.
@app.route('/findRecipeList', methods=["POST", "GET"])
def findRecipeList():
    labels = request.get_data().decode("utf-8")
    
    # 요청과 함께 넘어온 식재료 목록을 string형태로 받는다.
    labelsXml = elemTree.fromstring(labels)

    items = []
    items_KOR = ""

    for item in labelsXml.findall("./item"):
        items.append(item.text)
        print('*' + item.text + '*')

    for i in range(len(items)):
        if (items[i] == "chilli"):
            items[i] = "고추"
        elif (items[i] == "egg"):
            items[i] = "계란"
        elif (items[i] == "pork meat"):
            items[i] = "돼지고기"
        elif (items[i] == "potato"):
            items[i] = "감자"
        elif (items[i] == "pa"):
            items[i] = "파"
        elif (items[i] == "onion"):
            items[i] = "양파"
        elif (items[i] == "carrot"):
            items[i] = "당근"
        elif (items[i] == "cucumber"):
            items[i] = "오이"

    items_KOR = " ".join(items)
    # 앞서 정의한 recommend 함수 실행
    # df=recommend(items_KOR,'돼지고기')
    df=recommend(items_KOR)
    
    responseData = []
    # 연관성높은 순으로 100가지의 recipeId를 추려낸다.
    for i in range(100):
        responseData.append(data.iloc[df['idx_filtering'][i]]['id'])
    
    for col in df.columns:
        print(df[col].dtypes)
    
    # 연관성높은 레시피의 recipeId 100개를 json형태로 반환한다.
    return jsonify(recomandResult = responseData)


# lazy Loading을 하여 모델을 불러오는 시간을 단축한다.
if __name__ == '__main__':
    #현재 인식할 수 있는 식재료들
    labels = ['chilli', 'egg', 'pork meat', 'potato', 'pa', 'onion', 'carrot', 'cucumber']
    #벡터라이저 선언
    vectorize = HashingVectorizer()

    # DB와의 연동하는 부분
    # DB와의 연결을 생성
    engine = create_engine('mysql://root:1234@localhost:3307/testDB?charset=utf8', convert_unicode=True,encoding='UTF-8')
    # engine = create_engine('mysql://JKS:12345678@sts.c2yt44rkrmcp.us-east-2.rds.amazonaws.com:3306/finalproject?charset=utf8', convert_unicode=True,encoding='UTF-8')
    conn = engine.connect()
    # recipe 테이블을 읽어온다.
    data = pd.read_sql_table('recipe', conn)
    # 누락된 값을 0으로 전환
    data = data.fillna(0)
    # json형태로 반환하기 위해 int32 or int64 형태의 변수를 float로 전환
    data["id"] = data['id'].astype("float")
    data["size"] = data['size'].astype("float")
    data["time"] = data['time'].astype("float")

    ingre = data['ingre_main_oneline']
    ingre = np.array(ingre.tolist())
    # 이미지 detection 모델을 load
    model = core.Model.load('static/model/detection_weights_v3.5.pth', labels)
    # load model
    with open('static/model/hv.pkl', 'rb') as f:
        X = pickle.load(f)

    app.run(debug=True, host='0.0.0.0')
