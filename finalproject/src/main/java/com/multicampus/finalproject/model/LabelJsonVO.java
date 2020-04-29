package com.multicampus.finalproject.model;

import java.util.ArrayList;

import javax.xml.bind.annotation.XmlElement;

import lombok.Getter;


@Getter
public class LabelJsonVO {
    @XmlElement(name="recomandResult")
    private ArrayList<Integer> recomandResult;
}