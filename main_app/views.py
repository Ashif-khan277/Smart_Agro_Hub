# from django.shortcuts import render
# from django.http import HttpResponse
#
# def home(request):
#     return HttpResponse("<h1>welcome to smart Agro_hub!</h1>")
# # Create your views here.
# from django.shortcuts import render
# from.models import crop
#
# def home(request):
#     all_crops=crop.object.all()
#     context{
#         'crop_list'=all_crops
#     }
#     return render(request, 'index.html',context)
# from django.shortcuts import render
# from .models import Crop
#
#
# def home(request):
#     all_crops = Crop.objects.all()
#     context = {
#         'crops_list': all_crops
#     }
#
#     return render(request, 'index.html', context)  #

from django.shortcuts import render
from .models import Crop  # ഡാറ്റാബേസ് ടേബിൾ ആയ Crop ക്ലാസിനെ ഇങ്ങോട്ട് കൊണ്ടുവരുന്നു


def home(request):
    query = request.GET.get(
        'search_box')  # ബ്രൗസറിലെ സെർച്ച് ബോക്സിൽ യൂസർ ടൈപ്പ് ചെയ്ത വാക്ക് 'query' എന്ന വേരിയബിളിലേക്ക് എടുക്കുന്നു

    if query:
        all_crops = Crop.objects.filter(
            name__icontains=query)  # യൂസർ അടിച്ച വാക്ക് വിളയുടെ പേരിലുണ്ടോ എന്ന് ഡാറ്റാബേസിലോട്ട് ഫിൽട്ടർ ചെയ്ത് നോക്കുന്നു
    else:
        all_crops = Crop.objects.all()  # സെർച്ച് ഒന്നും ചെയ്തിട്ടില്ലെങ്കിൽ ഡാറ്റാബേസിലെ എല്ലാ വിളകളും എടുക്കുന്നു

    context = {
        'crops_list': all_crops  # വിവരങ്ങൾ HTML-ലേക്ക് അയക്കാൻ വേണ്ടി ഒരു ഡിക്‌ഷണറി ബാഗിലാക്കുന്നു
    }

    return render(request, 'index.html', context)  # ഡാറ്റയും ചേർത്ത് index.html ലോഡ് ചെയ്യുന്നു