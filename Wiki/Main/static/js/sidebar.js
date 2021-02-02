var x = document.getElementById("minimize-menu");
if  (x.classList.contains("fa-chevron-circle-left")) {
        x.onclick = function () {
    document.getElementById('minimize-menu').classList.remove('fa-chevron-circle-left');
    document.getElementById('minimize-menu').classList.add('fa-chevron-circle-right');
    document.getElementsById("navbar-side").setAttribute("style", "color:red; border: 1px solid blue;");
    document.getElementsByClassName("menu-text").style.display='none';
}
}
else {

    console.log(x.classList)
}

$('#navbar-side').css({"width":"55px"});
          $('.menu-text').css({"display":"none"});
          $('#navbar-side > ul > li > a > b').remove();
