package com.multicampus.finalproject.model;

import java.util.ArrayList;

import javax.xml.bind.annotation.XmlElement;

import lombok.Getter;


// Flask API 에서 반환하는 이미지와 label에 대한 데이터를 담는 DAO
@Getter
public class JsonVO {
    @XmlElement(name="response_img")
    private String response_img="default";
    @XmlElement(name="labels")
    private ArrayList<String> labels;
}