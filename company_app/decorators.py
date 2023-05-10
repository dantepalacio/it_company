from django.contrib.auth.decorators import user_passes_test


def only_staf(my_view):
    
    def is_staff(user):
        return user.is_active and user.is_staff
    custom_decorator = user_passes_test(is_staff, login_url='/')
    return custom_decorator(my_view)