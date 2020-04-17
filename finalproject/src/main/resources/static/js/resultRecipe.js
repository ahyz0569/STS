// let recipe__infos = {}
let recipe__info = recipe;
console.log(recipe);

let frag = document.createDocumentFragment();
let resultRecipeInfo = document.getElementById("result-recipe-info");

let recipeImg = document.createElement("img");
let recipeHeader = document.createElement("header");
let recipeDescription = document.createElement("p");

// recipeHeader.className = ""; recipeHeader.innerHTML = recipe__info[1];
// recipeImg.src = recipe__info[66];

function bookmarkSwitch(recipeID) {
    console.log("recipeID", recipeID);
    const odj = {
        method: 'POST',
        body: JSON.stringify({userID: 0, recipeID: recipeID}),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        },
        credentials: 'same-origin'
    };
    //fetch를 사용할때 url과 odj로 GET ,SET 메서드를 설정해 준다.
    fetch("http://localhost:8080/testFetch", odj)
    //reponse를 가져와서
        .then(res => {
        //status가 200이라면
        if (res.status == 200) {
            //servlet에서 return된 json값을 가져 온다.
            res
                .json()
                .then(json => console.log(json));
        }
    })
}
resultRecipeInfo.appendChild(recipeImg);
resultRecipeInfo.appendChild(recipeHeader);
resultRecipeInfo.appendChild(recipeDescription);