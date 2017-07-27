/* js 提交创建主题请求 */
var POST_NEW_MIND = {
    actionUrl: '/new-mind/',
    actionForm: '#newMindForm',
    postSuccess: function (data) {
        console.log('post success', data);
    },
    postError: function () {
        console.log('post error');
    },

    check: function () {
    },
    doAction: function () {
        var actionForm = $(this.actionForm);
        var formData = new FormData(actionForm[0]);
        var ajaxOptions = {
                url: this.actionUrl,
                type: "post",
                data: formData,
                processData: false,
                contentType: false,
                cache: false,
                success: this.postSuccess,
                error: this.postError
            };

        $.ajax(ajaxOptions);
    },
    action: function () {
        this.doAction();
    }
};

/* 绑定事件 */
$("#submitBtn").click(function () {
    POST_NEW_MIND.action();
});
