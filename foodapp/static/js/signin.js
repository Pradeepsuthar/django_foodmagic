// Sign Up / Login

function showLoginForm(){
  if(document.getElementById('registerForm').style.display=='block') {
    document.getElementById('registerForm').style.display='none';
  }
    document.getElementById('loginForm').style.display='block';
}

function showRegisterForm(){
  if(document.getElementById('loginForm').style.display=='none') {
    document.getElementById('loginForm').style.display='block';
  }
    document.getElementById('registerForm').style.display='block';
    document.getElementById('loginForm').style.display='none';
}
let userName = document.getElementById("inputEmail");
let password = document.getElementById("inputPassword");
let error = document.getElementById("err");

userName = "sutharpradeep081@gmail.com";
password = "123456";

function loginSucces(){
  
    if(userName && password)
    {
        // window.open("deshboard.html");
        window.open("main.html");
    }
    else{
        error.innerHTML = "Username and password is in correct.";
    }

}