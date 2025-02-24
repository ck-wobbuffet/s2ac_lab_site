from django import forms
from django.contrib.contenttypes.models import ContentType
from django.db.models import ObjectDoesNotExist
from ckeditor.widgets import CKEditorWidget
from .models import Comment

class CommentFrom(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput, label=False)
    object_id = forms.IntegerField(widget=forms.HiddenInput, label=False)
    text = forms.CharField(widget=CKEditorWidget(config_name='comment_ckeditor'),
                    label=False, error_messages={'required': "Comment can't be empty! "})
    reply_comment_id = forms.IntegerField(widget=forms.HiddenInput(attrs={'id':'reply_comment_id'}))
    
    '''
        widget设置渲染出来的html样式
    '''


    def __init__(self, *arg, **kwargs):
        # 得到user变量
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super(CommentFrom, self).__init__(*arg, **kwargs)
        

    def clean(self):
        #   判断用户是否登录
        if self.user.is_authenticated:
            self.cleaned_data['user'] = self.user
        else:
            raise forms.ValidationError('Please sign in.')

        # 评论对象判断验证
        content_type = self.cleaned_data['content_type']
        object_id = self.cleaned_data['object_id']
        
        try:
            model_class = ContentType.objects.get(model=content_type).model_class()
            model_obj = model_class.objects.get(pk=object_id)
            self.cleaned_data['content_object'] = model_obj
        except ObjectDoesNotExist:
            raise forms.ValidationError('The comment object does not exist!')
        return self.cleaned_data

    def clean_reply_comment_id(self):
        reply_comment_id = self.cleaned_data['reply_comment_id']
        if reply_comment_id < 0:
            raise forms.ValidationError('Reply error!')
        elif reply_comment_id == 0:
            self.cleaned_data['parent'] = None
        elif Comment.objects.filter(pk=reply_comment_id).exists():
            self.cleaned_data['parent'] = Comment.objects.get(pk=reply_comment_id)
        else:
            raise forms.ValidationError('Reply error!')
        return reply_comment_id
        
