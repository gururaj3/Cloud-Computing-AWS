
var chatHistory = [];
var apigClient = null;
// const AWS =require('aws-sdk');
var url_string = window.location.href;
// var cognito_token = url_string.substring(url_string.indexOf("=") + 1,url_string.indexOf("&"));

// AWS.config.region = 'us-east-1';
// AWS.config.credentials = new AWS.CognitoIdentityCredentials({
//   IdentityPoolId: 'Your Identity Pool ID',
// 	Logins: {
// 	   'cognito-idp.us-east-1.amazonaws.com/us-east-1_8MsV07uIJ': cognito_token
// 	}
// });

function callInputLambda() {
  var itext = document.getElementById('name-text').value.trim()
  // var inputText = itext.toLowerCase();
  document.getElementById('name-text').value = "";
  if(itext == "") {
    alert("Sorry! You entered wrong OTP.");
    return false;
  }
  else {
    chatHistory.push("User: " + itext);
    // chatHistory.push("User: " + ptext);
  //   document.getElementById('chat-output').innerHTML = "";
  //   chatHistory.forEach((element) => {
  //     document.getElementById('chat-output').innerHTML += "<p>" + element + "</p>";
     };
  setTimeout(chatbotResponse, 500, itext);
  
  return false;
  
  //return chatbotResponse(inputText,phonenumberText);
}

function chatbotResponse(itext) {
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
      "otp":itext
    };
    var additionalParams = {
      // headers: {
      //   'x-api-key': 'Your API KEY'
      // },
      // queryParams: {}
    };
    console.log(body)
    return apigClient.validateOTPPost(params,body,additionalParams)
  // // })
  //  .then((result) =>{
      
  //     chatHistory.push("Bot: " + result.message);
  //     document.getElementById('chat-output').innerHTML = "";
  //     console.log(result.message)
  //     chatHistory.forEach((element) => {
  //       document.getElementById('chat-output').innerHTML += "<p>" + element + "</p>";
  //     });
  // })
  // .catch((err) =>{
  //   console.log(err);
  // });
 }


