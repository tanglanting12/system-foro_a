/**
 * Created by administrator on 14-4-9.
 */
document.write("<script language=javascript src='../../resource/js/leave.js'></script>");
var nowpage = 1;
var checkValue=0;
$(".timesearch").change(function(){
    checkValue=$(".timesearch").val();
    loadXMLDoc("/exceptiondataajax?index="+nowpage+"&name="+name+"&superiorStyle="+superiorStyle+"&checkvalue="+checkValue,"exceptiondata");
});

$('#paging_right,#paging_left').click( function (){
    if(this.id == "paging_left")
       step = -5;
    else if(this.id == "paging_right")
       step=5;
    navigate_control(step);
});
if( nowpage == 1 )
$("#beforepage").attr("disabled","disabled");//设置所有的button不可用  $(":button").removeAttr("disabled");//去掉button的disabled属性，使button可用



$('#beforepage').click(function(){
 if  ( nowpage > 1){
      nowpage -= 1;
 }
 else
      $("#beforepage").attr("disabled","disabled");
 $("#afterpage").removeAttr("disabled");
 document.getElementById("nowpage").innerHTML = nowpage;
 loadXMLDoc("/exceptiondataajax?index="+nowpage+"&name="+name+"&superiorStyle="+superiorStyle,"exceptiondata");
 }
);

$('#afterpage').click(function(){
  nowpage += 1;
  if(nowpage == 2)
     $("#beforepage").removeAttr("disabled");
  document.getElementById("nowpage").innerHTML = nowpage;
  loadXMLDoc("/exceptiondataajax?index="+nowpage+"&name="+name+"&superiorStyle="+superiorStyle,"exceptiondata");
 }
);

loadXMLDoc("/exceptiondataajax?index="+nowpage+"&name="+name+"&superiorStyle="+superiorStyle,"exceptiondata");
//navigate_control();
