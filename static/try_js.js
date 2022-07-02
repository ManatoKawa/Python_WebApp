function change_table(){
    // table_obj = document.getElementById('table_id');
    table_obj = document.getElementById('select_id');
    if(flag){
        table_obj.style.backgroundColor = "red";
        flag=false;
    }else{
        table_obj.style.backgroundColor ="";
        flag=true;
    }
    
    
}
let flag=true;

function change_by_select(){
    select_obj = document.getElementById('select_id');
    table_obj = document.getElementById('table_id');
    table_obj.style.backgroundColor = select_obj.value;
}