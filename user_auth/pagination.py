from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10 # Сколько объектов на страницу по умолчанию
    page_size_query_param = 'page_size'# Позволяет переопределить из запроса ?
    max_page_size = 100 # Максимум разрешённых объектов на страницу
