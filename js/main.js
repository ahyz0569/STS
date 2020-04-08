// 햄버거 메뉴바 열기
function openNav() {
  document.querySelector(".sidenav").style.width = "250px";
  document.querySelector("body").style.backgroundColor = "#ecf0f1";
  document.getElementById("bg").style.display = "block";
}
// 햄버거 메뉴바 닫기
function closeNav() {
  document.querySelector(".sidenav").style.width = "0";
  document.querySelector("body").style.backgroundColor = "#fdfdfd";
  document.getElementById("bg").style.display = "none";
}