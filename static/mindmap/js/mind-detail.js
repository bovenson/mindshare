/* 删除 Mindmap */
function voteAction(mindmapId) {
    var voteA = $("#voteA");
    var voteNumber = $("#voteNumber");
    var data = {
        id: mindmapId
    };

    var callBack = function (data) {
        if(data["res"] === "success") {
            if (data["action"] === "vote") {
                voteA.css('color', '#009688');
                voteNumber.text(data["vote"]);
            } else if (data["action"] === "devote") {
                voteA.css('color', '#BDBDBD');
                voteNumber.text(data["vote"]);
            }
        } else if (data["res"] === "error") {
            if (data["action"] === "login") {
                triggerLogin();
            }
            toastr["error"](data["msg"]);
        }
    };

    var postError = function (data) {
        toastr['error']("请求失败");
    };

    postAction("/mind/vote/", data, callBack, postError);
}