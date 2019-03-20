// // 增加数量
// $('#btnn1').click(function(){
// 	var yiyi = $('#vals').text();
// 	console.log(yiyi);
// 	if(yiyi<9){
// 		yiyi++;
// 	$('#vals').text(yiyi);
// 	var bb = yiyi*10.00;
// 	$('#yingfu').text(bb);
// 	$('#liu').text(bb);
// 	}
// })
// //减少数量
// $('#btnn2').click(function(){
// 	var yiyi = $('#vals').text();
// 	console.log(yiyi);
// 	if(yiyi<2){
// 		yiyi = 1;
// 		$('#vals').text(yiyi);
// 		var bb = yiyi*10.00;
// 		$('#yingfu').text(bb);
// 		$('#liu').text(bb);
// 	}else{
// 		yiyi--;
// 	}
// 	$('#vals').text(yiyi);
// 	var bb = yiyi*10.00;
// 	$('#yingfu').text(bb);
// 	$('#liu').text(bb);
// })

// 全选和反选
// function chi(a){
// 	var id = document.getElementsByTagName('input');
// 	for (var i = 0; i < id.length; i++) {
// 		switch(a){
// 			case 1:
// 				id[i].checked=true;
// 				break;
// 			case 2:
// 				id[i].checked=false;
// 				break;
// 			case 3 :
// 				id[i].checked=!id[i].checked;
// 				break;
// 		}	
// 	}
// }


// 购物增加数量及应付金额
$('.jia').click(function(){
	var a = $(this).parent().prev('div').text();
	// alert(a)
	// $('div').next('p')
	// alert(a)
	if(a<9){
		a ++;
		// alert(a)
		$(this).parent().prev('div').text(a);
	}
	var c = $('#danjia').text();  
	// alert(c)
	var d = a*c;
	// alert(d)
	// $('.shuliang').text(a);
	// $('#youhui').text(d);
	$(this).parents().find('#youhui').text(d);

})

//PC购物数量减少及应付金额
 $('.jian').click(function(){
	var b = $(this).parent().next('div').text();
	// alert(b)
	if(b>1){
		b --;
		// alert(b)
		$(this).parent().next('div').text(b);
	}else{
		b=1;
	}
	var c = $('#danjia').text();
	// alert(c)
	var d = b*c;
	// alert(d)
	// if(d>10){
	// 	$('#jine').text(d);
	// }else{
	// 	d=10;
	// 	$('#jine').text(d);
	// }
	// $('#yixuan').text(b);
	$('#youhui').text(d);
})



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

// PC点击移除
$('.ii').click(function(){
	$('.dell').remove();
	$('#jine').text('0');
	$('#yixuan').text('0');
})




