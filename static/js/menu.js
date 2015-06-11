/**
 * Created by lg on 15/5/25.
 */
$(function(){
    var baseX = 294;
    var cid = 0;
    var overId = -1;

    TweenMax.to($(".menu2Con"),0,{marginLeft:(baseX+104*cid),ease:Cubic.easeOut});

    $.each($(".menuCon li"),function(index,elm){
        $(elm).bind("mouseover",{cid:index},show2Menu);
        $(elm).bind("mouseout",{cid:index},menuOut);
        $(elm).bind("click",{cid:index},menuClicked);
    })
    $(".menu3").bind("mouseover",{cid:2},over2);
    $(".menu3").bind("mouseout",{cid:2},menuOut);

    function over2(e){
        overId = e.data.cid;
    }

    function menuClicked(e){
    }
    function show2Menu(e){
        tmpId = e.data.cid;
        overId = tmpId;
        var _x = (baseX+104*tmpId);
        TweenMax.to($(".menu2Con"),.6,{marginLeft:_x,ease:Cubic.easeOut});
        if(e.data.cid == 2){
            $(".menu3").css({"display":"block","opacity":1});
        }else{
            $(".menu3").css({"display":"none","opacity":0});
        }
    }
    function menuOut(e){
        overId = -1;
        TweenMax.delayedCall(.1,checkMenu2);
    }

    function checkMenu2(){
        if(overId != 2){
            $(".menu3").css({"display":"none","opacity":0});
        }else{
            $(".menu3").css({"display":"block","opacity":1});
        }
        if(overId == -1){
            var _x = (baseX+104*cid);
            TweenMax.to($(".menu2Con"),.6,{marginLeft:_x,ease:Cubic.easeOut});
        }
    }


})