package com.multicampus.finalproject.repository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;

@Component
public class RestTemplateUtil {
    //private로 지정했기 때문에 Autowired는 생성자에서 생성 한다
    private static RestTemplate restTemplate;

    @Autowired
    public RestTemplateUtil(RestTemplate restTemplate){
        this.restTemplate = restTemplate;
    }

    //외부 api의 요청과 응답 처리를 해주는 실직적인 코드
    public static String getStringResponse(){
        System.out.println("1");
        //restTemplate 라이브러리의 getForObject를 사용해서 첫번째 매개변수로는 외부 api url , 두번째 매개변수로는 return 타입을 작성한다. 
        String content = restTemplate.getForObject("http://52.79.151.210:5000/json", String.class);
        System.out.println("2");
        //return 으로 String 타입의 conotent를 반환한다.
        return content;
    }
}