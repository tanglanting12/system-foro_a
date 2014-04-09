/**
 * Created by administrator on 14-4-9.
 */
$(function(){
			$('*[name=leave_time_begin]').appendDtpicker();
            $('*[name=leave_time_end]').appendDtpicker();
		});

$(window).on('load', function () {
		    $('.selectpicker').selectpicker({
				'selectedText': 'cat'
            });
							               // $('.selectpicker').selectpicker('hide');
});
