from typing import Any


class TitleMixin:
    title = None

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(TitleMixin, self).get_context_data()
        context["title"] = self.title
        return context
