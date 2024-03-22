"""imported modules"""
from django.http import HttpResponse

def allowed_users(allowed_roles=[]):
    """Decorator to separate roles"""
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                print(group)
                if group in allowed_roles or not allowed_roles:
                    return view_func(request, *args, **kwargs)
            return HttpResponse("You are not allowed to view this")
        return wrapper_func
    return decorator