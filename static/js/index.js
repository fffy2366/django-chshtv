/**
 * Created by lg on 15/5/23.
 */
$(function(){
    //$(window).on("resize",onResized);
    //
    //function onResized(e){
    //
    //}

    $(".gotoTopBtn").on("click",gotoTop);
    function gotoTop(){
        $(window).scrollTop(0);
    }

    $.each($(".sproCon li"),function(index,elm){
        $(elm).on("mouseover",function(){
            $(".sproCon li").removeClass("on");
            $(elm).addClass("on");
        });
    })

    var curkvid = 0;
    var oldkvid = 0;
    var islock = false;
    var dir = 0;
    var len = $(".mkv").length;
    TweenMax.to($(".mkv"),0,{x:1920});
    TweenMax.to($(".mkv")[0],0,{x:0});

    var _time = setTimeout(function(){
        dir = 1;
        curkvid++;
        if(curkvid>=len){
            curkvid = 0;
        }
        $(".kvIcons li").removeClass("on");
        $($(".kvIcons li")[curkvid]).addClass("on");
        flushKv();
    },3000);

    $.each($(".kvIcons li"),function(index,elm){
        $(elm).bind("click",{cid:index},kvHandle);
    })

    function kvHandle(e){
        if(islock) return;
        if(e.data.cid>=curkvid) {
            dir = 1;
        }else{
            dir = -1;
        }
        curkvid = e.data.cid;
        $(".kvIcons li").removeClass("on");
        $($(".kvIcons li")[curkvid]).addClass("on");
        flushKv();
    }

    function flushKv(){
        if(islock) return;
        islock = true;//if(curkvid > oldkvid){
        TweenMax.to($(".mkv")[oldkvid],1,{x:-dir*1920});
        TweenMax.to($(".mkv")[curkvid],1,{x:0,startAt:{x:dir*1920},onComplete:kvCom});
    }
    function kvCom(){
        islock = false;
        oldkvid = curkvid;
    }

});