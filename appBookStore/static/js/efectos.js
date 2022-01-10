function BlinkIt () {
    var blink = document.getElementById ("blink");
    color = (color == "#ffffff")? "rgba(136, 66, 95, 0.965)" : "#ffffff";
    blink.style.color = color;
    blink.style.fontSize='36px';

}


function alertNovedadPlanetaDelLibro(nombre){

    alert(nombre+' es el último libro que ha sacado la editorial planeta del libro');
    return false;
}


function alertNovedadErein(nombre){

    alert(nombre+' es el último libro que ha sacado la editorial Erein');
    return false;
}

