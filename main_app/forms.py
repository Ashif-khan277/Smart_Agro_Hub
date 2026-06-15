from django import forms
from .models import Crop # നമ്മൾ ഉണ്ടാക്കിയ Crop മോഡൽ ഇമ്പോർട്ട് ചെയ്യുന്നു

class CropForm(forms.ModelForm):
    class Meta:
        model = Crop # ഏത് മോഡൽ വെച്ചാണ് ഫോം ഉണ്ടാക്കേണ്ടത് എന്ന് ജാംഗോയോട് പറയുന്നു
        fields = ['name', 'category', 'price_per_kg', 'description'] # കർഷകൻ ടൈപ്പ് ചെയ്യേണ്ട ബോക്സുകൾ