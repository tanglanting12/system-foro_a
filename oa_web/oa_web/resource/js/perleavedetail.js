
    leave_type_id=["0","1"];
    leave_type_name=["事假","病假"];
    status_id=["0","1"];
    status_name=["未确认","确认"];
    toggle(leave_type_id,leave_type_name,"leave_type");
    toggle(status_id,status_name,"status");
    var arr_leave_time_begin=document.getElementsByName("leave_time_begin");
    var arr_leave_time_end=document.getElementsByName("leave_time_end");
    var arr_daynum=document.getElementsByName("day_num");
    Calculateleaveday(arr_leave_time_begin,arr_leave_time_end,arr_daynum);
