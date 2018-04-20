/**
 * Created by SoulPainterC on 2018/4/19.
 */

var secs = 3; //倒计时的秒数
var URL;
function Load(url) {
    URL = url;
    for (var i = secs; i >= 0; i--) {
        window.setTimeout('doUpdate(' + i + ')', (secs - i) * 1000);
    }
}
function doUpdate(num) {
    document.getElementById('ShowDiv').innerHTML = '将在' + num + '秒后自动跳转到主页';
    if (num == 0) {
        window.location = URL;
    }
}

function validate_required(field, alerttxt) {
    with (field) {
        if (value == null || value == "") {
            alert(alerttxt);
            return false
        }
        else {
            return true
        }
    }
}

function validate_form(thisform) {
    with (thisform) {
        if (validate_required(useraccount, "账号不能为空") == false) {
            useraccount.focus();
            return false
        }
        else if (validate_required(username, "用户名不能为空") == false) {
            username.focus();
            return false
        }
        else if (validate_required(userpwd, "密码不能为空") == false) {
            userpwd.focus();
            return false
        }
        else if (validate_required(againpwd, "确认密码不能为空") == false) {
            againpwd.focus();
            return false
        }
    }

}