// function getDeviceData(url, data, callback){
// 	var request = new XMLHttpRequest();
// 	request.open('post',url);
// 	request.onreadystatechange = function(){
// 		if(request.readyState == 4){
// 			callback(request);
// 		}
// 	};
// 	request.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
// 	request.send(encodeFormData);
// }

// function insertDeviceData(data){
// 	var table = document.getElementByTagName('table');
// 	var length = data.length;
// 	for(var i=0; i<length; i++){
// 		var newTd = document.createElement('td');
// 		var oneData = data[i];
// 		var data_length = data[i].length;
// 		for(var j=0; j<data_length; j++){
// 			var newTr = document.createElement('tr');
// 			newTr.innerText = oneData[j];
// 			newTd.appendChild(newTr);
// 		}
// 	}
// }

// //condition = [bigCondition, smallCondition]
// function dataSelect(data, condition){
// 	var data_selection= [];
// 	var length = data.length;
// 	var select_condition = condition[0];
// 	for(var i=0; i<length; i++){
// 		if(data[i].select_condition == condition[2]){
// 			data_selection.push(data[i]);
// 		}
// 	}
// 	return data_selection;
// }

// function deleteTableData(){
// 	var table = document.getElementByTagName('table');
// 	var table_length = table.length;
// 	while(table.length != 0){
// 		table.removeChild(table.lastChild);
// 	}
// }

function onClick_IOS(){
	// var condition = ['操作系统'，‘IOS’];
	alert('hello sb~');
}

function onClick_Android(){
	alert('1hahaasb');
}

function onClick_Other(){
    //xmlhttp=new XMLHttpRequest();
    //xmlhttp.onreadystatechange=funtion(){
        alert('haha');
    //    }
    //xmlhttp.open('GET','http://localhost:8000/getDeviceInfo/show/',true);
    //xmlhttp.send();
    //}
    //$.get('http://localhost:8000/getDeviceInfo/show/',function(data,status){
    //alert('return:'+data+status+'.');
    //});
}

function onClick_borrow(){
    var borrower = document.getElementById("borrower").value;
    alert(borrower)
    var device_id = document.getElementById("borrow_device_id").innerHTML;
    var usrPre = window.location.hostname;
    var selfObject = "http://"+usrPre+":8000/getDeviceInfo/borrow_with_name/?device_id="+device_id+"&borrower="+borrower;
    window.opener=null;
    window.close();
    //var lin = document.getElementById("borrow_button")
    //lin.href = selfObject.href
    }

