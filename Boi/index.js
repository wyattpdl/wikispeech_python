var toggle = 3;
function run(){
	if(toggle === 3){	
		toggle = 'jimmy';
		var rid= "confirmed";
		document.getElementById("live").innerHTML += rid + " ";
	}else{
		toggle = 3;
		var rid= "jimmy";
		document.getElementById("live").innerHTML += rid + " ";
 	}         
 	console.log(toggle)
}