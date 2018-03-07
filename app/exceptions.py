from rest_framework.exceptions import APIException


class TopicNotFoundException(APIException):
    status_code = 404
    default_detail = 'Topic with given id not available'
    default_code = 'topic_unavailable'
