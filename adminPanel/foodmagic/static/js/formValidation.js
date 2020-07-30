//From Validation
$(document).ready(function () {
    $('#nameError').hide();
    $('#mobileError').hide();
    $('#emailError').hide();
    $('#passError').hide();
    $('#cpassError').hide();

    var name_error = true;
    var mobile_error = true;
    var email_error = true;
    var pass_error = true;
    var cpass_error = true;
    var checkBox = true;

    //checkname() call
    $('#name').keyup(function () {
        checkName();
    });

    //checkname() Define
    function checkName() {
        var name_val = $('#name').val();
        //Check Name is Empty
        if (name_val.length == '') {
            $('#nameError').show();
            $('#nameError').html("You cannot have an empty Name input field");
            $('#nameError').focus();
            $('#nameError').css("color", "red");
            name_error = false;
            return false;
        } else {
            $('#nameError').hide();
        }
    }

    //checkMobile() call
    $('#mobile').keyup(function () {
        checkMobile();
    });

    //checkMobile() Define
    function checkMobile() {
        var mobile_val = $('#mobile').val();
        //Check Name is Empty
        if (mobile_val.length != 10) {
            $('#mobileError').show();
            $('#mobileError').html("Mobile should be contain only 10 digits..");
            $('#mobileError').focus();
            $('#mobileError').css("color", "red");
            mobile_error = false;
            return false;
        } else {
            $('#mobileError').hide();
        }
    }

    //checkEmail() call
    $('#email').keyup(function () {
        checkEmail();
    });

    //checkEmail() Define
    function checkEmail() {
        var email_val = $('#email').val();
        //Check Email is Empty
        if (email_val.length == '') {
            $('#emailError').show();
            $('#emailError').html("You cannot have an empty Email input field");
            $('#emailError').focus();
            $('#emailError').css("color", "red");
            email_error = false;
            return false;
        } else {
            $('#emailError').hide();
        }

        //Check Email is uniqe
        var uniqe = email_val.endsWith("@gmail.com");

        if (!uniqe) {
            $('#emailError').show();
            $('#emailError').html("Invaild Email Address");
            $('#emailError').focus();
            $('#emailError').css("color", "red");
            email_error = false;
            return false;
        } else {
            $('#emailError').hide();
        }
    }

    //checkPassword() call
    $('#pass').keyup(function () {
        checkPassword();
    });

    $('#cpass').keyup(function () {
        checkPassword();
    });

    //checkPassword() Define
    function checkPassword() {
        var pass_val = $('#pass').val();
        var cpass_val = $('#cpass').val();
        //Check password is Empty
        if (pass_val.length == '') {
            $('#passError').show();
            $('#passError').html("You cannot have an empty Password input field");
            $('#passError').focus();
            $('#passError').css("color", "red");
            pass_error = false;
            return false;
        } else {
            $('#passError').hide();
        }

         //Check confirm password is Empty
        if (cpass_val.length == '') {
            $('#cpassError').show();
            $('#cpassError').html("You cannot have an empty Confirm Password input field");
            $('#cpassError').focus();
            $('#cpassError').css("color", "red");
            cpass_error = false;
            return false;
        } else {
            $('#cpassError').hide();
        }

        if(pass_val != cpass_val)
        {
            $('#cpassError').show();
            $('#cpassError').html("Password and Confirm Password are not match");
            $('#cpassError').focus();
            $('#cpassError').css("color", "red");
            cpass_error = false;
            return false;
        } else {
            $('#cpassError').hide();
        }
    }


    $('#agreements').click(function () {
        checkBox();
    });

    function checkBox() {
        if($(this).is(":checked") == true && $(this).is(":checked") == false){
            checkBox = true;
            return true;
        }
        else{
            checkBox = false;
            alert("Please checked Terms &  Conditions");
        }
    }

 

    $('#submit').click(function () {
        name_error = true;
        mobile_error = true;
        email_error = true;
        pass_error = true;
        cpass_error = true;
        checkBox = true;

        checkName();
        checkMobile();
        checkEmail();
        checkPassword();

        if ((name_error == true) && (mobile_error == true) && (email_error == true) && (pass_error == true) && (cpass_error == true) && (checkBox == true)) {
            return false;
        }
        else {
            return true;
        }
    });
});

