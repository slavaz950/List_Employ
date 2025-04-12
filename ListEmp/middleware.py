# Отключение CSRF (Чтобы избежать ошибок)
class disableCSRF:
    def process_request(self,request):
        setattr(request, '_dont_enforse_csrf_checks', True)
        return None