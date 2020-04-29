package com.multicampus.finalproject.repository;

import java.util.ArrayList;

import com.multicampus.finalproject.model.BookmarkVO;

public interface BookmarkMapper {
    public void insertBookmark(BookmarkVO bookmarkVO);
    
    public void deleteBookmark(BookmarkVO bookmarkVO);

    public BookmarkVO selectBookmark(BookmarkVO bookmarkVO);

    public ArrayList<Integer> loadBookmark(String userID);
    
    public int isBookmark(String userID , int recipeID);
}