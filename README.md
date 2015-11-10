# Avito Analytical Recommendation Service

* [Confluence requirements documentation](https://cf.avito.ru/display/CFAA/CRM+Requirements)

## Usage

```
./grapheditor/web.py  # to run web server on localhost:5000 with graph editor.
```

## Administration

TODO.

# Структура таблиц

### Table: recommendations

| recommendation_id |	user_id | local_item_id |	score |	gen_date | recom_model | reason |
| ------------- | --------- | ---------- | ------ | ---------- | ----------- | ------- |
| | из вертики | из postgres (по нему джоиним recommended_items) | любое вещественное число | дата генерации рекомендации |	тип модели _ версия модели |  отладочная информация, почему порекомендовали |

### Table: recommended_items

| local_item_id | external_id | title  | image | price | param1 | param2                      | tag                           |	location_id | category_id  | active  |
| ------------- | ------------| ------ | ----- | ----- | ------ | ------ | ---                | ---                           | ----------- | ------------ | ------- |
|               | бэкофисный  |        |       |       | параметр, специфичный для категории || Является ли item актуальным.  |             |              |         |

