// 登录注册
var loginBtnElement = $("#btn-login");
var registerBtnElement = $("#btn-register");
var registerOrLoginTipElement = $("#registerOrLoginTipElement");
var registerOrLoginBtnElement = $("#registerOrLoginBtnElement");
var inputEmailElement = $("#inputEmail");
var inputPasswordElement = $("#inputPassword");
var lrModalErrorTipElement = $("#lrModalErrorTipElement");

var registerStrTip = "还没有账号? 点击注册";
var loginStrTip = "已有账号? 点击登录";
var registerStr = "注册";
var loginStr = "登录";

loginBtnElement.click(loginBtnClick);
registerBtnElement.click(registerBtnClick);
registerOrLoginTipElement.click(actionTipClick);
registerOrLoginBtnElement.click(actionLoginOrRegister);

function loginBtnClick() {
    changeTextToLogin();
    $("#loginRegisterModelBox").modal("show");
}

function registerBtnClick() {
    changeTextToRegister();
    $("#loginRegisterModelBox").modal("show");
}

// 登录操作
function actionLoginOrRegister() {
    var tStr = registerOrLoginBtnElement.text();
    var loginUrl = "/user/login/";
    var registerUrl = "/user/register/";
    var curActionUrl = "";

    // 置空错误提示
    lrModalErrorTipElement.text("");

    // 获取输入
    var email = inputEmailElement.val();
    var password = inputPasswordElement.val();
    if (tStr === loginStr) {
        curActionUrl = loginUrl;
    } else if (tStr === registerStr) {
        curActionUrl = registerUrl;
    }

    var postData = {
        email: email,
        username: email,
        nickname: email,
        password: password
    };

    var ajaxOptions = {
        url: curActionUrl,
        type: "post",
        dataType: "json",
        data: postData,
        success: function(data) {
            if (data["res"] === "error") {
                setErrorTip(data["msg"]);
            } else if (data["res"] === "success") {
                // 登录/注册 成功, 刷新页面
                location.reload();
            } else {
                setErrorTip("服务器返回数据格式不正确")
            }
        },
        error: function() {
            setErrorTip("请求失败")
        }
    };

    // 发送请求
    $.ajax(ajaxOptions);
}

function setErrorTip(msg) {
    lrModalErrorTipElement.text(msg);
}

function actionTipClick() {
    var tStr = registerOrLoginBtnElement.text();
    if (tStr === loginStr) {
        changeTextToRegister();
    } else if (tStr === registerStr) {
        changeTextToLogin();
    }
}

function changeTextToLogin() {
    lrModalErrorTipElement.text("");
    registerOrLoginBtnElement.text(loginStr);
    registerOrLoginTipElement.text(registerStrTip);
}

function changeTextToRegister() {
    lrModalErrorTipElement.text("");
    registerOrLoginBtnElement.text(registerStr);
    registerOrLoginTipElement.text(loginStrTip);
}




function actionLogin() {
    $("#btn-login").click();
}
