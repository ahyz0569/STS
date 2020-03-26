package com.multicampus.finalproject.service;

import com.multicampus.finalproject.repository.RestTemplateUtil;

import org.springframework.stereotype.Service;

import lombok.extern.slf4j.Slf4j;

@Service
@Slf4j
public class RestTemplateService {
    public String getStringData(){
        return RestTemplateUtil.getStringResponse();
    }
}