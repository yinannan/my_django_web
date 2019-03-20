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
