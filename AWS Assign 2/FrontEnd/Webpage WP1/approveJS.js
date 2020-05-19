
var chatHistory = [];
var apigClient = null;
// const AWS =require('aws-sdk');
var url_string = window.location.href;
function callInputLambda() {
  alert("Inside sendMessageToApi");          
  var itext = document.getElementById('name-text').value.trim()
  var ptext = document.getElementById('phonenumber-text').value.trim()
  var link = window.location.href;
            alert(link)
            var faceid;
            // var fileName;
            if (link) {
                console.log(link)
                link = link.split('?')[1];
                console.log("link",link)
                // var arr = link.split('&');
                for (var i = 0; i < link.length; i++) {
                    var a = link.split('=');
                    console.log(a)
                    if (a[0] == "faceId") {
                        faceid = a[1];
                        console.log("faceid", faceid)
                    }
                //     if (a[0] == "fileName") {
                //         s3key = a[1];
                //     }
                }
            }
            alert(" Here " + faceid)
            console.log(faceid)
            //alert(" Here 2 " + fileName)
  // var inputText = itext.toLowerCase();
  document.getElementById('name-text').value = "";
  if(itext == "") {
    alert("Sorry! You entered an invalid name.");
    return false;
  }
  else {
    // chatHistory.push("User: " + itext);
    // chatHistory.push("User: " + ptext);
    // document.getElementById('chat-output').innerHTML = "";
    // chatHistory.forEach((element) => {
    //   document.getElementById('chat-output').innerHTML += "<p>" + element + "</p>";
     };
     console.log(itext,ptext);
  setTimeout(chatbotResponse, 500, itext, ptext, faceid);
  
  return false;
  
  //return chatbotResponse(inputText,phonenumberText);
}


function chatbotResponse(itext, ptext, faceid) {
  // return AWS.config.credentials.getPromise()
  // .then(()=>{
  //   console.log('Successfully logged!');
  apigClient = apigClientFactory.newClient({
  //     accessKey: AWS.config.credentials.accessKeyId,
  //     secretKey: AWS.config.credentials.secretAccessKey,
  //     // sessionToken: AWS.config.credentials.sessionToken
     });
    var params = {
      
    };
    var body = {
      "name":itext,
      "phonenumber":ptext,
      "faceid":faceid
    };
    var additionalParams = {
      // headers: {
      //   'x-api-key': 'Your API KEY'
      // },
      // queryParams: {}
    };
    console.log(body)
    return apigClient.visitorPost(params,body,additionalParams)
  // // })
  //  .then((result) =>{
  //   r1 = result["data"];
  //   console.log(r1);
  //   // r2 = JSON.stringify(r1);
  //   // r3 = r2.substring(3, r2.length-3);
  //   if (r1=='false'){
  //     chatHistory.push("you can not enter through the virtual door");
  //   }
  //   else{
  //     chatHistory.push(r1 + " you can enter through the virtual door");
  //   }
   
  //     document.getElementById('chat-output').innerHTML = "";
  //     // console.log(result.message)
  //     chatHistory.forEach((element) => {
  //       document.getElementById('chat-output').innerHTML += "<p>" + element + "</p>";
  //     });
  // })
  .catch((err) =>{
    console.log(err);
  });
 }











// var chatHistory = [];
// var apigClient = null;
// // const AWS =require('aws-sdk');
// var url_string = window.location.href;
// function callInputLambda() {
//   var itext = document.getElementById('name-text').value.trim()
//   // var inputText = itext.toLowerCase();
//   document.getElementById('name-text').value = "";
//   if(itext == "") {
//     alert("Sorry! You entered wrong OTP.");
//     return false;
//   }
//   else {
//     chatHistory.push("User: " + itext);
//     // chatHistory.push("User: " + ptext);
//   //   document.getElementById('chat-output').innerHTML = "";
//   //   chatHistory.forEach((element) => {
//   //     document.getElementById('chat-output').innerHTML += "<p>" + element + "</p>";
//      };
//   setTimeout(chatbotResponse, 500, itext);
  
//   return false;
  
//   //return chatbotResponse(inputText,phonenumberText);
// }

// function chatbotResponse(itext) {
//   // return AWS.config.credentials.getPromise()
//   // .then(()=>{
//   //   console.log('Successfully logged!');
//   apigClient = apigClientFactory.newClient({
//   //     accessKey: AWS.config.credentials.accessKeyId,
//   //     secretKey: AWS.config.credentials.secretAccessKey,
//   //     // sessionToken: AWS.config.credentials.sessionToken
//      });
//     var params = {
      
//     };
//     var body = {
//       "otp":itext
//     };
//     var additionalParams = {
//       // headers: {
//       //   'x-api-key': 'Your API KEY'
//       // },
//       // queryParams: {}
//     };
//     console.log(body)
//     return apigClient.validateOTPPost(params,body,additionalParams)
//   // // })
//   //  .then((result) =>{
      
//   //     chatHistory.push("Bot: " + result.message);
//   //     document.getElementById('chat-output').innerHTML = "";
//   //     console.log(result.message)
//   //     chatHistory.forEach((element) => {
//   //       document.getElementById('chat-output').innerHTML += "<p>" + element + "</p>";
//   //     });
//   // })
//   // .catch((err) =>{
//   //   console.log(err);
//   // });
//  }


