// 楼层导航
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

// 鼠标移入事件
$('.biankuangid').mouseover(function(){
	$(this).addClass('biankuang');
	$(this).find('.pp1').hide();
	$(this).find('.pp2').show();
})
		
// 鼠标移出事件
$('.biankuangid').mouseout(function(){
	$(this).removeClass('biankuang');
	$(this).find('.pp1').show();
	$(this).find('.pp2').hide();
})

$(window).scroll(funcgun2);
funcgun2();

function funcgun2(){
	var wendangh2 = $(document).scrollTop();
	var cha2 = wendangh2 -55;
	if( cha2 >= 0){
		$('#baobo').addClass('navbar-fixed-top');
	}else{
		$('#baobo').removeClass('navbar-fixed-top');
	}
}


