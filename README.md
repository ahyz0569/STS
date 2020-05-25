# 식자재 분석 기반 레시피 큐레이팅 서비스

## Recipe Curating Service

---

### 1. 프로젝트 정보

#### 프로젝트 기간: 

 - 2020.03.16 ~ 2020.04.29

 #### 팀 구성원: 

 - 6 people (Front-end: 1 person, Back-end: 2 people, Data analysis: 3 people)

 #### 사용기술:

 - FE: HTML, CSS, Vanilla JS

   BE: Spring, Java, Tomcat, Flask, Thymeleaf

   DA: Python3, Pytorch

#### 목적 및 기능:

- 식재료 이미지를 분석해 사용자 맞춤 레시피를 제공한다. 가지고 있는 식자재를 휴대폰으로 촬영하면, Object Detection 모델을 통해 어떤 식자재가 있는지 분석하고, 이를 토대로 요리 레시피를 추천한다.

  북마크, 레시피 검색 등의 기능 또한 구현되어 있다.

 #### 모델 설정 방법:

 - 해당 링크로 접속 후 detection_weights_v3.5.pth 파일을 받은 후 FlaskApi >> static >> model 파일에 넣어야 재료 분석이 정상적으로 실행된다.

 #### Train model by Detecto

| Model  | download                                                     |
| ------ | ------------------------------------------------------------ |
| Faster | [model](https://drive.google.com/file/d/1-EStD1O7hWwM3bYvEnaehOPGUSOIB5KA/view?usp=sharing) |

 #### Train model by Detectron2

| Model  | Backbone | lr sched | AP     | AP50   | AP75   | APm    | API    | download                                                     |
| ------ | -------- | -------- | ------ | ------ | ------ | ------ | ------ | ------------------------------------------------------------ |
| Faster | R50-FPN  | 1x       | 29.292 | 53.561 | 28.624 | 28.609 | 28.191 | [model](https://drive.google.com/file/d/1-cXc9NXYjyDj1OfCD2NTpv4F5luPTAIg/view?usp=sharing) \| [metrics](https://drive.google.com/file/d/18Mk98Keko5wYw9mZj3Xou_SEyYSO00QL/view?usp=sharing) |



