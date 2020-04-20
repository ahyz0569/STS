const menuLists = document.getElementById("menu__lists");

let i = "";
let frag = document.createDocumentFragment();



for (i in recipeList) {
  // console.log(i);
  let menuList = document.createElement("li");
  menuList.className = "menu__list";
  let aboutMenu = document.createElement("div");
  aboutMenu.className = "about__menu";
  let recipeTitle = document.createElement("h1");
  recipeTitle.innerHTML = recipeList[i].title;
  let recipeMain = document.createElement("span");
  recipeMain.id = "recipe-main-ingredients"
  recipeMain.innerHTML = `<span style="font-weight:bold";>ㅇ주재료:</span> ${recipeList[i].main}`;
  let recipeMinor = document.createElement("span");
  recipeMinor.id = "recipe-minor-ingredients"
  recipeMinor.innerHTML = `<span style="font-weight:bold";>ㅇ부재료:</span> ${recipeList[i].minor}`;
  let recipeImg = document.createElement("img");
  recipeImg.className = "menu__list-image";
  recipeImg.src = recipeList[i].img_complete;;


  menuList.appendChild(aboutMenu);
  aboutMenu.appendChild(recipeTitle);
  aboutMenu.appendChild(recipeMain);
  aboutMenu.appendChild(recipeMinor);
  menuList.appendChild(recipeImg);


  frag.appendChild(menuList);
  menuLists.appendChild(frag);
}