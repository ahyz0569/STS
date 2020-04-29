package com.multicampus.finalproject.service;
 
import java.util.ArrayList;
import java.util.List;
 
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
 
import com.multicampus.finalproject.model.UserInfo;
import com.multicampus.finalproject.repository.RecipeMapper;
import com.multicampus.finalproject.model.RecommandListVO;

// Service로 정의하고 Autowired를 통해 testMapper와의 의존성을 주입해준다.
@Service
public class RecipeInfoService {
 
    @Autowired
    RecipeMapper recipeMapper;

    public List<RecommandListVO> readRecipeList(ArrayList<Integer> idList){
        return recipeMapper.readRecipeList(idList);
    }
    public RecommandListVO readRecipe(int recipeId){
        return recipeMapper.readRecipe(recipeId);
    }

    public int getSearchPageNum(String keyword){
        return recipeMapper.getSearchPageNum(keyword);
    }

    public List<RecommandListVO> searchRecipeList(int page,String keyword){
        return recipeMapper.searchRecipeList(page,keyword);
    }
}
