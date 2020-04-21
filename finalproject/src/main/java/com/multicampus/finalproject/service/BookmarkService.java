package com.multicampus.finalproject.service;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import com.multicampus.finalproject.model.BookmarkVO;
import com.multicampus.finalproject.model.RecipeIDList;
import com.multicampus.finalproject.repository.UserMapper;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class BookmarkService {
    
    @Autowired
    UserMapper userMapper;

    public void insertBookmark(BookmarkVO bookmarkVO){
        userMapper.insertBookmark(bookmarkVO);
    }
    public BookmarkVO selectBookmark(BookmarkVO bookmarkVO){
        return userMapper.selectBookmark(bookmarkVO);
    }
    public void deleteBookmark(BookmarkVO bookmarkVO){
        userMapper.deleteBookmark(bookmarkVO);
    }
    public List<RecipeIDList> loadBookmark(String userID){
        return userMapper.loadBookmark(userID);
    }
    // public int[] loadBookmark(String userID){
    //     return userMapper.loadBookmark(userID);
    // }
    // public ArrayList<Float> loadBookmark(String userID){
    //     return userMapper.loadBookmark(userID);
    // }
    // public HashMap<String, Integer> loadBookmark(String userID){
    //     return userMapper.loadBookmark(userID);
    // }
}