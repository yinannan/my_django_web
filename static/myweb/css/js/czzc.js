
// 表单验证
var names = false;
var pass = false;

$('input[name=username]').blur(function(){ 
var valu = $(this).val();
var reg = /^\w{6,10}$/;
if(reg.test(valu)){ 
	$(this).css('border','1px solid green');  
	names = true;  
}else{
	$(this).html('用户名格式不正确').css('border','1px solid red');
	$(this).css('border','1px solid red');
	names = false; }
})


$('input[name=password]').blur(function(){ 
	var valp = $(this).val();
	var reg = /^\w{6,10}$/;
	if(reg.test(valp)){ 
		$(this).css('border','1px solid green');  
		pass = true;  
	}else{
		$(this).html('密码格式不正确').css('border','1px solid red');
		$(this).css('border','1px solid red');
		pass = false; 
	}
})

$('.zhuce').click(function(){
	$('input').trigger('blur');
	if(pass && names == true){
		return true;
	}
	return false;
})