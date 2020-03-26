package com.multicampus.finalproject.controller;

import java.util.List;

import com.multicampus.finalproject.model.UserInfo;
import com.multicampus.finalproject.service.UserInfoService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class TestController{

    @Autowired
    UserInfoService userInfoService;


    @RequestMapping("/")
    public String home(){
        return "home";
    }

    //Database연동 성공 확인하기
    @RequestMapping("/query")
    public @ResponseBody List<UserInfo> query() throws Exception{
        return userInfoService.getAll();
    }
}