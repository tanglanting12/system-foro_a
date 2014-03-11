/**
 * Created by abert on 14-3-11.
 */
function daysBetween(DateOne,DateTwo)
{
    var OneMonth = DateOne.substring(5,DateOne.lastIndexOf ('-'));
    var OneDay = DateOne.substring(8,10);
    var OneYear = DateOne.substring(0,DateOne.indexOf ('-'));

    var TwoMonth = DateTwo.substring(5,DateTwo.lastIndexOf ('-'));
    var TwoDay = DateTwo.substring(8,10);
    var TwoYear = DateTwo.substring(0,DateTwo.indexOf ('-'));

    var cha=Math.abs(((Date.parse(OneMonth+'/'+OneDay+'/'+OneYear)- Date.parse(TwoMonth+'/'+TwoDay+'/'+TwoYear))/86400000));
    var onehour=parseInt(DateOne.substring(11,13));
    var twohour=parseInt(DateTwo.substring(11,13));
    hourbetween=twohour-onehour;
    if(onehour<=12&&twohour>=12)
       hourbetween=hourbetween-2
    if (hourbetween<4)
       cha+=0.5;
    else
       cha+=1;
    return cha;
}
function toggle(arr,arr_name,id){

    var arr_byname=document.getElementsByName(id);
    for(j=0;j<arr_byname.length;j++){
    for(i=0;i<arr.length;i++)
        if(arr_byname[j].innerHTML==arr[i]){
           arr_byname[j].innerHTML=arr_name[i];
           break;
        }
    }
}
function Calculateleaveday(arr_leave_time_begin,arr_leave_time_end,arr_daynum)
{

    for(j=0;j<arr_leave_time_begin.length;j++){
    var leave_begin=arr_leave_time_begin[j].innerHTML.substr(0,19)
    var leave_end=arr_leave_time_end[j].innerHTML.substr(0,19)
    arr_leave_time_begin[j].innerHTML=leave_begin
    arr_leave_time_end[j].innerHTML=leave_end
    arr_daynum[j].innerHTML=daysBetween(leave_begin,leave_end)
}
}

//**********************************************

