const mainHeader = document.getElementById("main__header");
      
      
//--start--헤더 전체
mainHeader.innerHTML = ` <div id="mySidenav" class="sidenav">  
      <a class="nav-menu-6" href="/">HOME</a>
      <a class="nav-menu-1" href="/search">SEARCH</a>
      <a class="closebtn" onclick="closeNav()">&times;</a>
      <a class="nav-menu-3" href="/camera">CAMERA</a>`
      +
        nav_isLogin
      +
      `    
    </div>

    
      <div id="bg" onclick="closeNav()"></div>
      <div id="nav-container" onclick="openNav()">
        <div class=" button" tabindex="0">
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </div>
      </div>


      <a href="/">
        <img class="main-logo" src="/images/main-logo.png">
        <img class="main-logo2" src="/images/main-logo2.png">
      </a>


      <div class="nav__nav-column">
      <span class="nav__icon">
        <a href="/search">
          <i class="fas fa-search"></i>
          <span>검색</span>
        </a>
      </span>
      <span class="nav__icon">
        <a href="/camera">
          <i class="fas fa-camera-retro"></i>
          <span>촬영</span>
        </a>
      </span>`
      +
        nav_icon_isLogin
      +
      `
    </div>`;
//--end--헤더 전체

// 햄버거 메뉴바 열기
function openNav() {
  document.querySelector(".sidenav").style.width = "250px";
  document.getElementById("bg").style.display = "block";
}

// 햄버거 메뉴바 닫기
function closeNav() {
  document.querySelector(".sidenav").style.width = "0";
  document.getElementById("bg").style.display = "none";
}