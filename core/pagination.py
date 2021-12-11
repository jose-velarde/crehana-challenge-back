from rest_framework import pagination
from rest_framework.response import Response

class NoPagination(pagination.PageNumberPagination):
    page_size = 100
    
class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        if self.page.has_next():
            next = self.page.next_page_number()
        else:
            next = None

        if self.page.has_previous():
            previous = self.page.previous_page_number()
        else:
            previous = None

        return Response({
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'page_number': self.page.number,
            'next_url': self.get_next_link(),
            'next': next,
            'previous_url': self.get_previous_link(),
            'previous': previous,
            'results': data,
        })
