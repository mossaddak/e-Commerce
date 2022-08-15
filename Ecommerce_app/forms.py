from django import forms
from .models import Products,ProductREVIEWS
from django.forms import ModelForm
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget


class add_product_info(forms.ModelForm):
    product_desc = RichTextField()

    class Meta:
        model = Products
        fields = ('product_title','brand','product_desc','product_price','offer_price','total_stock','product_category','warranty','gurantee','product_image')
        
        labels = {
            'product_title':'Title',
            'brand':'Brand',
            'product_desc':'Description',
            'product_price':'Regular Price',
            'offer_price':'Offer Price',
            'total_stock':'Product Stock',
            'product_category':'Category',
            'warranty':'Product Warranty',
            'gurantee':'Product Gurantee',
            'product_image':'Product Image',
            
        }

         
        widgets = {
            'product_title':forms.TextInput(attrs={'class':'form-control', 'style':'font-size:13px;', 'required': True}),
            'brand':forms.TextInput(attrs={'class':'form-control', 'style':'font-size:13px;'}),
            'product_desc':forms.Textarea(attrs={'class':'form-control', 'style':'font-size:13px;','cols':'3'}),
            'product_price':forms.NumberInput(attrs={'class':'form-control', 'style':'font-size:13px;', 'min':'1', 'required': True}),
            'offer_price':forms.NumberInput(attrs={'class':'form-control', 'style':'font-size:13px;', 'min':'1',}),
            'total_stock':forms.NumberInput(attrs={'class':'form-control', 'style':'font-size:13px;', 'min':'1',}),
            'product_category':forms.Select(attrs={'class':'form-control', 'style':'font-size:13px;', 'required': True}),
            'warranty':forms.NumberInput(attrs={'class':'form-control', 'style':'font-size:13px;', 'min':'1',}),
            'gurantee':forms.NumberInput(attrs={'class':'form-control', 'style':'font-size:13px;', 'min':'1',}),
            'product_image':forms.FileInput(attrs={'class':'form-control', 'style':'font-size:13px;', 'required': True})
        }
        


#update product
class update_product_info(forms.ModelForm):
    product_desc = RichTextField()

    class Meta:
        model = Products
        fields = ('product_title','brand','product_desc','product_price','offer_price','total_stock','product_category','warranty','gurantee','product_image')
        

        labels = {
            'product_title':'Title',
            'brand':'Brand',
            'product_desc':'Description',
            'product_price':'Regular Price',
            'offer_price':'Offer Price',
            'total_stock':'Product Stock',
            'product_category':'Category',
            'warranty':'Product Warranty',
            'gurantee':'Product Gurantee',
            'product_image':'Product Image',
            

        }

         

        widgets = {
            'product_title':forms.TextInput(attrs={'class':'form-control', 'style':'font-size:13px;'}),
            'brand':forms.TextInput(attrs={'class':'form-control', 'style':'font-size:13px;'}),

            'product_desc':forms.Textarea(),
            
            'product_price':forms.NumberInput(attrs={'class':'form-control', 'style':'font-size:13px;'}),
            'offer_price':forms.NumberInput(attrs={'class':'form-control', 'style':'font-size:13px;'}),
            'total_stock':forms.NumberInput(attrs={'class':'form-control', 'style':'font-size:13px;'}),
            'product_category':forms.Select(attrs={'class':'form-control', 'style':'font-size:13px;'}),
            'warranty':forms.NumberInput(attrs={'class':'form-control', 'style':'font-size:13px;'}),
            'gurantee':forms.NumberInput(attrs={'class':'form-control', 'style':'font-size:13px;'}),
            'product_image':forms.FileInput(attrs={'class':'form-control', 'style':'font-size:13px;'})
        }


#update feedback form____________________________
class UpdateFeedbackForm(forms.ModelForm):

    class Meta:
        model = ProductREVIEWS
        fields = ('rating','feedBACK')
        

