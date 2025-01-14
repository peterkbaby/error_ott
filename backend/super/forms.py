from django import forms
from .models import Video, Subscription_Plan


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title','category','description','videoFile','thumbnail']
        
class PlanForm(forms.ModelForm):
    class Meta:
        model = Subscription_Plan
        fields = ['planname','details','plan_price','validity','planAdded']