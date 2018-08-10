Ethnic = {
	readFile: function(){
	    var preview = document.querySelector('#e_actual_image');
	    var file    = document.querySelector('input[type=file]').files[0];
	    var reader  = new FileReader();
	    	
		reader.readAsDataURL(file); //Takes input and changes it into image

	    $(reader).load(function () {
	    	$(preview).attr('src', reader.result) //make the src attribute the result of the file reader
	    	Ethnic.data.readerURL = reader.result
	    });

	    Ethnic.uploadImage();
	},

	uploadImage: function(){
		$(".e-upload-border").css({'border': 'solid 1px #91C6FF'})
		$("#e_pre_upload").hide();
		$("#e_post_upload").show();
		$("#test").attr('src', Ethnic.data.readerURL)
	}
	    
}
Ethnic.data = {
	readerURL: ""
}

$(document).ready(function () {
	$(document).foundation();
	Ethnic.init()
});

