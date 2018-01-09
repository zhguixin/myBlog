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

//固定顶部footer，动态添加【fixed-bottom】样式
$(function(){
 function footerPosition(){
     $("#footer").removeClass("fixed-bottom");
     var contentHeight = document.body.scrollHeight,//网页正文全文高度
         winHeight = window.innerHeight;//可视窗口高度，不包括浏览器顶部工具栏
     if(!(contentHeight > winHeight)){
         //当网页正文高度小于可视窗口高度时，为footer添加类fixed-bottom
         $("#footer").addClass("fixed-bottom");
     } else {
         $("#footer").removeClass("fixed-bottom");
     }
 }
 footerPosition();
 $(window).resize(footerPosition);
});

//标签页展开、隐藏按钮功能实现
$(document).ready(function(){
    $("#closeAll").click(function(){
        for(var i=1;i < 99; i++) {
            $('#'+i).collapse('hide');
        }
      });
});

$(document).ready(function(){
    $("#openAll").click(function(){
        for(var i=1;i < 99; i++) {
            $('#'+i).collapse('show');
        }
      });
});

function openNav() {
    document.getElementById("mySidenav").style.width = "150px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}
