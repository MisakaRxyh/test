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
        if (validate_required(search, "请输入查询内容") == false) {
            search.focus();
            return false
        }
    }

}