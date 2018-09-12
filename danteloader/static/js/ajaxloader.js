function getFormData(form) {
    var unindexed_array = form.serializeArray();
    var indexed_array = {};

    $.map(unindexed_array, function (n, i) {
        indexed_array[n['name']] = n['value'];
    });

    return indexed_array;
}


function ajax_load(url, div_selector, method, form_data, do_after_ajax) {
    //console.log('Загрузка');
    $.ajax({
            url: url,
            method: method,
            data: form_data,

            success: function (data) {
                //console.log(data);
                $(div_selector).html(data);
                //console.log('ajax done');
                if (do_after_ajax!==undefined)
                {
                    do_after_ajax();
                }
            },
        });
}

function get_selector(element_id) {
    return '#'+element_id;
}

GET = 'get'
POST = 'post'
//загрузка листа
function load_list(request_url, place_id, page) {
    if (page != undefined) {
       request_url += '?page='+page;
    }
    ajax_load(request_url, get_selector(place_id), GET);
}

//загрузка формы на создание и обновление
function load_edit(request_url, place_id, form_id, after_create) {
    ajax_load(request_url, get_selector(place_id), GET);

    //навешиваем обработчик на форму для пост запроса
    $(document).on('submit', get_selector(form_id), function(event){
        create_form = $(this);
        data = getFormData(create_form);
        ajax_load(request_url, get_selector(place_id), POST, data, after_create);
        event.preventDefault();
    })
}

//загрузка детальной информации
function load_detail(request_url, place_id) {
    ajax_load(request_url, get_selector(place_id), GET);
}


//удаление элемента
function load_delete(request_url, place_id, form_selector, after_delete) {
    ajax_load(request_url, get_selector(place_id), GET);

    $(document).on('submit', form_selector, function(event){
        delete_form = $(this);
        reques_url = delete_form.attr("action");
        data = getFormData(delete_form);
        ajax_load(reques_url, form_selector, POST, data, after_delete);
        event.preventDefault();
    })
}
