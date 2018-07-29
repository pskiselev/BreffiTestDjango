import django_tables2 as tables
from .models import Contact


class ContactTable(tables.Table):
    class Meta:
        model = Contact
        template_name = 'django_tables2/bootstrap.html'
        exclude = 'id'

    buttons = tables.TemplateColumn(
        '<style>.layer{border:1px; border-style:solid; border-color:#0000FF;padding: 1px;}</style>'
        '<a href="{% url "contact_details" record.pk %}" class=layer>&ensp;details&ensp;</a>'
        '<a>&ensp;</a>'
        '<a href="{% url "contact_rm" record.pk %}" class=layer>&ensp;remove&ensp;</a>'
        '<a>&ensp;</a>'
        '<a href="{% url "contact_edit" record.pk %}" class=layer>&ensp;edit&ensp;</a>',
        verbose_name=u'Action',
        orderable=False
    )
