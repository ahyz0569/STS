const mainContents = document.getElementById("main__contents");
const bookmarkModalContent = document.getElementById("bookmark-modal-content");
const bookmarkModalOpenButton = document.getElementById("bookmark");
const bookMarkOverlay = document.querySelector(".modal__overlay");
const bookmarkModalCloseBtn = document.getElementById("bookmark-modal__close");

let i = "";
let frag = document.createDocumentFragment();


// 레시피 리스트 우측 사진 별표 모양 북마크 기능
function addBookmark(event) {
  event.stopPropagation();
  const addBm = event.target;
  if (addBm.getAttribute("src") == "images/bm-logo.png") {
    addBm.setAttribute("src", "images/bm-logo-checked.png");
  } else if (addBm.getAttribute("src") == "images/bm-logo-checked.png") {
    addBm.setAttribute("src", "images/bm-logo.png");
  }
}


/*
for (i in recipeList) {
  //메뉴 리스트 전체적인 틀 만들기
  let menuList = document.createElement("li");
  menuList.className = "menu__list";

  //리스트 안에 각각의 레시피 틀 만들기
  let aboutMenu = document.createElement("div");
  aboutMenu.className = "about__menu";

  //제목 
  let recipeTitle = document.createElement("h1");
  recipeTitle.innerHTML = recipeList[i].title;

  //주재료
  let recipeMain = document.createElement("span");
  recipeMain.id = "recipe-main-ingredients";
  recipeMain.innerHTML = `<span style="font-weight:bold";>ㅇ주재료:<br></span> ${recipeList[i].main.replace("[", "").replace("]", "")}`;

  //부재료
  let recipeMinor = document.createElement("span");
  recipeMinor.id = "recipe-minor-ingredients";
  recipeMinor.innerHTML = `<span style="font-weight:bold";>ㅇ부재료:<br></span> ${recipeList[i].minor.replace("[", "").replace("]", "")}`;

  //레시피 리스트 우측에 완성 이미지 틀, 내용
  let recipeImgContainer = document.createElement("div")
  recipeImgContainer.className = "recipe-img-container"
  let recipeImgCover = document.createElement("div")
  recipeImgCover.className = "recipe-img-cover"
  let recipeImg = document.createElement("img");
  recipeImgContainer.appendChild(recipeImgCover);
  recipeImgCover.appendChild(recipeImg)
  recipeImg.src = recipeList[i].img_complete;
  recipeImg.className = "menu__list-image";

  //북마크 별표 틀 만들기
  let bmImgCover = document.createElement("div");
  bmImgCover.className = "bm-img-cover"
  let bmImg = document.createElement("img");
  bmImgCover.appendChild(bmImg);
  bmImg.className = "bookmark-image"
  bmImg.src = "images/bm-logo.png";
  bmImg.addEventListener("click", addBookmark);
  recipeImgContainer.appendChild(bmImgCover);

  //함수 안에서 생성한 각각의 틀을 전체를 포함하는 틀에 추가
  menuList.appendChild(aboutMenu);
  aboutMenu.appendChild(recipeTitle);
  aboutMenu.appendChild(recipeMain);
  aboutMenu.appendChild(recipeMinor);
  menuList.appendChild(recipeImgContainer);

  //만든 전체적인 HTML요소들을 가상 공간에 저장
  frag.appendChild(menuList);

  //가상 공간에 저장된 것을 한번에 페이지에 뿌린다
  bookmarkModalContent.appendChild(frag);

  //리스트에서 메뉴 클릭시 레시피결과 페이지로 이동
  menuList.href = "/recipe" + "/" + recipeList[i].id.toString();
  menuList.addEventListener("click", function event() {
    location.href = this.href;
  });
}
*/



// ++++++++++++++++현진아 아래 함수가 클릭하면 모달창 열리는 함수야. 위에 있는 for함수 저걸 아래 함수에 아마 넣어야할듯?
// 그래야 내용이 들어갈거야




// 북마크 클릭 시 북마크한 레시피가 저장되어 있는 모달창을 띄움 
const bookmarkOpenModal = () => {
  // 왼쪽 네비바에서 북마크 클릭 시 네비바 닫고 북마크 모달 열기
  closeNav();

  let bookmarkContents = document.createElement("div");
  bookmarkContents.className = "bookmark__modal";

  let bookmarkCloseModalOverlay = document.createElement("div");
  bookmarkCloseModalOverlay.className = "modal__overlay";
  bookmarkCloseModalOverlay.setAttribute("onclick", "bookmarkCloseModal()")

  let bmc = document.createElement("div");
  bmc.className = "bookmark-modal-content";

  let bookmarkCloseModal = document.createElement("button");
  bookmarkCloseModal.innerHTML = "X";
  bookmarkCloseModal.id = "bookmark-modal__close";
  bookmarkCloseModal.setAttribute("onclick", "bookmarkCloseModal()")

  bmc.appendChild(bookmarkCloseModal);
  bookmarkContents.appendChild(bookmarkCloseModalOverlay);
  bookmarkContents.appendChild(bmc);

  frag.appendChild(bookmarkContents)
  mainContents.appendChild(frag);
};


//오버레이, X버튼 누르면 북마크 닫기
const bookmarkCloseModal = () => {
  let bookmarkContents = document.querySelector(".bookmark__modal");
  mainContents.removeChild(bookmarkContents);
};