let slider = document.querySelector(".slider-contenedor")
let sliderIndividual = document.querySelectorAll(".contenido-slider")
let contador = 1;
let width = sliderIndividual[0].clientWidth;
let intervalo = 5000;

window.addEventListener("resize", function(){
    width = sliderIndividual[0].clientWidth;
})

setInterval(function(){
    slides();
},intervalo);



function slides(){
    slider.style.transform = "translate("+(-width*contador)+"px)";
    slider.style.transition = "transform .8s";
    contador++;

    if(contador == sliderIndividual.length){
        setTimeout(function(){
            slider.style.transform = "translate(0px)";
            slider.style.transition = "transform 0s";
            contador=1;
        },1500)
    }
}



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