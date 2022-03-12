



function PopUp(hideOrshow) {
    if (hideOrshow == 'hide') document.getElementById('ac-wrapper').style.display = "none";
    else document.getElementById('ac-wrapper').removeAttribute('style');
}
// window.onload = function () {
//     setTimeout(function () {
    
//         PopUp('show');
//     }, 2000);
// }



function ShowPopup(title, body) {
    $("#MyPopup .modal-title").html(title);
    $("#MyPopup .modal-body").html(body);
    $("#MyPopup").modal("show");
}

