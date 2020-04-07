package com.multicampus.finalproject.model;

import javax.xml.bind.annotation.XmlElement;

import lombok.Getter;
@Getter
public class JsonVO {
    @XmlElement(name="name")
    private String name="default";
}