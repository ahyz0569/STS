package com.multicampus.finalproject.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class TestController{
    @RequestMapping("/")
    public String home(){
        return "home";
    }
}