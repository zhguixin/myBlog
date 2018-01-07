// webPlugin - http://download.eclipse.org/releases/juno

function myFunction() {
    document.getElementById("demo").innerHTML="我的第一个 JavaScript 函数";
}

$('#myBlog').on('click', function (e) {
    e.preventDefault();
    $('html,body').animate({
        scrollTop: 0
    }, 700);
});

function openNav() {
    document.getElementById("mySidenav").style.width = "150px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}
