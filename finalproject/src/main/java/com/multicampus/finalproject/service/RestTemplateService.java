package com.multicampus.finalproject.service;

import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import com.multicampus.finalproject.util.RestTemplateUtil;

import lombok.extern.slf4j.Slf4j;

import com.multicampus.finalproject.model.JsonVO;
@Service
//@Slf4j
public class RestTemplateService {

    // public XmlVo getXmlData() {
    //     return RestTemplateUtil.getXmlResponse();
    // }

    public ResponseEntity<JsonVO> getJsonData() {
        return RestTemplateUtil.getJsonRsponse();
    }

    // public ResponseEntity<String> getEntity(String key) {
    //     return RestTemplateUtil.getResponseEntity(key);
    // }
    
    public ResponseEntity<String> addData(String imgString) {
        return RestTemplateUtil.post(imgString);
    }

}