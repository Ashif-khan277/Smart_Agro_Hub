from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  # ജാംഗോ തരുന്ന ഇൻ-ബിൽറ്റ് രജിസ്ട്രേഷൻ ഫോം


def register_view(request):
    if request.method == 'POST':  # യൂസർ ഫോം ടൈപ്പ് ചെയ്ത് സബ്മിറ്റ് ചെയ്യുമ്പോൾ
        form = UserCreationForm(request.POST)  # യൂസർ അടിച്ച വിവരങ്ങൾ ജാംഗോ ഫോമിലേക്ക് മാറ്റുന്നു
        if form.is_valid():  # പാസ്‌വേഡ് കറക്റ്റ് ആണോ, യൂസർനെയിം മുൻപ് ഉള്ളതാണോ എന്ന് ജാംഗോ തനിയെ ചെക്ക് ചെയ്യുന്നു
            form.save()  # എല്ലാം കറക്റ്റ് ആണെങ്കിൽ ഡാറ്റാബേസിലേക്ക് പുതിയ യൂസറെ സേവ് ചെയ്യുന്നു
            return redirect('login')  # രജിസ്ട്രേഷൻ കഴിഞ്ഞാൽ ലോഗിൻ പേജിലേക്ക് തിരിച്ചു വിടുന്നു
    else:
        form = UserCreationForm()  # യൂസർ വെറുതെ പേജ് ഓപ്പൺ ചെയ്യുമ്പോൾ ഒഴിഞ്ഞ ഫോം കാണിക്കുന്നു

    context = {
        'form_bag': form  # ഫോം HTML-ലേക്ക് അയക്കാൻ വേണ്ടി ഒരു ഡിക്‌ഷണറി ബാഗിലാക്കുന്നു
    }
    return render(request, 'register.html', context)  # റെജിസ്റ്റർ പേജ് ലോഡ് ചെയ്യുന്നു

# Create your views here.
