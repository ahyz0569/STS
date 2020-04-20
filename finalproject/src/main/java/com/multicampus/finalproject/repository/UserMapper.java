package com.multicampus.finalproject.repository;
 
<<<<<<< HEAD
import java.util.ArrayList;
import java.util.List;

import com.multicampus.finalproject.model.BookmarkVO;
import com.multicampus.finalproject.model.RecommandListVO;
=======
import java.util.List;
>>>>>>> d5540d74119adea1e212dc64b4f249ed3da30205
 
import com.multicampus.finalproject.model.UserInfo;



// Mapper이다. 그저 interface로 정의한다.
// interface로 정의된 mapper는 service와의 의존성이 있다.
<<<<<<< HEAD
=======

>>>>>>> d5540d74119adea1e212dc64b4f249ed3da30205
public interface UserMapper {
 
    public List<UserInfo> getAll() throws Exception;

    public UserInfo readUser(String username);
 
    public List<String> readAuthority(String username);

    public void insertMember(UserInfo userInfo);

    public void insertAuthority(String username);
<<<<<<< HEAD

    public void insertBookmark(BookmarkVO bookmarkVO);
    
    public void deleteBookmark(BookmarkVO bookmarkVO);

    public BookmarkVO selectBookmark(BookmarkVO bookmarkVO);
    
    public List<RecommandListVO> readRecipeList(ArrayList<Integer> idList);
=======
>>>>>>> d5540d74119adea1e212dc64b4f249ed3da30205
}
