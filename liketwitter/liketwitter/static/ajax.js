$(function() {
    $("#signUpSubmitButton").click(function() {
	$.ajax({
	    url: "/signup",
	    data: $("#signupform").serialize(),
	    type: "POST",
	    success: function(response) {
	        console.log(response);
	    },
	    error: function(error) {
	        console.log(error);
            },
	}); 
    });
});
	       
