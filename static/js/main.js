const dropBtn = document.getElementById("dropBtn");
const dropBtn2 = document.getElementById("dropBtn2");
const hamMenu = document.getElementById("hamMenu");
dropBtn.onclick = function (e) {
    document.getElementById("dropMenu").classList.toggle("show");
};

dropBtn2.onclick = function (e) {
    document.getElementById("dropMenu3").classList.toggle("show");
};

hamMenu.onclick = function (e) {
    document.getElementById("dropMenu2").classList.toggle("show");
};
// // إغلاق القائمة عند النقر خارجها
// window.onclick = function (e) {
//     if (!e.target.matches("#dropBtn")) {
//         if (dropMenu.classList.contains("show")) {
//             dropMenu.classList.remove("show");
//         }
//     }
// };
