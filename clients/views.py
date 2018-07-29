from django.shortcuts import render, get_object_or_404
from django_tables2 import RequestConfig
from django_tables2.export.export import TableExport
from .models import Contact
from .tables import ContactTable
from .forms import ContactForm
from django.shortcuts import redirect
from src.Reader import read, read_from_json_place_holder
from src.BreffiScrap import get_worth
from src.Validation import phone_is_valid, email_is_valid


def contact_list(request):

    table = ContactTable(Contact.objects.all())

    if request.method == 'POST':
        RequestConfig(request).configure(table)

        export_format = None

        if '_export_json' in request.POST:
            export_format = 'json'

        elif '_export_csv' in request.POST:
            export_format = 'csv'

        if export_format is not None and TableExport.is_valid_format(export_format):
            exporter = TableExport(export_format, table, exclude_columns=u'buttons')
            return exporter.response('table.{}'.format(export_format))

        if '_import' in request.POST and request.FILES:

            uploaded_file = request.FILES['uploaded_file']
            gen = read(uploaded_file)
            for item in gen:
                contact = Contact.objects.create(name=item['name'],
                                                 company=item['company'],
                                                 email=item['email'],
                                                 phone=item['phone'],
                                                 interests=item['interests']
                                                 )
                contact.save()

        return redirect('contact_list')

    else:
        RequestConfig(request, paginate={'per_page': 10}).configure(table)

    return render(request, 'clients/contact_list.html', {'table': table, 'worth': get_worth()})


def remove_all(request):

    if request.method == "POST" and '_confirm' in request.POST:
        Contact.objects.all().delete()
        return redirect('contact_list')

    elif request.method == "POST" and '_cancel' in request.POST:
        return redirect('contact_list')

    return render(request, 'clients/confirm.html', {'text': 'to delete all items'})


def contact_details(request, pk):
    if request.method == "GET":
        contact = get_object_or_404(Contact, pk=pk)

        return render(request, 'clients/contact_detail.html', {'contact': contact})

    elif request.method == "POST":
        if '_cancel' in request.POST:
            return redirect('contact_list')


def contact_rm(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":

        if '_confirm' in request.POST:
            contact.delete()

        return redirect('contact_list')

    return render(request, 'clients/contact_remove.html', {'contact': contact})


def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    form = ContactForm(request.POST or None, instance=contact)
    if request.POST:
        if '_edit' in request.POST and form.is_valid():
            form.save()
            return redirect('contact_details', pk=contact.pk)
        elif '_cancel' in request.POST:
            return redirect('contact_list')

    return render(request, 'clients/contact_edit.html', {'form': form})


def contact_add(request):

    if request.method == "POST":

        if '_create' in request.POST:
            form = ContactForm(request.POST)

            phone = form.data['phone']
            email = form.data['email']

            if form.is_valid() and phone_is_valid(phone) and email_is_valid(email):
                contact = form.save()
                return redirect('contact_details', pk=contact.pk)
            else:
                return render(request, 'clients/contact_new.html', {'form': form})

        elif '_cancel' in request.POST:
            return redirect('contact_list')
    else:
        form = ContactForm()
        return render(request, 'clients/contact_new.html', {'form': form})


def load_from_json(request):

    if request.method == "POST" and '_confirm' in request.POST:
        gen = read_from_json_place_holder()
        for item in gen:
            contact = Contact.objects.create(name=item['name'],
                                             company=item['company'],
                                             email=item['email'],
                                             phone=item['phone'],
                                             interests=item['interests']
                                             )
            contact.save()
        return redirect('contact_list')

    elif request.method == "POST" and '_cancel' in request.POST:
        return redirect('contact_list')


    return render(request, 'clients/confirm.html', {'text': 'load data from JsonPlaceHolder'})

