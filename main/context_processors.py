from .models import Collection

def user_collection(request):
    if request.user.is_authenticated:
        active_user = request.user
        collection = Collection.objects.filter(user=active_user)
        return {'user_collection': collection}
    else:
        return {}