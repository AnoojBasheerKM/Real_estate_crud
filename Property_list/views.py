from django.shortcuts import render,redirect,get_object_or_404

from django.views.generic import View

from Property_list.forms import PropertyForm,PropertyEditForm

from Property_list.models import Property

# Create your views here.

class CreatePropertyView(View):
    
    template_name = "property_add.html"
    
    form_class = PropertyForm
    
    def get(self,request,*args,**kwargs):
        
        form_instance = self.form_class()
        
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        form_data = request.POST
        
        form_instance = self.form_class(form_data,files=request.FILES)
        
        if form_instance.is_valid():
            
            form_instance.save()
            
            return redirect("property-add")
        
        return render(request,self.template_name,{"form":form_instance})  
    
class PropertyListView(View):
    
    template_name = "property_list.html"
    
    def get(self,request,*args,**kwargs):
        
        qs = Property.objects.all()
        
        return render(request,self.template_name,{"data":qs})
    
class PropertyEditView(View):
    
    template_name = "property_edit.html"
    
    form_class = PropertyEditForm
    
    def get(self,request,*args,**kwargs):
        
        id = kwargs.get("pk")
        
        property_object = get_object_or_404(Property,id=id)
        
        form_instance = self.form_class(instance=property_object)
        
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        id = kwargs.get("pk")
        
        property_object = get_object_or_404(Property,id=id)
        
        form_data = request.POST
        
        form_instance = self.form_class(form_data,files=request.FILES,instance=property_object)
        
        if form_instance.is_valid():
            
            form_instance.save()
            
            return redirect("property-list")
        return render(request,self.template_name,{"form":form_instance})
    

class PropertyDeleteView(View):
    
     def get(self,request,*args,**kwargs):
        
        id = kwargs.get("pk")

        Property.objects.get(id=id).delete
        
        return redirect("property-list")
        
        
        
        
      
    
    
          
            
    

    
    
    
