<<<<<<< HEAD
// package com.multicampus.finalproject.controller;
 
// import java.util.List;
 
// import org.springframework.beans.factory.annotation.Autowired;
// import org.springframework.stereotype.Controller;
// import org.springframework.web.bind.annotation.RequestMapping;
// import org.springframework.web.bind.annotation.ResponseBody;
 
// import com.multicampus.finalproject.model.UserInfo;
// import com.multicampus.finalproject.service.UserInfoService;
 

// // DB와 연결되는 부분은 db파일로 구분했음 db와 연동되는 jsp의 controller
// @Controller
// public class TestController {
 
//     @Autowired
//     UserInfoService userInfoService;
    
//     // query라는 값과 매칭된다.
//     // 그저 SQL문 실행결과를 뿌려주지만
//     // model객체를 사용하면 원하는 형태로 html문과 섞어 출력할 수 있을 것 같다.
//     @RequestMapping("/")
//     public @ResponseBody String home(){
//         return "hello world!!!";
//     }
    
//     @RequestMapping("/query")
//     public @ResponseBody List<UserInfo> query() throws Exception{
//         return userInfoService.getAll();
//     }
    
 
// }
=======
package com.multicampus.finalproject.controller;

import java.io.IOException;
import java.util.List;

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
        for(int i=0;i<10;i++){
            System.out.print("이미지는 이거임!!"+img);
        }
        byte[] imgtext;
        String imgtext2;
        try{
            imgtext = Base64.encodeBase64(img.getBytes());
            imgtext2 = new String(imgtext);
            // mav.addObject("uploadedImage",imgtext2);

            StringBuilder sb = new StringBuilder();
            sb.append("data:image/jpg;base64,");
            sb.append(imgtext2);
            model.addAttribute("uploadedImage",sb);
            ResponseEntity<String> a=restTemplateService.addData(imgtext2);
            System.out.print(a.getBody());
        }
        catch(IOException except){
            System.out.println("파일이 이상함!");
        }
        
        
        return "upload";
    }
}
>>>>>>> origin/backend_version
