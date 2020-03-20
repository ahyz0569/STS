package com.multicampus.finalproject.controller;
 
import java.util.List;
 
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
 
import com.multicampus.finalproject.model.UserInfo;
import com.multicampus.finalproject.service.UserInfoService;
 

// DB와 연결되는 부분은 db파일로 구분했음 db와 연동되는 jsp의 controller
@Controller
public class TestController {
 
    @Autowired
    UserInfoService userInfoService;
    
    // query라는 값과 매칭된다.
    // 그저 SQL문 실행결과를 뿌려주지만
    // model객체를 사용하면 원하는 형태로 html문과 섞어 출력할 수 있을 것 같다.
    @RequestMapping("/")
    public @ResponseBody String home(){
        return "hello world!!!";
    }
    
    @RequestMapping("/query")
    public @ResponseBody List<UserInfo> query() throws Exception{
        return userInfoService.getAll();
    }
    
 
}
