from rest_framework.viewsets import ViewSet
from helpers.response import response_data
from .tasks import *
from .models import *
from .serializer import *

class CeleryView(ViewSet):
    # def test(self, request):
    #     total.apply_async(args=(2, 2))
    #     return response_data()
    
    def getall(self, request):
        queryset = LogUser.objects.all()
        serializer = LogUserSerializer(queryset, many=True)
        return response_data(serializer.data)
    
    def write_log(self, request):
        list_data = [
            {
                'a': 'a',
                'b': 'b'
            },
            {
                'a': 'c',
                'b': 's'
            }
        ]
        test = TestSerializer(data=list_data, many=True)
        if not test.is_valid():
            return response_data(message='loi roi')
        # test.save()
        add_log.apply_async(kwargs={'value':test.data}, debug=False)
        return response_data(test.data)