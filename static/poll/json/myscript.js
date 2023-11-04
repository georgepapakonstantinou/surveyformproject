var disel = document.getElementById("NO")
var result = disel.input[disel.selectedIndex].text;
  if (result == 'No'){

    document.getElementById("No").diasabled=true;
    document.getElementById("Medium").disabled=true;
    document.getElementById("Full").disabled=true;


  }else{

    document.getElementById("No").diasabled=false;
    document.getElementById("Medium").disabled=false;
    document.getElementById("Full").disabled=false;
  }
