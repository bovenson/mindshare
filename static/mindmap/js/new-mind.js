/* js 提交创建主题请求 */
var POST_NEW_MIND = {
    actionUrl: '/new-mind/',
    actionForm: '#newMindForm',
    postSuccess: function (data) {
        if (data['res'] === 'error') {
            // 出错
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
        $('#titleTip').text('');
        $('#descriptionTip').text('');
        $('#imgTip').text('');
        $('#shareTip').text('');
        $('#mindmapTip').text('');
        $('#categoryTip').text('');

        this.doAction();
    }
};

/* 绑定事件 */
$("#submitBtn").click(function () {
    POST_NEW_MIND.action();
});

/* 分类管理 */
// 获取所有分类
var CATEGORYS = {
    categoryFirst: $('#categoryFirst'),
    categorySecond: $('#categorySecond'),
    categorys: [],
    get: function () {
            var ajaxOptions = {
                url: '/category/show',
                type: "post",
                success: function (data) {
                    CATEGORYS.categorys = data['categorys'];
                    CATEGORYS.categoryFirst.change();
                },
                error: function () {
                    $('#categoryTip').text('获取分类列表失败');
                }
            };
            $.ajax(ajaxOptions);
        },
    getCategorySecondList: function (selected) {
        var res = [];
        for (var i=0; i < CATEGORYS.categorys.length; ++i) {
            if (String(CATEGORYS.categorys[i]['parent']) === String(selected)) {
                res.push(CATEGORYS.categorys[i]);
            }
        }
        return res;
    },
    getSelected: function () {
        return CATEGORYS.categoryFirst.children('option:selected').val();
    },
    changeSelect: function () {
        var selected = CATEGORYS.getSelected();
        CATEGORYS.categorySecond.children().remove();
        var list = CATEGORYS.getCategorySecondList(selected);
        for (var i=0; i < list.length; ++i) {
            var newElement = document.createElement('option');
            newElement.value = list[i]['id'];
            newElement.text = list[i]['title'];
            CATEGORYS.categorySecond.append(newElement);
        }
    },
    registerListener: function () {
        CATEGORYS.categoryFirst.change(function () {
            CATEGORYS.changeSelect();
        });
    },
    init: function () {
        CATEGORYS.get();
        CATEGORYS.registerListener();
    }
};
CATEGORYS.init();
