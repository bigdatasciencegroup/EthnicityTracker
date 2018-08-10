Ethnic.init = function(){
	$("#e_post_upload").hide();

	$("#e_file_upload").on('change', function(){
		Ethnic.readFile()

	});
}