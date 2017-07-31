/** 点击用户名显示popover窗体 **/
var usernameElement = $("#usernameElement");
var userPopoverModal = $("#userPopoverModal");
var userPopoverModalNode = document.getElementById("userPopoverModal");
// 绑定事件
usernameElement.click(showUserPopover);
// 显示弹出层
function showUserPopover(event) {
    // console.log($(this).offset().top, $(this).offset().left);
    var clientX = event.target.offsetWidth / 2 - userPopoverModalNode.offsetWidth / 2 + $(this).offset().left;
    var clientY = $(this).offset().top + event.target.clientHeight + 18;
    userPopoverModal.css('visibility', 'visible');
    userPopoverModal.css('top', clientY + "px"); // 63px
    userPopoverModal.css('left', clientX + "px");
}

// 监听页面时间
document.onmousedown = function (event) {
    // 如果点击位置在弹出框内
    // console.log(event.srcElement);
    if (isParent(userPopoverModalNode, event.srcElement)) {
    } else { // 否则
        userPopoverModal.css('visibility', 'hidden');
    }
};

// 判断ea是不是eb的父节点
function isParent(ea, eb) {
    if (eb) {
        while (eb.parentNode) {
            eb = eb.parentNode;
            if (ea === eb) {
                return true;
            }
        }
        return false;
    }
    return false;
}

// 页面大小改变时
window.onresize = function(){
    // 隐藏popover窗体
    userPopoverModal.css('visibility', 'hidden');
};