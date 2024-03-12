from django.urls import reverse_lazy


class RedirectToIndexMixin:
    success_url = reverse_lazy('index')
