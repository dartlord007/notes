from rest_framework.decorators import api_view 
from rest_framework.response import Response 

@api_view(['GET']) #decorator, user can only GET data here
def getRoutes(request):
    routes = [
        {
            'Endpoint' : '/notes/',
            'method' : 'GET',
            'body' : None,
            'description' : 'Returns an array of notes',
        },
        {
            'Endpoint' : '/notes/id',
            'method' : 'GET',
            'body' : None,
            'description' : 'Returns a single note object',
        },
        {
            'Endpoint' : '/notes/create',
            'method' : 'POST',
            'body' : {'body': ""},
            'description' : 'Creates a new note with data sent in post request',
        },
        {
            'Endpoint' : '/notes/id/update',
            'method' : 'PUT',
            'body' : None,
            'description' : 'Creates data in existing note',
        },
        {
            'Endpoint' : '/notes/id/delete',
            'method' : 'DELETE',
            'body' : {'body':""},
            'description' : 'Deletes an existing note.',
        },
    ]
    return Response(routes)
