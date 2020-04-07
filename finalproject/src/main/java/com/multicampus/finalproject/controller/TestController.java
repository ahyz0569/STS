package com.multicampus.finalproject.controller;

import java.io.IOException;
import java.util.List;

import com.multicampus.finalproject.model.JsonVO;
import com.multicampus.finalproject.model.UserInfo;
import com.multicampus.finalproject.service.RestTemplateService;
import com.multicampus.finalproject.service.UserInfoService;

import org.apache.commons.codec.binary.Base64;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.multipart.MultipartFile;

@Controller
public class TestController{

    @Autowired
    UserInfoService userInfoService;

    @Autowired
    RestTemplateService restTemplateService;

    
    @RequestMapping("/")
    public String home(){
        return "home";
    }

    //Database연동 성공 확인하기
    @RequestMapping("/query")
    public @ResponseBody List<UserInfo> query() throws Exception{
        return userInfoService.getAll();
    }

    @RequestMapping("/testimg")
    public String testimg(){
        
        return "testimg";
    }


    @RequestMapping("/upload")
    public String upload(Model model,@RequestParam("file") MultipartFile img){
       
        byte[] imgtext;
        String imgtext2;
        try{
            imgtext = Base64.encodeBase64(img.getBytes());
            imgtext2 = new String(imgtext);

            System.out.println(imgtext2.length());
            ResponseEntity<String> a=restTemplateService.addData(imgtext2);

            StringBuilder sb = new StringBuilder();
            sb.append("data:image/jpg;base64,");
            sb.append(a.getBody());
            model.addAttribute("uploadedImage",sb);

        }
        catch(IOException except){
            System.out.println("파일이 이상함!");
        }
        
        
        return "upload";
    }

    @RequestMapping("/testJson")
    @ResponseBody
    public String testJson(){
        ResponseEntity<JsonVO> a = restTemplateService.getJsonData();
        System.out.println(a.getBody().getName());
        System.out.println(a.getStatusCode());
        return a.getBody().getName();
    }
}