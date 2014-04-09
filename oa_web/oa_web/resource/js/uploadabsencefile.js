
$(document).on('change', '.btn-file :file',function() {
  var input = $(this),
  numFiles = input.get(0).files ? input.get(0).files.length : 1,
  label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
  input.trigger('fileselect', [numFiles, label]);
});

$(document).ready( function() {
	$('.btn-file :file').on('fileselect', function(event, numFiles, label) {
      var input = $(this).parents('.input-group').find(':text'),
	  log = numFiles > 1 ? numFiles + ' files selected' : label;
      if( input.length ) {
		input.val(log);
	  }
      else {
		if( log ) alert(log);
		}

	});
	});
function check(form)
 {
   var temp;
   temp=true;
   if(window.confirm("确定删除选中的数据？"))
   {
      temp=true;
      $("#btnAjaxForm").attr("disabled","disabled");
   }
   else
    {
      return false;
     }
      return temp;
   }

//
//        $(document).ready(function () {
//        var options = {
//             dataType: 'text',
//             data: $("#form1").serialize(),
//            success: function (data) {
//                $("#btnAjaxForm").removeAttr ("disabled");
//                $("#uploadfilediv").text(data);
//            }
//        };
//            // ajaxForm
//            $("#form1").ajaxForm(options);
//        });
$(function () {
   var options = {
       success: function (data) {
           $("#responseText").text(data);
       }
   };

   $("#form1").ajaxForm(options);
   });
