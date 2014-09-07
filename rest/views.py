# Create your views here.
from utils import compose_sql,execute_query
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


key_mapping = {
    'date' : 'date'
    ,'instance':'exec_id'
    ,'list': 'type'
}

@require_http_methods(['GET'])
def query_metadata(request,**kwargs):
    sql = compose_sql(kwargs['query'],kwargs[key_mapping[kwargs['query']]])
    #print(sql)
    result = execute_query(sql)
    response = HttpResponse(result,content_type="text/plain")
    return response



