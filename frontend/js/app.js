function get_unlogged_user() {
	$(document).ready(function () {
		$('header .menu .add-service').css('display', 'none');
		$('header .menu .services').css('display', 'none');
		$('header .menu .user-name').css('display', 'none');
		$('header .menu .log-out').css('display', 'none');
	});
}

if($.cookie().token && (document.location.href == document.location.protocol + '//' + window.location.hostname + '/login.html')){
	document.location.href = 'index.html';
}else if(document.location.href == document.location.protocol + '//' + window.location.hostname + '/login.html') {
	get_unlogged_user();
}else {
	$('header .menu .log-in').css('display', 'none');
}


$(document).ready(function () {
	var login_request = 'http://346e4e19.ngrok.io/sign-up';
	$('form.login-form').click(function() {

		if($('form.login-form input[name="user-password"]').val() != $('form.login-form input[name="password-confirm"]').val())
			return false;
		else{
			var username = $('form.login-form input[name="user-name"]').val();
			var userpassword = $('form.login-form input[name="user-password"]').val();

			$.ajax({
			    url: login_request,
			    headers: {
			        'Content-Type': 'application/x-www-form-urlencoded'
			    },
			    type: "POST", /* or type:"GET" or type:"PUT" */
			    dataType: "json",
			    crossDomain: true,
			    data: { username: 'username1111', password: 'userpassword1111'
			    },
			    success: function (result) {
			    	//console.log(result.token);
			        $.cookie('token', result.token);   
			    },
			    error: function () {
			        console.log("error");
			    }
			});
		}
	});
});

console.log(document.location.protocol + '//' + window.location.hostname + '/');

if((document.location.href == document.location.protocol + '//' + window.location.hostname + '/index.html') || (document.location.href == document.location.protocol + '//' + window.location.hostname + '/')){
	
	var login_request = 'http://346e4e19.ngrok.io/service';

	$.ajax({
	    url: login_request,
	    headers: {
	        'Content-Type': 'application/x-www-form-urlencoded'
	    },
	    type: "GET", /* or type:"GET" or type:"PUT" */
	    dataType: "json",
	    crossDomain: true,
	    data: { },
	    success: function (result) {
	    	result.sort(function(a, b){
			    var x = a.plan;
			    var y = b.plan;
			    if (x < y) {return 1;}
			    if (x > y) {return -1;}
			    return 0;
			});
			for(var i = 0; i < result.length; i++){
				
				//var date = 'asd';
				var date = result[i].date.split('T')[0].split('-');
				// date = date[0].split('-');
				console.log(date[0]);
				if(i < 4 && result[i].plan == 3){
					// if(result[i].plan == 3){
					// }
					var plan_type = '<img src="../img/advertising-service.png">';
					$('body.search-page_page .main .services').append('<div class="large-3 medium-4 small-6 columns service-cell"><div class="header-service-item row"><div class="top-service"></div><div class="point-cost large-4 medium-4 small-4">' + result[i].time_coins + '</div><div class="service-type large-4 medium-4 small-4">' + plan_type + '</div><div class="service-date large-4 medium-4 small-4">' + date[2] + '.' + date[1] + '</div></div><div class="dark-cover"></div><div class="thumbnail" style="background: url(' + result[i].photo + '); height: 200px; background-repeat: no-repeat; background-size: cover;"></div><div class="bottom-service-item"><div class="service-title">' + result[i].name + '</div><div class="service-more"><a href="#">Подробнее</a></div></div></div>');
				}
				else {
					var plan_type = ' ';
					if(result[i].plan == 2)
						plan_type = '<img src="../img/lock-service.png">';
					$('body.search-page_page .main .services').append('<div class="large-3 medium-4 small-6 columns service-cell"><div class="header-service-item row"><div class="point-cost large-4 medium-4 small-4">' + result[i].time_coins + '</div><div class="service-type large-4 medium-4 small-4">' + plan_type + '</div><div class="service-date large-4 medium-4 small-4">' + date[2] + '.' + date[1] + '</div></div><div class="dark-cover"></div><div class="thumbnail" style="background: url(' + result[i].photo + '); height: 200px; background-repeat: no-repeat; background-size: cover;"></div><div class="bottom-service-item"><div class="service-title">' + result[i].name + '</div><div class="service-more"><a href="#">Подробнее</a></div></div></div>');
				}
				if(i == 3){
					$('body.search-page_page .main .services').append('<hr>');
				}
			}
			// $('body.search-page_page .services').append()
	        //$.cookie('token', result.token);   
	    },
	    error: function () {
	        console.log("error");
	    }
	});


}
