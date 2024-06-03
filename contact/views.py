from django.core.mail import send_mail

from django.shortcuts import render, redirect

from django.template.loader import render_to_string

from .forms import ContactForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['message']

            html = render_to_string('contact/emails/contactForm.html', {

                'name': name, 'email': email, 'content': content

                })
            # Send email
            print("the form was valid")

            send_mail('Contact Form Submission','You have received a new contact form submission. Here are the details:\n\nName: ' + name + '\nEmail: ' + email + '\nMessage: ' + content,'rvinayak108@gmail.com', ['yash2yk2@gmail.com'], html_message=html)

            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'contact/index.html', {
        'form': form,
    })
