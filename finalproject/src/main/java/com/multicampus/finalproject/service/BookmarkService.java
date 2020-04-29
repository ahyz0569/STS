package com.multicampus.finalproject.service;

import java.util.ArrayList;

import com.multicampus.finalproject.model.BookmarkVO;
import com.multicampus.finalproject.repository.BookmarkMapper;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class BookmarkService {
    
    @Autowired
    BookmarkMapper bookmarkMapper;

    public void insertBookmark(BookmarkVO bookmarkVO){
        bookmarkMapper.insertBookmark(bookmarkVO);
    }
    public BookmarkVO selectBookmark(BookmarkVO bookmarkVO){
        return bookmarkMapper.selectBookmark(bookmarkVO);
    }
    public void deleteBookmark(BookmarkVO bookmarkVO){
        bookmarkMapper.deleteBookmark(bookmarkVO);
    }
    public ArrayList<Integer> loadBookmark(String userID){
        return bookmarkMapper.loadBookmark(userID);
    }
    public int isBookmark(String userID , int recipeID){
        return bookmarkMapper.isBookmark(userID, recipeID);
    }
}