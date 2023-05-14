from core.constants.Helper import Choice


class ROLES(str, Choice):
    SUPER_ADMIN = 'SUPER_ADMIN'
    TEACHER = 'TEACHER'
    STUDENT = 'STUDENT'
