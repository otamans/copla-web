// function createCookie(name,value,days) {
// 	if (days) {
// 		var date = new Date();
// 		date.setTime(date.getTime()+(days*24*60*60*1000));
// 		var expires = "; expires="+date.toGMTString();
// 	}
// 	else var expires = "";
// 	document.cookie = name+"="+value+expires+"; path=/";
// }

// function readCookie(name) {
// 	var nameEQ = name + "=";
// 	var ca = document.cookie.split(';');
// 	for(var i=0;i < ca.length;i++) {
// 		var c = ca[i];
// 		while (c.charAt(0)==' ') c = c.substring(1,c.length);
// 		if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
// 	}
// 	return null;
// }

// function eraseCookie(name) {
// 	createCookie(name,"",-1);
// }

// function tokenSuccess(err, response) {
//     if(err){
//         throw err;
//     }
//     $(window).sessionStorage.accessToken = response.body.access_token;
//     console.log($(window).sessionStorage.accessToken);
// }

$(document).ready(function () {
	//readCookie('paul');
	var login_request = 'http://24698204.ngrok.io/sign-up';
	$('form.login-form').on('click',function() {

		$.ajax({
		    url: 'http://24698204.ngrok.io/sign-up',
		    headers: {
		        'Content-Type': 'application/x-www-form-urlencoded'
		    },
		    type: "POST", /* or type:"GET" or type:"PUT" */
		    dataType: "json",
		    crossDomain: true,
		    data: { username:'paul', password:'Zxcvbn90'
		    },
		    success: function (result) {
		        //console.log(result);    
		    },
		    error: function () {
		        console.log("error");
		    }
		});




		// console.log('log');
		// //createCookie('paul', '12345', 1);
		// $.post( login_request, function( data ) {
		// 	console.log(data);
		//   //$( ".result" ).html( data );
		//   //alert( "Load was performed." );
		// });
		// return false;
	});
})
