from rest_framework.pagination import PageNumberPagination


class SmallPagination(PageNumberPagination):
    page_size = 2


class LargePagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'sayfa'
