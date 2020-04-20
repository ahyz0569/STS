package com.multicampus.finalproject.model;

import java.util.ArrayList;
import java.util.List;

import javax.xml.bind.annotation.XmlElement;

import lombok.Getter;
@Getter
public class LabelJsonVO {
    @XmlElement(name="recomandResult")
<<<<<<< HEAD
    private ArrayList<Integer> recomandResult;
=======
    private ArrayList<String> recomandResult;
>>>>>>> d5540d74119adea1e212dc64b4f249ed3da30205
}