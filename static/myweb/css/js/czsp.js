// 电脑版楼层导航
$(window).scroll(funcgun);
funcgun();

function funcgun(){
	var wendangh = $(document).scrollTop();
	var cha = wendangh -185;
	if( cha >= 0){
		$('#lou').addClass('navbar-fixed-top');
	}else{
		$('#lou').removeClass('navbar-fixed-top');
	}
}

// 手机版楼层导航
$(window).scroll(funcgun2);
funcgun2();

function funcgun2(){
	var wendangh2 = $(document).scrollTop();
	var cha2 = wendangh2 -50;
	if( cha2 >= 0){
		$('#baobo').addClass('navbar-fixed-top');
	}else{
		$('#baobo').removeClass('navbar-fixed-top');
	}
}

// 点击换图
 $('#dianji li').mouseover(function(){
	var s = $(this).find('img').attr('src');
	$('#bigimg').attr('src',s);
});

 // 电脑版购买数量增加
 $('#btn1').click(function(){
 	 var a = $('#yi ').text();
 	if(a<10){
 		a ++;
 		$('#yi').text(a);
 	}
 })

 // 电脑版购买数量减少
  $('#btn2').click(function(){
 	 var a = $('#yi ').text();
 	if(a>1){
 		a --;
 		$('#yi').text(a);
 	}else{a=0;}
 })

  //手机版 购买数量增加
 $('#btnn1').click(function(){
 	 var a = $('#vals ').text();
 	if(a<10){
 		a ++;
 		$('#vals').text(a);
 	}
 })

 // 手机版购买数量减少
  $('#btnn2').click(function(){
 	 var a = $('#vals ').text();
 	if(a>1){
 		a --;
 		$('#vals').text(a);
 	}else{a=0;}
 })


