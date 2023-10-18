from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from django.db.utils import IntegrityError
from datetime import timedelta
from .forms import CreateContactForm,UpdateContactForm
from .models import ContactList


def home(request):
    return render(request, 'myapp3/home.html')
    
def create_contact(request):
    if request.method == 'POST':
        form = CreateContactForm(request.POST)
        try:
            def compare_strings(str1, str2):
                x=0
                if len(str1) != len(str2):
                    return False
                else:
                    for i in range(len(str1)):
                        if (str1[i] != str2[i]) and x!=2:
                            x+=1
                if x==2:
                    return False
                else:
                    return True
                
            if form.is_valid():
              formdata = form.cleaned_data
              name = formdata['name']
              address = formdata['address']
              profession = formdata['profession']
              confirmprofession = formdata['confirmprofession']
              telnumber = formdata['telnumber']
              email = formdata['email']
              datejoined= formdata['datejoined']
              dateexpired = formdata['dateexpired']
              if compare_strings(profession,confirmprofession)==True:
                  ContactList.objects.create(name=name, address=address,profession=profession,confirmprofession=confirmprofession, telnumber=telnumber,email=email,datejoined=datejoined,dateexpired=dateexpired)
                  return render(request, 'myapp3/success.html')
              else:
                  return render(request, 'myapp3/error.html')#ignore request but pretend the request was successful
        except IntegrityError as e:
            if 'UNIQUE constraint failed: myapp3_contact.name' in str(e):
                return render(request, 'myapp3/success.html')#ignore request but pretend the request was successful
            else:
                raise e
    else:
        form = CreateContactForm()
    
    return render(request, 'myapp3/createcontact.html', {'form': form})

def contact_list(request):
    contacts = ContactList.objects.all()
    return render(request, 'myapp3/contact_list.html', {'contacts': contacts})


def update_contact(request, pk):
    contact = get_object_or_404(ContactList, pk=pk)
    
    if request.method == 'POST':
        form = UpdateContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = UpdateContactForm(instance=contact)
    
    return render(request, 'myapp3/update_contact.html', {'form': form, 'contact': contact})


def delete_contact(request, pk):
    contact = get_object_or_404(ContactList, pk=pk)
    
    if request.method == 'POST':
        # Calculate the difference between dateexpired and datejoined
        date_difference = contact.dateexpired - contact.datejoined

        # Check if the difference is less than 1 year (365 days)
        if date_difference < timedelta(days=365):
            # Display a message to the user
            return HttpResponse("Contact cannot be deleted because the expiry date is less than 1 year from the join date.")
        
        # If the condition is not met, proceed with deletion
        contact.delete()
        return redirect('contact_list')
    
    return render(request, 'myapp3/delete_contact.html', {'contact': contact})