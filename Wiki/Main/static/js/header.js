menu.onclick = function myFunction() {
    var x = document.getElementById("myTopNav")

    if (x.className === "topnav"){
        console.log("Применили стиль")
        x.className += " responsive";
    } else {
        console.log("ничего не вышло")
        x.className = "topnav"
    }
}

