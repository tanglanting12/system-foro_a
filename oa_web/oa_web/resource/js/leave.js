/**
 * Created by abert on 14-3-11.
 */
function daysBetween(DateOne,DateTwo){

    var OneMonth = DateOne.substring(5,DateOne.lastIndexOf ('-'));
    var OneDay = DateOne.substring(8,10);
    var OneYear = DateOne.substring(0,DateOne.indexOf ('-'));

    var TwoMonth = DateTwo.substring(5,DateTwo.lastIndexOf ('-'));
    var TwoDay = DateTwo.substring(8,10);
    var TwoYear = DateTwo.substring(0,DateTwo.indexOf ('-'));

    var cha = Math.abs(((Date.parse(OneMonth+'/'+OneDay+'/'+OneYear)- Date.parse(TwoMonth+'/'+TwoDay+'/'+TwoYear))/86400000));
    var onehour = parseInt(DateOne.substring(11,13));
    var twohour=parseInt(DateTwo.substring(11,13));
    onehour = onehour > 18 ? 18 : onehour;
    onehour = onehour < 9 ? 9 : onehour;
    twohour = twohour > 18 ? 18 : twohour;
    twohour = twohour < 9 ? 9 : twohour;
    hourbetween = twohour - onehour;

    if(onehour <= 12 && twohour >= 12)
       hourbetween = hourbetween-2
    if ( hourbetween > 0 && hourbetween < 4 )
       cha += 0.5;
    else
       cha += 1;
    return cha;
}
function toggle(arr,arr_name,id){
    var arr_byname = document.getElementsByName(id);
    for( j = 0 ; j < arr_byname.length ; j++ ){
    for( i = 0 ; i<arr.length ; i++ )
        if(arr_byname[j].innerHTML == arr[i]){
           arr_byname[j].innerHTML = arr_name[i];
           break;
        }
    }
}
function Calculateleaveday(arr_leave_time_begin,arr_leave_time_end,arr_daynum)
{

    for( j = 0 ; j < arr_leave_time_begin.length ; j++ ){

       var leave_begin = arr_leave_time_begin[j].innerHTML.substr(0,13)+'点';
       var leave_end = arr_leave_time_end[j].innerHTML.substr(0,13)+'点';
       arr_leave_time_begin[j].innerHTML = leave_begin;
       arr_leave_time_end[j].innerHTML = leave_end;
       arr_daynum[j].innerHTML = daysBetween(leave_begin,leave_end);
}
}


function afterleavedetailajax(){
    leave_type_id = ["0","1","2","3"];
    leave_type_name = ["事假","病假","外出","年假"];
    status_id = ["0","1"];
    status_name = ["未确认","确认"];
    toggle(leave_type_id,leave_type_name,"leave_type");
    toggle(status_id,status_name,"status");
    var arr_leave_time_begin = document.getElementsByName("leave_time_begin");
    var arr_leave_time_end = document.getElementsByName("leave_time_end");
    var arr_daynum = document.getElementsByName("day_num");
    var reaonforleaves = document.getElementsByName("reaonforleave");
    var usernames=document.getElementsByName("username");

    Calculateleaveday(arr_leave_time_begin,arr_leave_time_end,arr_daynum);
    for( i = 0 ; i<reaonforleaves.length ; i++){
      var lenReasonforLeaves = reaonforleaves[i].innerHTML;
    if( String(lenReasonforLeaves).length > 30)
    reaonforleaves[i].innerHTML = String(lenReasonforLeaves).substring(0,30);
    }
//    alert(usernames[2].innerHTML);

//    $( "#autocomplete" ).autocomplete({
//         source: function( request, response ) {
//                  var matcher = new RegExp( "^" + $.ui.autocomplete.escapeRegex( request.term ), "i" );
//                  response( $.grep( tags, function( item ){
//                  return matcher.test( item );
//                  }) );
//         }
//     });
    $('#searchUser').click(function(){
    var selectname=$('#autocomplete')
// val = $("#id")[0].value;    loadXMLDoc("/leave_detailajax?lastpage = 0&index = 1"+"&comfirm="+comfirm+"&name="+name+"&superiorStyle="+superiorStyle);
    loadXMLDoc("/leave_detailajax?index=1"+"&name="+selectname+"&comfirm="+comfirm+"&superiorStyle="+superiorStyle);
    }
   );
}
/*paging function*/
function navigate_control(step){
   if(!step) step = 0;
   pagings=document.getElementsByClassName("paging");
  for(j=0; j<pagings.length; j++){
      pagings[j].innerHTML = parseInt(pagings[j].innerHTML)+step;
      if (pagings[j].innerHTML<1) {
      pagings[j].innerHTML = parseInt(pagings[j].innerHTML)-step;
       break;
      }
      _TheArray[j] = "/leave_detailajax?lastpage=0&index="+pagings[j].innerHTML+"&comfirm="+comfirm+"&name="+name+"&superiorStyle="+superiorStyle;
  }
pagings[0].setAttribute("onclick","loadXMLDoc(_TheArray[0])");
pagings[1].setAttribute("onclick","loadXMLDoc(_TheArray[1])");
pagings[2].setAttribute("onclick","loadXMLDoc(_TheArray[2])");
pagings[3].setAttribute("onclick","loadXMLDoc(_TheArray[3])");
pagings[4].setAttribute("onclick","loadXMLDoc(_TheArray[4])");
}
//**********************************************

