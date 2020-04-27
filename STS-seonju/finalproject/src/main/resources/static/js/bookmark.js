const mainContents = document.getElementById("main__contents");
// const bookmarkModalContent = document.querySelector("bookmark-modal-content");
// const bookmarkModalOpenButton = document.getElementById("bookmark");
// const bookMarkOverlay = document.querySelector(".modal__overlay");
// const bookmarkModalCloseBtn = document.getElementById("bookmark-modal__close");

let i = "";
let frag = document.createDocumentFragment();


// 레시피 리스트 우측 사진 별표 모양 북마크 기능
function addBookmark(event) {
  bookmarkDeleteModal();
  event.stopPropagation();
  const addBm = event.target;
  if (addBm.getAttribute("src") == "images/bm-logo.png") {
    addBm.setAttribute("src", "images/bm-logo-checked.png");
  } else if (addBm.getAttribute("src") == "images/bm-logo-checked.png") {
    addBm.setAttribute("src", "images/bm-logo.png");
  }
}




// 북마크 클릭 시 북마크한 레시피가 저장되어 있는 모달창을 띄움 
const bookmarkOpenModal = () => {
  // 왼쪽 네비바에서 북마크 클릭 시 네비바 닫고 북마크 모달 열기
  closeNav();

  let bookmarkContents = document.createElement("div");
  bookmarkContents.className = "bookmark__modal";

  let bookmarkCloseModalOverlay = document.createElement("div");
  bookmarkCloseModalOverlay.className = "modal__overlay";
  bookmarkCloseModalOverlay.setAttribute("onclick", "bookmarkCloseModal()")

  let bmc = document.createElement("ul");
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

  ///////////////////////////////이부분은 안건들어도 댐!!!!!!
  ///////////////////////////////이부분은 안건들어도 댐!!!!!!
  ///////////////////////////////이부분은 안건들어도 댐!!!!!!
  ///////////////////////////////이부분은 안건들어도 댐!!!!!!

  const odj = {
    //권한 설정이 되어 있을때만 fetch실행
    credentials: 'same-origin'
  };
  fetch("http://localhost:8080/loadBookmark", odj)
    .then(res => {
      //정상 응답이 왔을 때 로직 실행
      if (res.status == 200) {
        res
          .json()
          // .then(json => newDiv.innerHTML = json.recommandList)
          // .then(json => printJsonList(json.recommandList));
          .then(json => printJsonList(json.recommandList));
      }
    });
}

///////////////////////////////이부분은 안건들어도 댐!!!!!!
///////////////////////////////이부분은 안건들어도 댐!!!!!!
///////////////////////////////이부분은 안건들어도 댐!!!!!!
///////////////////////////////이부분은 안건들어도 댐!!!!!!
///////////////////////////////이부분은 안건들어도 댐!!!!!!
///////////////////////////////이부분은 안건들어도 댐!!!!!!


//printJsonList함수는 매개변수 즉 printJsonList(recipeList) <- 괄호 안에 들어가는 recipeList를 가져오는 함수이고
//매개변수 recipeList는 경석이가 말하던 타입리프 써서 가저온 변수랑 똑같은데 우리는 fetch를 사용해서 html에서 값을 가져오는게 아니라 js에서 가져오는 거라 #{} <-요거 안써도 댐
//타이틀은 recipeList[i].title이 아니라 recipeList[i]["title"]로 표현 된다.
//메인이랑
//마이너도 마찬가지 이고
//console.log로 데이터 잘 들어오는거 까지 확인 했음
//지금 printJsonList는 77라인에서 함수 사용을 한다.
//이거 조금 만져 보다가 8시쯤에 나 집 빨리 갈테니까
//조금만 기다려주셈 ㅠㅠ
//이해 안가는거는 갠톡으로 적어주구
//지금 늦어서 가봐야겠따
//쏘리 ㅠㅠ

function printJsonList(recipeList) {
  //json의 list를 출력하기 위한 for문
  for (i in recipeList) {
    //메뉴 리스트 전체적인 틀 만들기
    let menuList = document.createElement("li");
    menuList.className = "menu__list";

    //리스트 안에 각각의 레시피 틀 만들기
    let aboutMenu = document.createElement("div");
    aboutMenu.className = "about__menu";

    //제목 
    let recipeTitle = document.createElement("h1");
    //타이틀 찍어보기
    console.log(recipeList[i]["title"])
    recipeTitle.innerHTML = recipeList[i]["title"];

    //주재료
    let recipeMain = document.createElement("span");
    recipeMain.id = "recipe-main-ingredients";
    console.log(recipeList[i]["main"])
    recipeMain.innerHTML = `<span style="font-weight:bold";>ㅇ주재료:<br></span>` + recipeList[i]["main"].replace("[", "").replace("]", "");

    //부재료
    let recipeMinor = document.createElement("span");
    recipeMinor.id = "recipe-minor-ingredients";
    console.log(recipeList[i]["minor"])
    recipeMinor.innerHTML = `<span style="font-weight:bold";>ㅇ부재료:<br></span>` + recipeList[i]["minor"].replace("[", "").replace("]", "");

    //레시피 리스트 우측에 완성 이미지 틀, 내용
    let recipeImgContainer = document.createElement("div")
    recipeImgContainer.className = "recipe-img-container"
    let recipeImgCover = document.createElement("div")
    recipeImgCover.className = "recipe-img-cover"
    let recipeImg = document.createElement("img");
    recipeImgContainer.appendChild(recipeImgCover);
    recipeImgCover.appendChild(recipeImg)
    recipeImg.src = recipeList[i]["img_complete"];
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
    aboutMenu.appendChild(recipeTitle);
    aboutMenu.appendChild(recipeMain);
    aboutMenu.appendChild(recipeMinor);
    menuList.appendChild(aboutMenu);
    menuList.appendChild(recipeImgContainer);

    //만든 전체적인 HTML요소들을 가상 공간에 저장
    frag.appendChild(menuList);

    //가상 공간에 저장된 것을 한번에 페이지에 뿌린다
    let bmc = document.querySelector(".bookmark-modal-content");
    bmc.appendChild(frag);

    //리스트에서 메뉴 클릭시 레시피결과 페이지로 이동
    menuList.href = "/recipe" + "/" + recipeList[i]["id"].toString();
    menuList.addEventListener("click", function event() {
      location.href = this.href;
    });
  }
};


//오버레이, X버튼 누르면 북마크 닫기
const bookmarkCloseModal = () => {
  let bookmarkContents = document.querySelector(".bookmark__modal");
  mainContents.removeChild(bookmarkContents);
};

function bookmarkDeleteModal(e) {
  let aa = e.target
  let pn = aa.parentNode.parentNode.parentNode;
  let allPn = aa.parentNode.parentNode.parentNode.parentNode;
  pn.remove();
  allPn.remove();
}