from django import forms

from Property_list.models import Property

class PropertyForm(forms.ModelForm):
    
    class Meta:
        
        model = Property
        
        fields = "__all__"
        
class PropertyEditForm(forms.ModelForm):
    
    class Meta:
        
        model = Property
        
        fields = "__all__"
        