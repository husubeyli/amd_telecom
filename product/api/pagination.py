from urllib import parse
from rest_framework.response import Response
from rest_framework import pagination
from rest_framework.utils.urls import replace_query_param

class CustomProductPaginator(pagination.PageNumberPagination):

    # def get_paginated_response(self, data):
    #     return Response({
    #     'links': {
    #         'next': self.get_next_link(),
    #         'previous': self.get_previous_link()
    #     },
    #     'count': self.page.paginator.count,
    #     'products': data
    # })
    def get_paginated_response(self, data):
        return Response({   
            'page_size': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'list_pages_url': self.get_html_context(),
            'page_number': self.page.number,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'products': data 
        })


    # def get_next_link(self):
    #     if not self.page.has_next():
    #         return None
    #     page_number = self.page.next_page_number()
    #     print( self.page, 'urllik')
    #     url = self.request.build_absolute_uri()
    #     return replace_query_param(url, self.page_query_param, page_number)

    # def get_previous_link(self):
    #     if not self.page.has_previous():
    #         return None
    #     url = self.request.build_absolute_uri()
    #     page_number = self.page.previous_page_number()
    #     return replace_query_param(url, self.page_query_param, page_number)

    # # def replace_query_param(url, key, val):
    #     """
    #     Given a URL and a key/val pair, set or replace an item in the query
    #     parameters of the URL, and return the new URL.
    #     """
    #     (scheme, netloc, path, query, fragment) = parse.urlsplit(force_str(url))
    #     scheme = "http"
    #     netloc = "localhost:8000"
    #     query_dict = parse.parse_qs(query, keep_blank_values=True)
    #     query_dict[force_str(key)] = [force_str(val)]
    #     query = parse.urlencode(sorted(list(query_dict.items())), doseq=True)
    #     print(query, 'query')
    #     return parse.urlunsplit((scheme, netloc, path, query, fragment))
