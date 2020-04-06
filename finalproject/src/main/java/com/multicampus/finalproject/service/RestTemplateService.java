package com.multicampus.finalproject.service;

<<<<<<< HEAD
import com.multicampus.finalproject.repository.RestTemplateUtil;

import org.springframework.stereotype.Service;

import lombok.extern.slf4j.Slf4j;

@Service
@Slf4j
public class RestTemplateService {
    public String getStringData(){
        return RestTemplateUtil.getStringResponse();
    }
=======
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import com.multicampus.finalproject.util.RestTemplateUtil;

import lombok.extern.slf4j.Slf4j;

@Service
//@Slf4j
public class RestTemplateService {

    // public XmlVo getXmlData() {
    //     return RestTemplateUtil.getXmlResponse();
    // }

    // public JsonVo getJsonData() {
    //     return RestTemplateUtil.getJsonRsponse();
    // }

    // public ResponseEntity<String> getEntity(String key) {
    //     return RestTemplateUtil.getResponseEntity(key);
    // }
    
    public ResponseEntity<String> addData(String imgString) {
        return RestTemplateUtil.post(imgString);
    }

>>>>>>> origin/backend_version
}