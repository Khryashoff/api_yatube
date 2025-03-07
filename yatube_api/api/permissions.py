from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Проверка разрешений для объекта.

    Аутентифицированным пользователям доступно только чтение.
    Аутентифицированные авторы публикаций могут редактировать или удалять их.
    """
    def has_object_permission(self, request, view, obj):
        """
        Проверяет, имеет ли пользователь право на данное действие над объектом.
        """
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
