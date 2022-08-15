from .models import Category
from user_profile.models import Address

from user_profile.models import User
def categories(request):
    return {"categories":Category.objects.all()}

'''def ShoppingCart(request):
    if request.user is not None and request.user.is_authenticated:
        return {"ShoppingCart":request.user.UserShoppingCartRelatedName.all()}
    else:
         return {}'''




 