from rest_framework.permissions import BasePermission
from rest_framework.views import Request, View
from .models import User
import pdb

class IsOwner(BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User):
        if request.user.is_employee:
            return True
        
        return obj == request.user

