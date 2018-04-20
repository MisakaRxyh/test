/**
 * Created by SoulPainterC on 2018/4/19.
 */
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
        if (validate_required(useraccount, "请输入账号") == false) {
            useraccount.focus();
            return false
        }
        else if (validate_required(userpwd, "请输入密码") == false) {
            userpwd.focus();
            return false
        }
    }

}
