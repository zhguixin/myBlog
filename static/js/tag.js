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
