	$(function(){
		$('#create_date').datetimepicker({
			//inline: true,
			dateFormat: 'yy-mm-dd',
			timeFormat: "HH:mm:ss",
			maxDate:"+0m +0w"
		});
		uploadImage("#imgTitle","questions") ;
		uploadImage("#option_a","options") ;
		uploadImage("#option_b","options") ;
		uploadImage("#option_c","options") ;
		uploadImage("#option_d","options") ;
		uploadMusic("#music","musics") ;
		uploadMusic("#titlesound","titlesounds") ;

		$("#autoplay").click(function(){
			var check = $("#autoplay").is(':checked') ;
			if(check){
				$("#playcount").show() ;
			}else{
				$("#playcount").hide() ;
			}
		}) ;
	}) ;
	/**
	 * id:#id
	 * type:存储目录名
	 */
	function uploadImage(id,type){
	    var upload = new AjaxUpload(jQuery(id), {
		    action: '/admin/upload',
		    name: 'upfile',
		    data: {
		        'limitMaxSize': "1"
		    },
		    autoSubmit: true,
		    responseType: 'json',
		    onChange: function(file, ext){
		    },
		    onSubmit: function(file, ext){
		        // Allow only images. You should add security check on the server-side.
		        if (ext && /^(gif|jpg|png)$/i.test(ext)) {                            
		            this.setData({
		                'limitMaxSize': '2',
		                'type':type,
		                'key2': '...'
		            });
		            //loading
		            $(id+"_loading").html("<img src=\"/resources/js/fileuploader/loading.gif\"/>") ;
		        } else {
		            alert("上传文件类型不正确") ;
		            return false;
		        }                            
		    },
		    onComplete: function(file, response){
		        //this.disable();
		        //loading
		        $(id+"_loading").empty() ;
		        
		        if(response.status == "y"){
					$(id+"_img").html("<img style=\"height:80px\" src=\"/public/uploads/"+type+"/"+response.filename+"\"/>") ;
					$(id+"_inp").val(file) ;
					$(id+"_filename").val(response.filename) ;
		        }
		        if(response.status == "n"){
		        	alert("文件不大于1M！") ;
		        }
		    }
		});
	}    	
	/**
	 * id:#id
	 * type:存储目录名
	 */
	function uploadMusic(id,type){
	    var upload = new AjaxUpload(jQuery(id), {
		    action: '/admin/upload',
		    name: 'upfile',
		    data: {
		        'limitMaxSize': "1"
		    },
		    autoSubmit: true,
		    responseType: 'json',
		    onChange: function(file, ext){
		    },
		    onSubmit: function(file, ext){
		        // Allow only images. You should add security check on the server-side.
		        if (ext && /^(mp3)$/i.test(ext)) {                            
		            this.setData({
		                'limitMaxSize': '2',
		                'type':type,
		                'key2': '...'
		            });
		            //loading
		            $(id+"_loading").html("<img src=\"/resources/js/fileuploader/loading.gif\"/>") ;
		        } else {
		            alert("上传文件类型不正确") ;
		            return false;
		        }                            
		    },
		    onComplete: function(file, response){
		        //this.disable();
		        //loading
		        $(id+"_loading").empty() ;
		        
		        if(response.status == "y"){
					$(id+"_img").html("上传成功") ;
					$(id+"_inp").val(file) ;
					$(id+"_filename").val(response.filename) ;
		        }
		        if(response.status == "n"){
		        	alert("上传失败") ;
		        }
		    }
		});
	}  

	$(function(){
		
		$("#questionBtn").click(function(){
			var area_id = $("input[name='area']:checked").val() ;
            var title = $("#title").val() ;
            var category_id = $("#category").val() ;
            var num = $("#num").val() ;
            var correct = $("#correct").val() ;
            var score = $("#score").val() ;
            var img = $("#imgTitle_filename").val() ;
            var music = $("#music_filename").val() ;
            var titlesound = $("#titlesound_filename").val() ;
            //alert($("#autoplay").is(":checked")) ;
            var autoplay = $("#autoplay").is(":checked")?"yes":"no" ;
            var titlesound_autoplay = $("#titlesound_autoplay").is(":checked")?"yes":"no" ;
            var playcount = $("#playcount").val() ;
            var countdown = $("#countdown").val() ;//倒计时
            window.console&&console.log(autoplay+" "+playcount) ;
            //return ;
            var label = [] ;
            $("input[name='label[]']:checked").each(function(){
            	label.push($(this).val()) ;
            }) ;

            var option_a = $("#option_a_title").val() ;
            var option_a_img = $("#option_a_filename").val() ;

            var option_b = $("#option_b_title").val() ;
            var option_b_img = $("#option_b_filename").val() ;

            var option_c = $("#option_c_title").val() ;
            var option_c_img = $("#option_c_filename").val() ;

            var option_d = $("#option_d_title").val() ;
            var option_d_img = $("#option_d_filename").val() ;
            if(title==""){
            	$.Showmsg("请输入题目") ;
            	return ;
            }
            if(num==""){
            	$.Showmsg("请输入一个题号") ;
            	return ;
            }
            if(isNaN(num)){
            	$.Showmsg("题号应为一个数字") ;
            	return ;
            }
            if(img==""){
            	//$.Showmsg("请输入图片") ;
            	//return ;
            }
            if(music==""){
            	//$.Showmsg("请输入音乐") ;
            	//return ;
            }
            if(correct==""){
            	$.Showmsg("请选择正确答案") ;
            	return ;
            }
            if(category_id==""){
            	$.Showmsg("请选择一个目录") ;
            	return ;
            }
            if(countdown==""){
            	$.Showmsg("请输入一个倒计时") ;
            	return ;
            }
            if(isNaN(countdown)){
            	$.Showmsg("倒计时应为一个数字") ;
            	return ;
            }

            window.console&&console.log("label："+label) ;
            //return ;
			var data = {
						'id':id,'area_id':area_id,'label':label,'title':title,'category_id':category_id,'num':num,'correct':correct,'img':img,'music':music,
						'titlesound':titlesound,'score':score,
						'option_a':option_a,'option_a_img':option_a_img,
						'option_b':option_b,'option_b_img':option_b_img,
						'option_c':option_c,'option_c_img':option_c_img,
						'option_d':option_d,'option_d_img':option_d_img,
						'settings':{'autoplay':autoplay,'titlesound_autoplay':titlesound_autoplay,'playcount':playcount,'countdown':countdown}
						} ;
			$.post('/admin/question/update',data,function(data){
                window.console&&console.log(data) ;
				if(data.status=="y"){
					$.Showmsg(data.info) ;
					
					setTimeout(function(){
						$.Hidemsg(); //公用方法关闭信息提示框;显示方法是$.Showmsg("message goes here.");
						//window.location.href="/admin/question" ;
						var currPage = $.getURLParam("page");
						var cid = $.getURLParam("cid");
						if(!!currPage){
							if(!!cid){
								window.location.href="/admin/question?cid="+cid+"&page="+currPage ;
							}else{
								window.location.href="/admin/question?page="+currPage ;
							}							
						}else{
							if(!!cid){
								window.location.href="/admin/question?cid="+cid;
							}else{
								window.location.href="/admin/question"								
							}
						} 
						
						//history.back() ;
					},2000);
				}else if(data.status=="n"){
					$.Showmsg(data.info) ;
				}
			}) ;
		}) ;


	}) ;
    /*
	var editor = CKEDITOR.replace('content', { 
		language:'zh-cn',//简体中文 
		resize_enabled: false,
		toolbar ://工具栏设置 
		[ 
		['Source'], 
		//'/', 
		['Cut','Copy','Paste','PasteText','PasteFromWord'], 
		['Bold','Italic','Underline','Strike','-','Subscript','Superscript'], 
		['TextColor','BGColor'],
		['Image'] 
		]
	}); */
	