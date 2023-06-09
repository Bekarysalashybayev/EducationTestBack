from rest_framework import pagination


class StandardPagination(pagination.PageNumberPagination):
    """ Стандартная Пагинация """
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000
