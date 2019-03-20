
// 添加表单验证
var passwords = false;
var codes = false
var phones = false
var emails = false

$('input[name=code]').blur(function(){ 
var valu = $(this).val();
var reg = /^\w[0-9]{5}$/;
if(reg.test(valu)){ 
	$(this).css('border','1px solid green');  
	codes = true;
}else{
	$(this).val('邮编格式不正确').css('border','1px solid red');
	$(this).css('border','1px solid red');
	codes = false; }
})

$('input[name=phone]').blur(function(){ 
var valu = $(this).val();
var reg = /^\w[0-9]{10}$/;
if(reg.test(valu)){ 
	$(this).css('border','1px solid green');  
	phones = true;  
}else{
	$(this).val('手机号码格式不正确').css('border','1px solid red');
	$(this).css('border','1px solid red');
	phones = false; }
})

$('input[name=email]').blur(function(){ 
var valu = $(this).val();
var reg = /^\w[0-9]{2,12}$/;
if(reg.test(valu)){ 
	$(this).css('border','1px solid green');  
	emails = true;  
}else{
	$(this).val('邮箱格式不正确').css('border','1px solid red');
	$(this).css('border','1px solid red');
	emails = false; }
})

$('input[name=password]').blur(function(){ 
	var valp = $(this).val();
	var reg = /^\w[0-9]+$/;
	if(reg.test(valp)){ 
		$(this).css('border','1px solid green');  
		passwords = true;  
	}else{
		$(this).val('密码格式不正确').css('border','1px solid red');
		$(this).css('border','1px solid red');
		passwords = false; 
	}
})

$('.zhu').click(function(){
	$('input').trigger('blur');
	if( passwords && codes && phones && emails == true){
		return true;
	}
	return false;
})
