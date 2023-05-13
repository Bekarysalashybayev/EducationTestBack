from config.constants.helper import Choice


class ROLES(str, Choice):
    SUPER_ADMIN = 'SUPER_ADMIN'
    TEACHER = 'TEACHER'
    STUDENT = 'STUDENT'
