from .views import *

class LogUserView(ViewSet):
    pagination_class = CustomPagination()
    
    def post_log_user(self, request):
        data = request.data.copy()
        data_token = {
            'userId': '11785',
            'email': 'kimnt7@fpt.com.vn',
            'fullName': 'Nguyễn Trọng Kim',
            'isTinPncEmployee': 0,
            'jobTitle': '',
            'childDepart': '',
            'agency': '',
            'parentDepart': '',
            'branch': ''
        }
        if data_token is None:
            return response_data()
        status, data_save_log = self.data_log_user(data, data_token)
        if not status:
            return response_data(message=ERROR['NO_DATA'], status=STATUS['NO_DATA'])
        data_log = LogUserSerializer(data=data_save_log)
        if not data_log.is_valid():
            return validate_error(data_log.errors)
        add_log.apply_async(kwargs={'value':data_log.data})
        return response_data(data_log.data)
    
    def data_log_user(self, data, data_token):
        if 'input' in data.keys():
            data_input = data['input']
        else:
            data_input = data
        queryset = LogRouteAction.objects.filter(web_route=data['webRoute'], api_route=data['apiRoute'])
        if not queryset.exists():
            return False, {}
        if queryset.count() > 1:
            json_params_check = LogRouteActionSerializer(queryset, many=True)
            validation = InputValidate(data={'actionRoute':json_params_check.data,'data':data_input})
            if not validation.is_valid():
                return False, {}
            try:
                queryset = queryset.filter(json_params_required=validation.data['str_json_param_required'])
            except:
                return False, {}
        data_log = LogRouteActionSerializer(queryset.values()[0], fields=['functionCode','functionName','actionCode','actionName','serviceName'])
        data_token.update(data_log.data)
        data_token['webBrower'] = None
        data_token['apiInput'] = json.dumps(data)
        return True, data_token
    
    def get_log_user(self, request):
        queryset = LogUser.objects.filter()
        paginator = self.pagination_class
        pageSize = paginator.get_page_size(request=request)
        pagina = paginator.paginate_queryset(queryset=queryset, request=request)
        serializer = LogUserSerializer(pagina, many=True)
        return response_paginator(queryset.count(), pageSize, serializer.data)
        
    def search_log_user(self, request):
        data = request.data.copy()
        validate = DatetimeValidate(data=data)
        if not validate.is_valid():
            return validate_error(validate.errors)
        
        from_datetime = datetime.combine(validate.validated_data['startDate'], datetime.min.time())
        to_datetime = datetime.combine(validate.validated_data['endDate'], datetime.max.time())
        
        if 'name' in data.keys():
            queryset = LogUser.objects.filter(full_name__icontains=data['name'], date_created__range=[from_datetime, to_datetime])
        elif 'email' in data.keys():
            queryset = LogUser.objects.filter(email__icontains=data['email'], date_created__range=[from_datetime, to_datetime])
        else:
            return response_data(message=ERROR['NO_INPUT'], status=['INPUT_INVALID'])
        
        paginator = self.pagination_class
        pageSize = paginator.get_page_size(request=request)
        pagina = paginator.paginate_queryset(queryset=queryset, request=request)
        searchSerializer = LogUserSerializer(pagina, many=True)
        return response_paginator(queryset.count(), pageSize, searchSerializer.data)