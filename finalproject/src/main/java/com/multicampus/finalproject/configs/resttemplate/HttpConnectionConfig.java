package com.multicampus.finalproject.configs.resttemplate;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.client.HttpComponentsClientHttpRequestFactory;
import org.springframework.web.client.RestTemplate;
import org.apache.http.client.HttpClient;
import org.apache.http.impl.client.HttpClientBuilder;
@Configuration
public class HttpConnectionConfig{

    @Bean
    public RestTemplate getCustomRestTemplate(){
<<<<<<< HEAD:finalproject/src/main/java/com/multicampus/finalproject/configs/http/HttpConnectionConfig.java
        HttpComponentsClientHttpRequestFactory httpRequestFactory 
                        = new HttpComponentsClientHttpRequestFactory();
        httpRequestFactory.setConnectTimeout(5000);
        httpRequestFactory.setReadTimeout(5000);

=======
        HttpComponentsClientHttpRequestFactory httpRequestFactory = new HttpComponentsClientHttpRequestFactory();
        httpRequestFactory.setConnectTimeout(10000000);
        httpRequestFactory.setReadTimeout(10000000);
        //connetPool 설정
>>>>>>> 7e4921b43e106ec000075a8d78b420b3fffc64c9:finalproject/src/main/java/com/multicampus/finalproject/configs/resttemplate/HttpConnectionConfig.java
        HttpClient httpClient = HttpClientBuilder.create()
                                //connectPool 갯수
                                .setMaxConnTotal(200)
                                //ip,port 하나당 연결 제한 갯수
                                .setMaxConnPerRoute(20)
                                .build();
        
        httpRequestFactory.setHttpClient(httpClient);
        return new RestTemplate(httpRequestFactory);
    }
}


