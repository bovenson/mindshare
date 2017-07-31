var POST_UPDATE_PROFILE = {
    actionUrl: '/user/profile/update/',
    actionForm: '#userProfileForm',
    postSuccess: function (data) {
        if (data['res'] === 'error') {
            // 出错
            console.log(data);
            var msg = data['msg'];
            for (var i=0; i < msg.length; ++i) {
                if (msg[i][1]) {
                    var errorMsg = msg[i][1].replace('.', '').replace('。', '');
                    $('#' + msg[i][0] + 'Tip').text(errorMsg);
                }
            }
        } else {
            location.href = '/';
        }
    },
    postError: function () {
        $('#titleTip').text('向服务器发送请求失败!');
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
        $('#nicknameTip').text('');
        $('#passwordTip').text('');
        $('#new_passwordTip').text('');

        this.doAction();
    }
};

/* 绑定事件 */
$("#updateProfileSubmitBtn").click(function () {
    POST_UPDATE_PROFILE.action();
});
