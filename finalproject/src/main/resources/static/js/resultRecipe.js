let frag = document.createDocumentFragment();
let resultRecipeInfo = document.getElementById("result-recipe-info");

let recipeImg = document.createElement("img");
recipeImg.id = "result-img";
recipeImg.src = recipe.img_complete;

let recipeHeader = document.createElement("header");
recipeHeader.className = "recipeTitle";
recipeHeader.innerHTML = recipe.title;

let recipeDescription = document.createElement("p");
recipeDescription.className = "recipeDescription";
recipeDescription.innerHTML = `" ${recipe.description} "`;

let servingInfo = document.querySelector(".serving-info");
servingInfo.innerHTML = recipe.size;

let timeInfo = document.querySelector(".time-info");
timeInfo.innerHTML = recipe.time;

let difficultyInfo = document.querySelector(".difficulty-info");
difficultyInfo.innerHTML = recipe.level;

// recipeHeader.className = ""; recipeHeader.innerHTML = recipe__info[1];
// recipeImg.src = recipe__info[66];




//hyeon
function insertBookmark(recipeID) {
    console.log("recipeID", recipeID);
    const odj = {
        method: 'POST',
        body: JSON.stringify({userID: 0, recipeID: recipeID}),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        },
        credentials: 'same-origin'
    };
    //fetch를 사용할때 url과 odj로 GET ,POST 메서드를 설정해 준다.
    fetch("http://localhost:8080/insertBookmark", odj)
    //reponse를 가져와서
        .then(res => {
        //status가 200이라면
        if (res.status == 200) {
            //servlet에서 return된 json값을 가져 온다.
            res
                .json()
                .then(json => console.log(json.recipeIDList));
        }
    })
}
//bookmark를 load하기 위한 로직
function loadBookmark(){
    const odj = {
        //권한 설정이 되어 있을때만 fetch실행
        credentials: 'same-origin'
    };
    fetch("http://localhost:8080/loadBookmark",odj)
        .then(res =>{
            //정상 응답이 왔을 때 로직 실행
            if (res.status == 200){
                res
                .json()
                // .then(json => newDiv.innerHTML = json.recommandList)
                .then(json => printJsonList(json.recommandList));
            }
        });
    
}
//json에 포함되어 있는 list를 li태그를 사용해서 출력하기 위한 함수
function printJsonList(list){
    //li를 담을 div태그 생성
    let newDiv = document.createElement("div");
    //newDiv를 append할 list id를 가진 div 
    let div = document.getElementById("list");
    //json의 list를 출력하기 위한 for문
    for(key in list){
        let li = document.createElement('li')
        li.innerHTML = list[key]["title"];
        newDiv.appendChild(li);

        // console.log(list[key]);
        // newDiv.innerHTML = "<li>" + list[key]["title"] + "</li>";
    }
    div.appendChild(newDiv);
    
    
}
//hyeon




resultRecipeInfo.appendChild(recipeImg);
resultRecipeInfo.appendChild(recipeHeader);
resultRecipeInfo.appendChild(recipeDescription);
let mainIngredientsInfo = document.querySelector(".main-ingredients-info");
mainIngredientsInfo.innerHTML = `<span style="font-weight: bold">ㅇ주재료 :</span> ${recipe.main}`;

let minorIngredientInfo = document.querySelector(".minor-ingredients-info");
minorIngredientInfo.innerHTML = `<span style="font-weight: bold">ㅇ부재료 :</span> ${recipe.minor}`;
frag.appendChild(recipeImg);
frag.appendChild(recipeHeader);
frag.appendChild(recipeDescription);
resultRecipeInfo.appendChild(frag);

const recipeStepsInfo = document.getElementById("recipe-steps-info");

recipe__info = recipe.step.split("', '")
recipe__img = recipe.img.split("', '")
for (i in recipe__info) {
  console.log(recipe__info[i].replace("[","").replace("]","").replace("'",""))
  console.log(recipe__img[i].replace("[","").replace("]","").replace("'",""))
  recipeStepsInfo.id = "recipe-steps-info";
  let recipeSteps = document.createElement("div");
  recipeSteps.className = "recipe-steps";
  let step = document.createElement("span");
  step.className = "cookStep";
  step.innerHTML = `<div class="stepNumber">${[Number(i) + 1]}.</div> ${
    recipe__info[i].replace("[","").replace("]","").replace("'","")
  }`;
  let stepImg = document.createElement("img");
  stepImg.src = recipe__img[i].replace("[","").replace("]","").replace("'","");
  recipeSteps.appendChild(step);
  recipeSteps.appendChild(stepImg);

  frag.appendChild(recipeSteps);
  recipeStepsInfo.appendChild(frag);
}

let stepsEnd = document.createElement("div");
stepsEnd.id = "steps-end";
stepsEnd.innerHTML = "- - - END - - -";
recipeStepsInfo.appendChild(stepsEnd);
