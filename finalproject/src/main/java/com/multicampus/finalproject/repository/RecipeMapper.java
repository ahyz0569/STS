package com.multicampus.finalproject.repository;

import java.util.ArrayList;
import java.util.List;


import com.multicampus.finalproject.model.RecommandListVO;
 

public interface RecipeMapper {
    public List<RecommandListVO> readRecipeList(ArrayList<Integer> idList);

    public RecommandListVO readRecipe(int recipeId);

    public int getSearchPageNum(String keyword);

    public List<RecommandListVO> searchRecipeList(int page, String keyword);
}