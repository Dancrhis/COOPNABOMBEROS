
document.getElementById("menu-btn").addEventListener("click",mostrarMenu);
document.getElementById("back_menu").addEventListener("click",ocultarMenu);

let nav = document.getElementById("menu");
let backgroundMenu=document.getElementById("back_menu");


function mostrarMenu(){
    nav.style.left = "0px"
    backgroundMenu.style.display = "block";

}

function ocultarMenu(){

    nav.style.left="-400px"
    backgroundMenu.style.display="none"
}