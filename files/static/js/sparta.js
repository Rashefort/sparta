function toggle(id) {
    if (document.getElementById(id).style.display == "none") {
        $(".sign").slideToggle("slow");
    }
}


function getDate() {
    var date = new Date();

    var year = date.getFullYear();
    var month = ("0" + date.getMonth()).slice(-2);
    var day = ("0" + date.getDate()).slice(-2);
    var hours = ("0" + date.getHours()).slice(-2);
    var minutes = ("0" + date.getMinutes()).slice(-2);

    return day + "." + month + "." + year + " - " + hours + ":" + minutes;
}


function ajax_add(phone, note, date) {
    var request = new XMLHttpRequest();
    var data = new FormData();

    data.append("csrfmiddlewaretoken", document.forms.spartan.csrfmiddlewaretoken.value);
    data.append("phone", phone);
    data.append("note", note);
    data.append("date", date);

    request.open("POST", document.forms.spartan.action, false);
    request.send(data);

    return request.responseText;
}


function ajax_del(id) {
    var request = new XMLHttpRequest();
    var data = new FormData();

    data.append("csrfmiddlewaretoken", document.forms.spartan.csrfmiddlewaretoken.value);
    data.append("id", id);

    request.open("POST", document.forms.spartan.action);
    request.send(data);
}


function enter(event) {
    if (event.keyCode == 13) {
        add_note()
    }
}


function add_note() {
    var phone = document.getElementById("id_phone").value;
    var note = document.getElementById("id_note").value;
    var date = getDate();

    if (phone && note) {
        var id = JSON.parse(ajax_add(phone, note, date))["id"];
        var li = $("li#li_0").clone();

        li.attr("id", "li_" + id);
        li.css("display", "block");
        li.find(".input-phone").val(phone);
        li.find(".input-note").val(note);
        li.find("#a_0").attr("onclick", "del_note(" + id + ")");
        li.find("#a_0").attr("id", "a_" + id);

        li.find(".input-phone").attr("title", date);
        li.find(".input-note").attr("title", date);

        $("ul#spartan-table").prepend(li);
        document.getElementById("id_phone").value = "";
        document.getElementById("id_note").value = "";
    } else {
        $("ul.error").empty();

        if (phone == false) {
            $("ul.error").append("<li>Номер телефона</li>");
        }

        if (note == false) {
            $("ul.error").append("<li>Комментарий</li>");
        }

        $('#dialog').dialog("open");
    }

}

function confirmation(phone, note) {
    var defer = $.Deferred();
    $('<div></div>').html(note).dialog({
        title: phone,
        autoOpen: true,
        resizable: false,
        modal: true,
        width: 'auto',
        buttons: {
            "Удалить": function() {
                $(this).dialog("close");
                defer.resolve("true");
            },
            "Отмена": function() {
                $(this).dialog("close");
                defer.resolve("false");
            }
        },
        close: function () {
            $(this).remove();
        }
    });

    return defer.promise();
}


function del_note(id) {
    var phone = $("#li_" + id).children(".input-phone").val();
    var note = $("#li_" + id).children(".input-note").val();

    confirmation(phone, note).then(function(answer) {
        if(answer=="true"){
            document.getElementById("li_" + id).remove();
            ajax_del(id);
        }
    });
}
