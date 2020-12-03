{% extends 'base.html' %}
{% load crispy_forms_tags %}
{% block head_title %}{{ template_title }}{% endblock %}

{% block content %}
    <script>
        $(document).ready(function(){
            $("#add-item").click(function(ev) {
                ev.preventDefault();
                var count = $('#order').children().length;
                var tmplMarkup = $("#item-order").html();
                var compiledTmpl = tmplMarkup.replace(/__prefix__/g, count);
                $("div#order").append(compiledTmpl);

                // update form count
                $('#id_product-TOTAL_FORMS').attr('value', count + 1);

                // some animate to scroll to view our new form
                $('html, body').animate({
                    scrollTop: $("#add-item").position().top-200
                }, 800);
            });
        });
    </script>

    <div class="row">
        <div class="col-md-6 col-md-offset-3">
            <h1 class="page-header text-center lead">Cadastro Pedido</h1>
        </div>
    </div>
    <div class="row">
        <div class="col-md-8 col-md-offset-2">
            <form action="" method="POST">
                {% csrf_token %}
                {{ forms|crispy }}
                {{ formset.management_form }}

                <legend class="lead">PRODUTOS</legend>

                <div id="order" class="form-inline form-group">
                    {% for item_order_form in formset %}
                        <div id="item-{{ forloop.counter0 }}">
                            {{ item_order_form|crispy }}
                        </div>
                    {% endfor %}
                </div>

                <a class="btn btn-info" id="add-item"><i class="fa fa-plus"></i> Add Item</a>

                <div class="form-inline buttons">
                    <a href="{% url 'order' %}" class="btn btn-warning pull-right"><i class="fa fa-times"></i> Cancelar</a>
                    <button class="btn btn-primary pull-right" value="Save"><i class="fa fa-floppy-o"></i> Salvar</button>
                </div>
            </form>
    </div>    

    <script type="text/html" id="item-order">
        <div id="item-__prefix__" style="margin-top: 10px">
                {{ formset.empty_form|crispy }}
        </div>
    </script>
{% endblock %}