// 跨域请求保护
var csrftoken = $.cookie('csrftoken');

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$(document).ready(function () {
    toastr.options = {
        "closeButton": false,
        "debug": false,
        "newestOnTop": false,
        "progressBar": false,
        "positionClass": "toast-top-right",
        "preventDuplicates": false,
        "onclick": null,
        "showDuration": "300",
        "hideDuration": "500",
        "timeOut": "1200",
        "extendedTimeOut": "500",
        "showEasing": "swing",
        "hideEasing": "linear",
        "showMethod": "fadeIn",
        "hideMethod": "fadeOut"
    }
});

/* 触发登录 */
function triggerLogin() {
    $("#btn-login").click();
}

/* 确定/取消模态框 */
function showConfirmOrCancelModal(title, msg, confirm, cancel) {
    var confirmCancelModal = $("#confirmCancelModal");
    var confirmCancelModalTitle = $("#confirmCancelModalTitle");
    var confirmCancelModalText = $("#confirmCancelModalText");
    var confirmCancelModalConfirm = $("#confirmCancelModalConfirm");

    confirmCancelModalTitle.text(title);
    confirmCancelModalText.text(msg);
    confirmCancelModalConfirm.unbind('click');
    // 点击确定, 回调函数
    confirmCancelModalConfirm.click(confirm);
    confirmCancelModal.modal("show");
}

function postAction(url, data, callBack, postError) {
    var ajaxOptions = {
        url: url,
        type: "post",
        data: data,
        dataType: "json",
        success: callBack,
        error: postError
    };

    $.ajax(ajaxOptions);
}

/* 删除 Mindmap */
function deleteMindmap(mindmapId) {
    var data = {
        id: mindmapId
    };

    var callBack = function (data) {
        if(data["res"] === "success") {
            toastr["success"]("删除成功");

            var pathName=window.document.location.pathname;
            console.log(pathName);

            if (pathName.startsWith('mind/show') || pathName.startsWith('/mind/show')) {
                location.href = '/'
            } else {
                var mindmapDiv = $("#divMindmap" + mindmapId);
                if (mindmapDiv) {
                    mindmapDiv.remove();
                }
            }
        } else if (data["res"] === "error") {
            toastr["error"](data["msg"]);
        }
    };

    var postError = function (data) {
        toastr['error']("请求失败");
    };

    function doAction() {
        postAction("/mind/delete/", data, callBack, postError);
    }

    showConfirmOrCancelModal("删除思维导图", "确定要删除该导图吗?", doAction);
}