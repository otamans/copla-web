$(document).ready(function () {
	var api = '9da81b09ab671d99202764fe681d24a6';
//	var register_api = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=' + api;
	var londonvar = 'http://api.openweathermap.org/data/2.5/weather?q=London&APPID=' + api;
	var new_yourk = 'http://api.openweathermap.org/data/2.5/weather?q=New York&APPID=' + api;
	$('#call_wheather').on('click', function() {
		//location(document.URL + 'London');
		// console.log(document.URL);
		document.location.href = 'London.html';
		$.get( londonvar, function( data ) {
			console.log(data);
		  //$( ".result" ).html( data );
		  //alert( "Load was performed." );
		});
		console.log('asd');
	});

	console.log(location.host);

	$('#next_city').on('click', function() {
		document.location.href = 'New-York.html';
	});

	$('#prev_city').on('click', function() {
		document.location.href = 'London.html';
	});


	if(window.location.href == 'http://localhost/London.html' ){
		$.get( londonvar, function( data ) {
			//console.log(data);
			var temp = data.main.temp - 273.15;
			console.log(temp);
			$('#result_wheather .result_box').append('<span class="result_temp">' + temp.toFixed(1) + '</span>');
		  //$( ".result" ).html( data );
		  //alert( "Load was performed." );
		});
	}
	if(window.location.href == 'http://localhost/New-York.html' ){
		$.get( new_yourk, function( data ) {
			var temp = data.main.temp - 273.15;
			console.log(temp);
			$('#result_wheather .result_box').append('<span class="result_temp">' + temp.toFixed(1) + '</span>');
		});
	}
	//if(window.location.href)
	//console.log(document.URL);
})
