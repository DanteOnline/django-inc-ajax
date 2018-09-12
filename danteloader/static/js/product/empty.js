//Продукты
model_name_p = 'product'
load_list(model_name_p+'/list/', 'true_product_list');
f = function() {
    load_list(model_name_p+'/list/', 'true_product_list');
}
load_edit(model_name_p+'/create/', 'true_product_edit', 'product_create_form', f);


//Категории
model_name = '/category'

load_list(model_name+'/list/', 'product_list');
f = function() {
    load_list(model_name+'/list/', 'product_list');
    // при создании обновлении категории обнавляем форму с продуктом
    load_edit(model_name_p+'/create/', 'true_product_edit', 'product_create_form', f);
}
number_input = $('#page');

$(document).on('change', '#page', function(event) {
   val = $(this).val();
   load_list(model_name+'/list/', 'product_list', val);
})

load_edit(model_name+'/create/', 'product_edit', 'create_form', f);

// обработчик прописываем тут:
$(document).on('click', '.btn-detail', function (event) {
    // console.log('Клик на кнопку');
    var button_detail = $(this);

    // получаем id
    item_id = button_detail.data('id');
    url = model_name+"/detail/" + item_id + '/'
    //Шлем аякс запрос
    load_detail(url, 'category_detail');
    event.preventDefault();
});

$(document).on('click', '.btn-update', function (event) {
    // console.log('Клик на кнопку');
    var btn_update = $(this);

    // получаем id
    item_id = btn_update.data('id');
    //console.log(item_id);
    //Шлем аякс запрос
    url = model_name+"/update/" + item_id + '/'

    load_edit(url, 'product_edit', 'update_form', f);
    event.preventDefault();
});

$(document).on('click', '.btn-delete', function (event) {

        var btn = $(this);

        // получаем id
        item_id = btn.data('id');

        url = model_name+"/delete/" + item_id + '/'
        place_id = 'div-delete-'+item_id
        //Шлем аякс запрос
        load_delete(url, place_id, '.delete-form', f);
        event.preventDefault();
    });

