/* 反馈弹窗 */

function feedbackBtnClick() {
    $("#feedbackModal").modal("show");
}

function sendFeedback() {
    var feedbackContentElement = $("#feedbackContent");
    var feedbackContent = feedbackContentElement.val();
    var actionUrl = $("#feedbackUrl").text();

    var postData = {
        content: feedbackContent
    };

    var ajaxOptions = {
        url: actionUrl,
        type: "post",
        dataType: "json",
        data: postData,
        success: function(data) {
            if (data["res"] === "success") {
                toastr["success"]("你的意见被记下了");
            } else {
                toastr["error"]("出现了些问题... : " + data["msg"]);
            }
        },
        error: function() {
            toastr["error"]("你的请求发送失败了, 然而这是我的错... 你可以稍后重试")
        }
    };

    // 发送请求
    $.ajax(ajaxOptions);
}
