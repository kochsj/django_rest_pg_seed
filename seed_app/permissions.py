from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # read only allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        #write permissions are only allowed for the author
        # return obj.<model_fk_attribute> == request.user