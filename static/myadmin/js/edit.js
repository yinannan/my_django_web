// 编辑表单验证

var phone = false
var email = false

$('input[name=code]').blur(function(){ 
var valu = $(this).val();
var reg = /^\w[0-9]{5}$/;
if(reg.test(valu)){ 
	$(this).css('border','1px solid green');  
	code = true;
}else{
	$(this).val('邮编格式不正确').css('border','1px solid red');
	$(this).css('border','1px solid red');
	code = false; }
})

$('input[name=phone]').blur(function(){ 
var valu = $(this).val();
var reg = /^\w[0-9]{10}$/;
if(reg.test(valu)){ 
	$(this).css('border','1px solid green');  
	phone = true;  
}else{
	$(this).val('手机号码格式不正确').css('border','1px solid red');
	$(this).css('border','1px solid red');
	phone = false; }
})

$('input[name=email]').blur(function(){ 
var valu = $(this).val();
var reg = /^\w[0-9]{2,12}$/;
if(reg.test(valu)){ 
	$(this).css('border','1px solid green');  
	email = true;  
}else{
	$(this).val('邮箱格式不正确').css('border','1px solid red');
	$(this).css('border','1px solid red');
	email = false; }
})

$('.zhuce').click(function(){
	$('input').trigger('blur');
	if(code && phone && email == true){
		return true;
	}
	return false;
})

