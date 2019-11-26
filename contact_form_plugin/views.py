from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
import logging
from django.utils.translation import ugettext_lazy as _

from .forms import ContactForm
# Create your views here.

logger = logging.getLogger(__name__)


class ContactFormView(View):
    # all_contacts = Contact.objects.all()
    # # loading EN info
    # all_pages_EN = Page.objects.filter(lang='en')
    # all_activities_EN = Activity.objects.filter(lang='en')
    # activity_types_EN = all_activities_EN.values('type').distinct()
    # # loading ES info
    # all_pages_ES = Page.objects.filter(lang='es')
    # all_activities_ES = Activity.objects.filter(lang='es')
    # activity_types_ES = all_activities_ES.values('type').distinct()
    #
    # def get(self, request):
    #     try:
    #         if request.META['HTTP_ACCEPT_LANGUAGE'].startswith('es'):
    #             context = {
    #                 'all_contacts': self.all_contacts,
    #                 # 'all_photos': self.all_photos,
    #                 'activity_types': self.activity_types_ES,
    #                 'all_activities': self.all_activities_ES,
    #                 'all_pages': self.all_pages_ES,
    #             }
    #         else:
    #             context = {
    #                 'all_contacts': self.all_contacts,
    #                 # 'all_photos': self.all_photos,
    #                 'activity_types': self.activity_types_EN,
    #                 'all_activities': self.all_activities_EN,
    #                 'all_pages': self.all_pages_EN,
    #             }
    #         form = ContactForm()
    #         context['form'] = form
    #         return render(request, 'my_site/contact.html', context)
    #     except Exception as e:
    #         logger.exception(e)
    #         return redirect('/error/')
    #
    @staticmethod
    def post(request):
        try:
            form = ContactForm(request.POST)
            if form.is_valid():
                fields = ['name', 'email', 'arrival_date', 'party_size', 'reference']
                # print("[1] {}: {}".format(type(form.cleaned_data), form.cleaned_data))
                email_template = "<ul>"
                for field in fields:
                    email_template += "\n<li> {}: {}</li>".format(field, form.cleaned_data[field])
                    # print("> {}: {}".format(field, form.cleaned_data[field]))
                email_template += "\n</ul>"
                print(email_template)
                # send email here
                return redirect('/')
            else:
                return redirect('/contact/')
        except Exception as e:
            logger.exception(e)
            return redirect('/error/')


# def error(request):
#     if request.method == 'GET':
#         return render(request, 'my_site/error.html')
#     else:
#         return redirect('/error/')
