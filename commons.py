# -*- coding: utf-8 -*-
from django.forms.utils import ErrorList
from django.utils.encoding import force_text
from django.utils.html import format_html, format_html_join


class ErrList(ErrorList):

    def as_ul(self):
        if not self.data:
            return ''

        return format_html(
            '<div class="invalid-feedback">{}</div>',
            format_html_join('', '<li>{}</li>', ((force_text(e),) for e in self))
        )