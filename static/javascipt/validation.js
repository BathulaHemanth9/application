function validation(){
    let v1,v2;
    v1=document.getElementById('t1').value;
    v2=document.getElementById('t2').value;
    if(v1<0 || v2<0){
        window.alert("negative values are not allow")
        return false;
    }
    else{
        return true
    }
}