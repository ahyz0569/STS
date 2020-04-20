<<<<<<< HEAD
let resultForm = document.getElementById("result__form");
let resultInfo = document.getElementById("result__info");
const plusText = document.getElementById("plus__text");
let plusBtn = document.getElementById("info-plus-btn");
let closeBtn = document.getElementById("close__text-add");

let frag = document.createDocumentFragment();
=======
const resultForm = document.getElementById("result__form");
const plusText = document.getElementById("plus__text");
let resultInfo = document.getElementById("result__info");


>>>>>>> d5540d74119adea1e212dc64b4f249ed3da30205
//--start-- 재료 데이터 받는 곳//
let analyzed__ingredients,
  i,
  ingredient__lists = "";

analyzed__ingredients = {
<<<<<<< HEAD
  name: label
};


for (i in analyzed__ingredients.name) {
  let ingredientsTypes = document.createElement("div");
  ingredientsTypes.className = "ingredients-types";
  let ele = document.createElement("input");
  ele.readOnly = true;
  ele.className = "info";
  ele.setAttribute("type", "text");
  ele.setAttribute("name", "label");
  ele.setAttribute("value", analyzed__ingredients.name);
  ingredientsTypes.appendChild(ele);

  let deleteBtn = document.createElement("button");
  deleteBtn.setAttribute("type", "button");
  deleteBtn.innerHTML = "X"
  deleteBtn.className = "info-delete-btn";
  deleteBtn.addEventListener("click", deleteLi);
  ingredientsTypes.appendChild(deleteBtn);

  frag.appendChild(ingredientsTypes);
  resultInfo.appendChild(frag);
  resultInfo.appendChild(plusBtn);
}

=======
  name: ["egg", "onion", "potato", "carrot", "cucumber", "tomato"],
};

let frag = document.createDocumentFragment();
let plusBtn = document.getElementById("info-plus-btn");

for (i in analyzed__ingredients.name) {
  let ele = document.createElement("li");
  ele.className = "info";
  ele.innerHTML = `<span style="cursor:pointer" onclick="fnc()">${analyzed__ingredients.name[i]}</span> <div class="info-close-btn">&times;</div>`;
  frag.appendChild(ele);
  ele.getElementsByClassName("info-close-btn")[0].addEventListener("click", deleteLi);
}
>>>>>>> d5540d74119adea1e212dc64b4f249ed3da30205
//--end--재료 데이터 받는 곳//


//--start-- 재료 삭제 버튼//
function deleteLi(event) {
  const btn = event.target;
<<<<<<< HEAD
  const prevBtn = btn.parentNode;
  prevBtn.remove();
}
=======
  const li = btn.parentNode;
  resultInfo.removeChild(li);
}
resultInfo.appendChild(frag);
resultInfo.appendChild(plusBtn);
>>>>>>> d5540d74119adea1e212dc64b4f249ed3da30205
//--end-- 재료 삭제 버튼//


//--start-- 메인 재료 선정 - 미구현
function fnc() {
  console.log(this);
}
//--end-- 메인 재료 선정 - 미구현


<<<<<<< HEAD
function addIng() {
  // enter 시 자동 submit기능 방지.
  event.preventDefault()
  let currentValue = plusText.value;

  let ingredientsTypes = document.createElement("div");
  ingredientsTypes.className = "ingredients-types";
  let eles = document.createElement("input");
  eles.className = "info";
  eles.setAttribute("type", "text");
  eles.setAttribute("name", "label");
  eles.setAttribute("value", currentValue);
  ingredientsTypes.appendChild(eles);

  let deleteBtn = document.createElement("button");
  deleteBtn.setAttribute("type", "button");
  deleteBtn.innerHTML = "X"
  deleteBtn.className = "info-delete-btn";
  deleteBtn.addEventListener("click", deleteLi);
  ingredientsTypes.appendChild(deleteBtn);

  frag.appendChild(ingredientsTypes);
  resultInfo.appendChild(frag);
  resultInfo.appendChild(plusBtn);

  eles.readOnly = true;
  plusText.value = "";

  let input = document.getElementById("plus__text").focus();
}


function openAddModal() {
  let addModal = document.getElementById("add-modal-cover");
  addModal.classList.remove("hidden");
  let input = document.getElementById("plus__text").focus();
  plusBtn.style.display = "none";
}

function closeAddModal() {
  let addModal = document.getElementById("add-modal-cover");
  addModal.classList.add("hidden");
  plusBtn.style.display = "block";

}
=======

//--start-- 재료추가 타이핑
function handleSubmit(event) {
  event.preventDefault();
  let currentValue = plusText.value;
  paintToDo(currentValue);
  plusText.value = "";
}

function paintToDo(text) {
  let ele = document.createElement("li");
  ele.className = "info";
  ele.innerHTML = `<span style="cursor:pointer" onclick="fnc()">${text}</span> <div class="info-close-btn">&times;</div>`;
  ele.getElementsByClassName("info-close-btn")[0].addEventListener("click", deleteLi);
  frag.appendChild(ele);
  resultInfo.appendChild(frag);
  resultInfo.appendChild(plusBtn);
}

function init() {
  resultForm.addEventListener("submit", handleSubmit);
}
init();
//--end-- 재료추가 타이핑
>>>>>>> d5540d74119adea1e212dc64b4f249ed3da30205
