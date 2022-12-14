"""Renders Module"""
from rest_framework.renderers import JSONRenderer


class CustomRenderer(JSONRenderer):
    """Custom Render class"""

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """Render method"""

        service_name = getattr(
            renderer_context.get("view").get_serializer().Meta, "service_name", "data"
        )
        response = renderer_context.get("response")

        if response and response.status_code < 300:
            data = {service_name: data}

        return super().render(
            data, accepted_media_type, renderer_context
        )
