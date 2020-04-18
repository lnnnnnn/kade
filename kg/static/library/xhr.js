function xhr(url, isJson, sucCallback, errCallback){
	//alert("in");
	var xhr = null;

        if (window.XMLHttpRequest) {
            // code for IE7+, Firefox, Chrome, Opera, Safari
            xhr = new XMLHttpRequest();
        } else {
            // code for IE6, IE5
            xhr = new ActiveXObject("Microsoft.XMLHTTP");
        }
	try{

		xhr.timeout = 20000;
		xhr.onreadystatechange = function () {
			switch ( xhr.readyState ) {
				case 0:
					//alert( "xhr请求已初始化" );
				break;
				case 1:
					//alert( "xhr请求已打开" );
				break;
				case 2:
					//alert( "xhr请求已发送" );
				break;
				case 3:
					//alert( "xhr请求已响应");
					break;
				case 4:
					if ( xhr.status == 200 ) {
						//alert(xhr.responseText);

						//console.log(xhr.responseText);
						if(isJson)
							sucCallback( JSON.parse( xhr.responseText ) );
						else
							sucCallback(  xhr.responseText );
					} else {
						errCallback();
					}
					break;
				default :
					break;
			}
		}
		console.log(url);

		   xhr.open("GET", url, true);
        xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
        xhr.send();
		/*xhr.open("POST", url);
		xhr.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
		xhr.send();*/
			
	}catch(e){
		console.log(e);
		if( xhr != null){
			xhr.abort();
			xhr = null;
		}
	}
	
}
