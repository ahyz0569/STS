## Library import
# Flask
from flask import Flask, jsonify, escape, request, render_template

# Vectorizer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, HashingVectorizer
from sklearn.metrics.pairwise import linear_kernel

# For using detectron2 model
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.data import MetadataCatalog
from detectron2.data.datasets import register_coco_instances
from detectron2.utils.visualizer import Visualizer, ColorMode
import cv2
import requests

from PIL import Image
from io import BytesIO

# SQL
from sqlalchemy import create_engine
# import mysql.connector

# common library
import xml.etree.ElementTree as elemTree
import pandas as pd
import numpy as np
import csv
import pickle
import base64
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
def recommend(ingre_input, main):
    srch_vector = vectorize.transform([ingre_input])
    cosine_similar = linear_kernel(srch_vector, X).flatten()
    rank_idx = cosine_similar.argsort()[::-1]
    count = 0
    idx_filtering = []
    for i in rank_idx:
        if cosine_similar[i] > 0:
            if main in ingre[i]:
                # ingre_for_cv.append(ingre[i])
                idx_filtering.append(i)
                count += 1
                if count > 100:
                    break

    df = pd.DataFrame(ingre[idx_filtering], columns=['ingre'])
    df['idx_filtering'] = idx_filtering
    df['calc'] = 0.

    ingre_for_cv = df['ingre'].tolist()
    ingre_for_cv.append(ingre_input)

    vect = CountVectorizer(min_df=0, tokenizer=lambda x: x.split())
    vect.fit(ingre_for_cv)
    cv = vect.transform(ingre_for_cv).toarray()
    # print(vect.get_feature_names())
    for idx, val in enumerate(cv[0:-1]):
        df['calc'][idx] = (val * cv[-1]).sum() / val.sum()
        # print(idx, (val*cv[-1]).sum()/val.sum())

    df = df.sort_values(by=['calc'], axis=0, ascending=False)
    df = df.reset_index(drop=True)

    return df


# Detectron2 Model Predictor 생성 함수
def prepare_predictor():
    # create config
    cfg = get_cfg()
    
    # cfgFile 경로 설정
    cfgFile = "static/model/custom_config.yaml"
    cfg.merge_from_file(cfgFile)
    
    ## customize config options
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.7  # set threshold for this model
    
    # 이것도 학습시킨 모델 경로로 바꾸어 주어야함
    cfg.MODEL.WEIGHTS = "static/model/model_final.pth"
    cfg.MODEL.DEVICE = "cpu" # we use a CPU Detectron copy
    
    ingre_val_metadata = MetadataCatalog.get("my_dataset_val2", )
    
    # Metadata 생성을 위한 Data instance 생성
    register_coco_instances("my_dataset_val_test", {},
                        "static/model/output_val.json",
                        '')
    ingre_val_metadata = MetadataCatalog.get("my_dataset_val_test")

    # classes 형태: ['chilli', 'egg', 'porkmeat', 'potato', 'pa', 'onion', 'carrot', 'cucumber']
    classes = MetadataCatalog.get(cfg.DATASETS.TEST[0]).thing_classes    

    predictor = DefaultPredictor(cfg)
    print("Predictor has been initialized.")
    return (predictor, classes, ingre_val_metadata)


@app.route('/testapi', methods=["POST", "GET"])
def test():
    # data = request.getJson()
    # print(data)

    im = base64.b64decode(request.get_data())
    image = Image.open(BytesIO(im))

    # predictor 실행
    outputs = predictor(image)

    # predictor 실행 확인
    print(outputs)
    
    instances = outputs["instances"]    
    pred_classes_idx = instances.get_fields()["pred_classes"].tolist()
    # pred_boxes = instances.get_fields()["pred_boxes"].tensor.tolist()
    # scores = instances.get_fields()["scores"].tolist()

    v = Visualizer(image[:, :, ::-1],
                   metadata=ingre_val_metadata, 
                   scale=0.8
    )
    
    # 재료 리스트를 한글로 변환하기 위한 dictionary 생성
    # classes = 'chilli', 'egg', 'porkmeat', 'potato', 'pa', 'onion', 'carrot', 'cucumber'
    ingre_dict ={0: '고추',
                 1: '계란',
                 2: '돼지고기',
                 3: '감자',
                 4: '파',
                 5: '양파',
                 6: '당근',
                 7: '오이'
                }
    
    # detect된 재료 class의 index 저장
    pred_classes_idx = outputs["instances"].get_fields()["pred_classes"].tolist()

    # 재료 리스트(한글)을 저장하기 위한 리스트 생성
    pred_classes = []
    for idx in pred_classes_idx:
        pred_classes.append(ingre_dict[idx])

    # 감지된 재료 리스트 한글 변환 확인용
    print(pred_classes)

    # 결과 이미지 생성
    vis_output = v.draw_instance_predictions(outputs["instances"].to("cpu"))
    print(type(vis_output))
    # cv2_imshow(v.get_image()[:, :, ::-1])

    return jsonify(response_img=vis_output.decode('utf-8'), labels=pred_classes)



@app.route('/recomandApi', methods=["POST", "GET"])
def recomand():
    # try:
    labels = request.get_data().decode("utf-8")
    labelsXml = elemTree.fromstring(labels)

    items = []
    items_KOR = ""
    for item in labelsXml.findall("./item"):
        items.append(item.text)
        print('*' + item.text + '*')

    # for i in range(len(items)):
    #     if (items[i] == "chilli"):
    #         items[i] = "고추"
    #     elif (items[i] == "egg"):
    #         items[i] = "계란"
    #     elif (items[i] == "pork meat"):
    #         items[i] = "돼지고기"
    #     elif (items[i] == "potato"):
    #         items[i] = "감자"
    #     elif (items[i] == "pa"):
    #         items[i] = "파"
    #     elif (items[i] == "onion"):
    #         items[i] = "양파"
    #     elif (items[i] == "carrot"):
    #         items[i] = "당근"
    #     elif (items[i] == "cucumber"):
    #         items[i] = "오이"

    items_KOR = " ".join(items)
    # print("하하하하: " + items_KOR)
    df=recommend(items_KOR,'돼지고기')
    
    responseData = []
    for i in range(100):
        responseData.append(data.iloc[df['idx_filtering'][i]]['id'])
    
    # print("type: ",type(data.iloc[df['idx_filtering'][0]]))
    # print("list_type: ",type(data.iloc[df['idx_filtering'][0]].tolist()))

    # for index , i in enumerate(data.iloc[df['idx_filtering'][0]]):
    #     if i!='':
    #         print(index ,":",i)
	# except:
	# 	recomandResult = ["한가지 이상의 음식을 촬영해주세요"]
    for col in df.columns:
        print(df[col].dtypes)
	#int64변수가 있어서 send 오류
    
    print(responseData)
    return jsonify(recomandResult = responseData)

    ###############################
    # print("하하하하: " + items_KOR)
    # df = recommend(items_KOR, '돼지고기')
    # print("type: ", type(data.iloc[df['idx_filtering'][0]]))
    # print("list_type: ", type(data.iloc[df['idx_filtering'][0]].tolist()))

    # for index, i in enumerate(data.iloc[df['idx_filtering'][0]]):
    #     if i != '':
    #         print(index, ":", i)
    # # except:
    # # 	recomandResult = ["한가지 이상의 음식을 촬영해주세요"]

    # # int64변수가 있어서 send 오류
    # return jsonify(recomandResult=data.iloc[df['idx_filtering'][0]].tolist())
    ################################

@app.route('/testModel', methods=["POST", "GET"])
def test2():
    return "성공"


@app.route('/testjson')
def json():
    # flask 에서 기본적으로 제공하는 jsonify함수를 통해 값을 json형태로 전환할 수 있다.

    return jsonify(name="JKS")


# @app.route('/testjson')
# def json():
#     # flask 에서 기본적으로 제공하는 jsonify함수를 통해 값을 json형태로 전환할 수 있다.
#     print(jsonify(name='JKS'))
#     return jsonify(name='JKS')


if __name__ == '__main__':
    labels = ['chilli', 'egg', 'pork meat', 'potato', 'pa', 'onion', 'carrot', 'cucumber']
    vectorize = HashingVectorizer()

    # detectron2 predictor 생성
    predictor, classes, ingre_val_metadata = prepare_predictor()

    engine = create_engine('mysql://root:1234@localhost:3307/testDB?charset=utf8', convert_unicode=True,encoding='UTF-8')
    # engine = create_engine('mysql://JKS:12345678@sts.c2yt44rkrmcp.us-east-2.rds.amazonaws.com:3306/finalproject?charset=utf8', convert_unicode=True,encoding='UTF-8')
    conn = engine.connect()
    data = pd.read_sql_table('recipe', conn)
    data = data.fillna(0)
    data["id"] = data['id'].astype("float")
    data["size"] = data['size'].astype("float")
    data["time"] = data['time'].astype("float")
    print(data.dtypes)

    ingre = data['ingre_main_oneline']
    ingre = np.array(ingre.tolist())
    
    # model = core.Model.load('static/model/detection_weights_v3.pth', labels)
    # load model
    with open('static/model/hv.pkl', 'rb') as f:
        X = pickle.load(f)
    app.run(debug=True, host='0.0.0.0')
