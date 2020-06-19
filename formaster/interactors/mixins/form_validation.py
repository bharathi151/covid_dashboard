from formaster.exceptions.exceptions import FormClosed
class FormValidationMixin:

    def validate_for_live_form(self, form_id: int):
        is_form_live = not self.storage.get_form_status(form_id)
        if is_form_live:
            raise FormClosed
