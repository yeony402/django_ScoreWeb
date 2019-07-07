# from django.shortcuts import render, render_to_response, get_object_or_404, reverse, redirect
# from django import forms
# from django.core.exceptions import ValidationError, MultipleObjectsReturned, ObjectDoesNotExist
# from django.db.utils import IntegrityError
# from django.contrib.auth.forms import UserCreationForm
# from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
# from django.contrib import messages
# from django.views.generic.base import TemplateView
# from django.views.generic.edit import FormView
# from django.views.generic import ListView
# from .models import Ceo, MyUser, Score
# from . import models
#
#
# class ScoreForm(forms.ModelForm):
#     score_0 = forms.IntegerField()
#     score_1 = forms.IntegerField()
#     score_2 = forms.IntegerField()
#     score_3 = forms.IntegerField()
#     score_4 = forms.IntegerField()
#     score_5 = forms.IntegerField()
#     score_6 = forms.IntegerField()
#     score_7 = forms.IntegerField()
#     score_8 = forms.IntegerField()
#     comment = forms.CharField(widget=forms.Textarea)
#
#     class Meta:
#         model = Score
#         exclude = ('ceo', 'myuser')
#
# # clean은 필드의 서브클래스로 폼의 전체필드에 대해 유효성 검사를 할 때 사용하고, clean_필드명 함수는 폼의 서브클래스로 특정 필드에 대한 유효성 검사를 실시할 때 사용한다. 폼에 두 메서드가 같이 있을 땐 clean_필드명 메서드가 먼저 실행된다.
# #     def clean(self):
# #         cleaned_data = self.cleaned_data
# #
# # # socre_0 = self.cleaned_data.get()는 clean() 메소드에서 자꾸 오류가 난다.. cleaned_data[]로 데이터 변화값을 받아줘야한다.
# #         score_0 = cleaned_data.get('score_0')
# #         score_1 = cleaned_data.get('score_1')
# #         score_2 = cleaned_data.get('score_2')
# #         score_3 = cleaned_data.get('score_3')
# #         score_4 = cleaned_data.get('score_4')
# #         score_5 = cleaned_data.get('score_5')
# #         score_6 = cleaned_data.get('score_6')
# #         score_7 = cleaned_data.get('score_7')
# #         score_8 = cleaned_data.get('score_8')
# #         comment = cleaned_data.get('comment')
#
#
#         def clean_score_0(self):
#             score_0 = self.cleaned_data.get('score_0')
#             return score_0
#         def clean_score_1(self):
#             score_1 = self.cleaned_data.get('score_1')
#             return score_1
#         def clean_score_2(self):
#             score_2 = self.cleaned_data.get('score_2')
#             return score_2
#         def clean_score_3(self):
#             score_3 = self.cleaned_data.get('score_3')
#             return score_3
#         def clean_score_4(self):
#             score_4 = self.cleaned_data.get('score_4')
#             return score_4
#         def clean_score_5(self):
#             score_5 = self.cleaned_data.get('score_5')
#             return score_5
#         def clean_score_6(self):
#             score_6 = self.cleaned_data.get('score_6')
#             return score_6
#         def clean_score_7(self):
#             score_7 = self.cleaned_data.get('score_7')
#             return score_7
#         def clean_score_8(self):
#             score_8 = self.cleaned_data.get('score_8')
#             return score_8
#         def clean_comment(self):
#             comment = self.cleaned_data.get('comment')
#             return comment
#
#         def save(self):
#             score = super().save(commit=False)
#             if 0 <= score_0 <= 15 and 0 <= score_1 <= 15 and 0 <= score_2 <= 15 and 0 <= score_3 <= 15 and 0 <= score_4 <= 5 and 0 <= score_6 <= 5 and 0 <= score_5 <= 10 and 0 <= score_7 <= 10   and 0 <= score_8 <= 10:
#                 score.save(commit=True)
#                 # return cleaned_data
#             else:
#                 raise forms.ValidationError("점수를 확인해주세요.", code='too mach')
#                 # return cleaned_data
#
# # 지원자 정보 확인할 때 choicefield에 지원자명을 나타내주는 폼
# class CheckCeoForm(forms.Form):
#     # 모델의 필드값을 choicefield로 만들기 - 데이터가 안넘어옴 > ModelChoiceField를 올바른 방법으로 사용하지 않은 것 같음.
#     # ceo_select = Ceo.objects.values_list('ceoname',flat=True).order_by('ceoname')
#     # ceos = forms.ModelChoiceField(queryset=ceo_select)
#
#     YEARS=(
#         (2019, 2019),
#         (2020, 2020),
#         (2021, 2021),
#         (2022, 2022),
#         (2023, 2023),
#         (2024, 2024),
#         (2025, 2025),
#     )
#     years = forms.ChoiceField(choices=YEARS)
#     # models.Ceo.objects의 역할 도대체 무엇 >> return값인 ceoname만 반환했음
#     ceos = forms.ModelChoiceField(models.Ceo.objects)
#     #, widget=forms.Select(attrs={'pk':'ceoname'})) ModelChoiceField 뒤에 있던 아이인데 필요없는 것 같음.
#
#     # 초기데이터에서 값이 변했을 수도 있기 때문에 그 변환된 값으로 받아줌. 아래 정보 수정 부분에서 사용.
#     def clean_ceos(self):
#         checked_ceo = self.cleaned_data.get('ceos')
#         return checked_ceo
#
#     def clean_years(self):
#         checked_year = self.cleaned_data.get('years')
#         return checked_year
#
#
#
# # 회원가입 뷰(현재 admin에서만 사용)
# # 이게 없으면 왜 유저를 생성해도 로그인이 안되지?
# class UserCreationForm(forms.ModelForm):
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
#
#     class Meta:
#         model = MyUser
#         fields = '__all__'
#
#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user
#
# # forms.ModelForm을 해줘야 모델과 연동이 되어 저장이 된다(+ 메타 클래스에 모델 선언)
# class CeoForm(forms.ModelForm):
#
#     class Meta:
#         model = Ceo
#         fields = ['ceoname', 'years', 'item_fields', 'work_fields', 'setup_fields', 'plus_points', 'itemname']
#
#     #수정된 데이터 받아오기(form.cleaned_data.get())
#     def clean_ceoname(self):
#         ceoname = self.cleaned_data.get('ceoname')
#         return ceoname
#     def clean_itemname(self):
#         itemname = self.cleaned_data.get('itemname')
#         return itemname
#     def clean_years(self):
#         years = self.cleaned_data.get('years')
#         return years
#     def clean_item_fields(self):
#         item_fields = self.cleaned_data.get('item_fields')
#         return item_fields
#     def clean_work_fields(self):
#         work_fields = self.cleaned_data.get('work_fields')
#         return work_fields
#     def clean_setup_fields(self):
#         setup_fields = self.cleaned_data.get('setup_fields')
#         return setup_fields
#     def clean_plus_points(self):
#         plus_points = self.cleaned_data.get('plus_points')
#         return plus_points
#
#     def save(self):
#         save = super().save(commit=True)
#
#
#
# # 기본 홈 뷰
# class HomeView(TemplateView):
#     #Listview에는 model명을 적지 않으면 에러남
#     # model = MyUser
#     template_name = 'django_ex/home.html'
#     # (listview를 상속받았을 경우)context_object_list의 디폴트 값은 object_list 또는 모델명소문자_list로 자동 지정된다.
#     # context_object_list =
#
# class BaseListView(TemplateView):
#     template_name = 'django_ex/base_info_list.html'
#
# def document_results(request, current_user, current_ceo):
#     forms = Ceo.objects.get(id=current_ceo)
#     ceo_score_info = Score.objects.get(myuser_id=current_user, ceo_id=current_ceo)
#     ceo_plus_score = Ceo.objects.get(ceo_relation=current_user, id=current_ceo)
#
#     sum_score = []
#     list = [ceo_score_info.score_0, ceo_score_info.score_1, ceo_score_info.score_2, ceo_score_info.score_3, ceo_score_info.score_4, ceo_score_info.score_5, ceo_score_info.score_6, ceo_score_info.score_7, ceo_score_info.score_8]
#     list_1 = [ceo_plus_score.plus_points]
#     sum_score.extend(list+list_1)
#
#     global middle_sum_score, final_sum_score
#     middle_sum_score = sum(list)
#     final_sum_score = sum(sum_score)
#     context = {
#         'show_score' : ceo_score_info,
#         'post' : forms,
#         'sum' : middle_sum_score,
#         'sum_score': final_sum_score
#     }
#     return render(request, 'django_ex/document_results.html', context)
#
#
# def document_post(request, current_user, current_ceo):
#     try:
#         # values_list('ceoname') 메서드를 사용하면 ceoname값만 불러오기 떄문에 템플릿에서 ceoname.id값을 호출하면 id에 대한 에러가 남.
#         ceo_instance = Ceo.objects.get(id=current_ceo)
#         myuser_instance = MyUser.objects.get(id=current_user)
#         check_exists = Score.objects.filter(myuser_id=myuser_instance.pk, ceo_id=ceo_instance.pk).exists()
#         # shell api를 이용해서 연구함, post할 때 ForeignKey값을 저장하는 방법, instance 매개변수 사용
#         foreign_instance = Score(myuser=myuser_instance, ceo=ceo_instance)
#
#         # 같은 평가자와 지원자의 정보가 이미 존재할 때 결과로 리다이렉트 한다.
#         if check_exists == True:
#             return redirect(reverse('django_ex:document_results', args=(current_user, current_ceo)))
#         else:
#             pass
#
#         if request.method == 'POST':
#             scoreform = ScoreForm(request.POST, instance=foreign_instance)
#             if scoreform.is_valid():
#                 scoreform.save()
#                 # 점수 저장이 완료되어 결과값을 볼 수 있는 화면으로 리다이렉트
#                 return HttpResponseRedirect(reverse('django_ex:document_results', args=(current_user, current_ceo)))
#             else:
#                 scoreform.errors
#         else:
#             scoreform = ScoreForm()
#
#         context = {
#             'post':ceo_instance,
#             'score':scoreform,
#         }
#
#         # 유효성 검사에 실패하였으므로 점수 입력하던 화면으로 리다이렉트(배점에 맞춰 입력해야함)
#         return render(request, 'django_ex/document_post.html', context)
#     except IntegrityError:
#         # unique_together옵션으로 평가자명과 지원자/기업명이 같으면 이미 평가가 완료된 상태를 뜻하기 떄문에 지원자 목록으로 리다이렉트 (check_exists를 생성한 이후로 불필요한 예외처리)
#         return redirect('django_ex:document_list', current_user)
#
#
# # ceoname을 서류평가 템플릿의 {% for in %} 태그에서 사용하기 위한 view
# def document_list(request, current_user):
#     # flat=True는 values_list다음 또 다른 필드의 사용을 알려주는 것이다.
#     ceo_list = Ceo.objects.order_by('id')
#     return render(request, 'django_ex/document_list.html', {'ceo_list':ceo_list})
#
# #ceoname을 발표평가 템플릿의 {% for in %}태그에서 사용하기 위한 view
# def presentation_list(request, current_user):
#     ceoname = Ceo.objects.values_list('ceoname', flat=True).order_by('id')
#     return render(request, 'django_ex/presentation_list.html', {'ceo_list':ceoname})
#
# # ceoform을 템플릿에서 사용하기 위해 호출한 view
# def base_info(request):
#     if request.method == 'POST':
#         ceoform = CeoForm(request.POST)
#         # 폼에서 정의된 유효성 검증 규칙에 맞다면 - is_valid
#         if ceoform.is_valid():
#             ceoform.save()
#             messages.success(request, '저장되었습니다.')
#             return redirect('django_ex:base_info')
#         else:
#             ceoform.errors
#     else:
#         ceoform=CeoForm()
#     return render(request, 'django_ex/base_info.html', {'ceoform':ceoform})
#
#
# def base_info_check(request):
#     try:
#         if request.method == 'POST':
#             form = CheckCeoForm(request.POST)
#             input_form = CeoForm(request.POST)
#             if form.is_valid():
#                 get_value = request.POST.get('ceos')
#                 get_years = request.POST.get('years')
#                 post = Ceo.objects.filter(years=get_years).get(id=get_value)
#                 context = {
#                     'post':post,
#                     'ceos':form,
#                     'input_form':input_form,
#                 }
#                 return render(request, 'django_ex/base_info_reviews.html', context)
#             else:
#                 form.errors
#         else:
#             form = CheckCeoForm()
#         return render(request, 'django_ex/base_info_check.html', {'ceos':form})
#     except Ceo.DoesNotExist:
#         messages.info(request, '존재하지 않는 데이터입니다.')
#         return redirect('django_ex:base-info-check')
#
# def checked_evaluation(request):
#     try:
#         # sum = document_results(request, current_ceo, current_user)
#         if request.method == 'POST':
#             form = CheckCeoForm(request.POST)
#             if form.is_valid():
#                 get_value = request.POST.get('ceos')
#                 get_years = request.POST.get('years')
#                 selected_info = Ceo.objects.filter(years=get_years).get(id=get_value)
#                 score = Score.objects.get(ceo_id=selected_info)
#                 post = Ceo.objects.get(id=get_value)
#                 # user = request.POST.get('user')
#                 # sum_ = document_results(request, current_ceo=get_value, current_user=user)
#                 context = {
#                     'ceos':form,
#                     'score':score,
#                     'post':post,
#                     # 'sum':middle_sum_score,
#                     # 'sum_score':sum.final_sum_score,
#                 }
#                 return render(request, 'django_ex/checked_evaluation_results.html', context)
#             else:
#                 form.errors
#         else:
#             form = CheckCeoForm()
#
#         #다운로드가 진행된 코드
#         # return HttpResponse(request, 'django_ex/show_evaluation.html')
#         return render(request, 'django_ex/checked_evaluation.html', {'ceos':form})
#     except ObjectDoesNotExist:
#         messages.info(request, '존재하지 않는 데이터입니다.')
#         return redirect('django_ex:checked-evaluation-results')
#
#
# def base_info_change(request, current_ceo):
#     post = Ceo.objects.get(id=current_ceo)
#     if request.method == 'POST':
#         ceoform = CeoForm(request.POST, instance=post)
#         if ceoform.is_valid():
#             ceoform.save()
#             return redirect('django_ex:base-info-check')
#         else:
#             ceoform.errors
#     else:
#         ceoform = CeoForm(instance=post)
#     context = {
#         'ceoform':ceoform,
#         'post':post,
#     }
#     return render(request, 'django_ex/base_info_change.html', context)
#
# def changed_evaluation(request, current_ceo):
#     score_instance = Score.objects.get(ceo=current_ceo)
#     post = Ceo.objects.get(id=current_ceo)
#     if request.method == 'POST':
#         # ceos = CheckCeoForm(request.POST, instance=post)
#         scoreform = ScoreForm(request.POST, instance=score_instance)
#         if scoreform.is_valid():
#             scoreform.save()
#             return redirect('django_ex:checked-evaluation')
#         else:
#             scoreform.errors
#     else:
#         scoreform = ScoreForm(instance=score_instance)
#     context = {
#         # 'ceos':ceos,
#         'post':post,
#         'scoreform':scoreform,
#     }
#     return render(request, 'django_ex/changed_evaluation.html', context)

######################################################################################
from django.shortcuts import render, render_to_response, get_object_or_404, reverse, redirect
from django import forms
from django.template import loader
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError, MultipleObjectsReturned, ObjectDoesNotExist
from django.db.utils import IntegrityError
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .models import Ceo, MyUser, Score
from . import models
import datetime


class ScoreForm(forms.ModelForm):
    score_0 = forms.FloatField(widget=forms.TextInput(attrs={'class':'num_only num_sum'}))
    score_1 = forms.FloatField(widget=forms.TextInput(attrs={'class':'num_only num_sum'}))
    score_2 = forms.FloatField(widget=forms.TextInput(attrs={'class':'num_only num_sum'}))
    score_3 = forms.FloatField(widget=forms.TextInput(attrs={'class':'num_only num_sum'}))
    score_4 = forms.FloatField(widget=forms.TextInput(attrs={'class':'num_only num_sum'}))
    score_5 = forms.FloatField(widget=forms.TextInput(attrs={'class':'num_only num_sum'}))
    score_6 = forms.FloatField(widget=forms.TextInput(attrs={'class':'num_only num_sum'}))
    score_7 = forms.FloatField(widget=forms.TextInput(attrs={'class':'num_only num_sum'}))

    class Meta:
        model = Score
        exclude = ('ceo', 'myuser')
        fields = ['th', 'score_0', 'score_1', 'score_2', 'score_3', 'score_4', 'score_5', 'score_6', 'score_7', 'comment']

# clean은 필드의 서브클래스로 폼의 전체필드에 대해 유효성 검사를 할 때 사용하고, clean_필드명 함수는 폼의 서브클래스로 특정 필드에 대한 유효성 검사를 실시할 때 사용한다. 폼에 두 메서드가 같이 있을 땐 clean_필드명 메서드가 먼저 실행된다.
#     def clean(self):
#         cleaned_data = self.cleaned_data
#
# # socre_0 = self.cleaned_data.get()는 clean() 메소드에서 자꾸 오류가 난다.. cleaned_data[]로 데이터 변화값을 받아줘야한다.
#         score_0 = cleaned_data['score_0']
#         score_1 = cleaned_data['score_1']
#         score_2 = cleaned_data['score_2']
#         score_3 = cleaned_data['score_3']
#         score_4 = cleaned_data['score_4']
#         score_5 = cleaned_data['score_5']
#         score_6 = cleaned_data['score_6']
#         score_7 = cleaned_data['score_7']
#         comment = cleaned_data['comment']

        def clean_score_0(self):
            score_0 = self.cleaned_data.get('score_0')
            return score_0
        def clean_score_1(self):
            score_1 = self.cleaned_data.get('score_1')
            return score_1
        def clean_score_2(self):
            score_2 = self.cleaned_data.get('score_2')
            return score_2
        def clean_score_3(self):
            score_3 = self.cleaned_data.get('score_3')
            return score_3
        def clean_score_4(self):
            score_4 = self.cleaned_data.get('score_4')
            return score_4
        def clean_score_5(self):
            score_5 = self.cleaned_data.get('score_5')
            return score_5
        def clean_score_6(self):
            score_6 = self.cleaned_data.get('score_6')
            return score_6
        def clean_score_7(self):
            score_7 = self.cleaned_data.get('score_7')
            return score_7
        def clean_comment(self):
            comment = self.cleaned_data.get('comment')
            return comment
        # def clean_th(self):
        #     th = self.cleaned_data.get('th')
        #     return th

# 지금은 폼에서 점수 유효성검사를 하지만 배점도 필드로 두고 유효성검사를 해야할것같다.
    def save(self):
        score = super().save(commit=False)
        if 0 <= score.score_0 <= 15 and 0 <= score.score_1 <= 15 and 0 <= score.score_2 <= 15 and 0 <= score.score_3 <= 15 and 0 <= score.score_4 <= 5 and 0 <= score.score_6 <= 10 and 0 <= score.score_5 <= 10 and 0 <= score.score_7 <= 10 :
            score.save()
        else:
            raise forms.ValidationError(_('점수를 확인해주세요.'), code='invalid')



class ScoreForm_2(forms.ModelForm):
    score_0 = forms.FloatField(widget=forms.TextInput(attrs={'class':'num_only num_sum'}))
    score_1 = forms.FloatField(widget=forms.TextInput(attrs={'class':'num_only num_sum'}))
    score_2 = forms.FloatField(widget=forms.TextInput(attrs={'class':'num_only num_sum'}))
    score_3 = forms.FloatField(widget=forms.TextInput(attrs={'class':'num_only num_sum'}))
    score_4 = forms.FloatField(widget=forms.TextInput(attrs={'class':'num_only num_sum'}))
    score_5 = forms.FloatField(widget=forms.TextInput(attrs={'class':'num_only num_sum'}))
    score_6 = forms.FloatField(widget=forms.TextInput(attrs={'class':'num_only num_sum'}))
    score_7 = forms.FloatField(widget=forms.TextInput(attrs={'class':'num_only num_sum'}))

    class Meta:
        model = Score
        exclude = ('ceo', 'myuser')
        fields = ['th', 'score_0', 'score_1', 'score_2', 'score_3', 'score_4', 'score_5', 'score_6', 'score_7', 'comment']

        def clean_score_0(self):
            score_0 = self.cleaned_data.get('score_0')
            return score_0
        def clean_score_1(self):
            score_1 = self.cleaned_data.get('score_1')
            return score_1
        def clean_score_2(self):
            score_2 = self.cleaned_data.get('score_2')
            return score_2
        def clean_score_3(self):
            score_3 = self.cleaned_data.get('score_3')
            return score_3
        def clean_score_4(self):
            score_4 = self.cleaned_data.get('score_4')
            return score_4
        def clean_score_5(self):
            score_5 = self.cleaned_data.get('score_5')
            return score_5
        def clean_score_6(self):
            score_6 = self.cleaned_data.get('score_6')
            return score_6
        def clean_score_7(self):
            score_7 = self.cleaned_data.get('score_7')
            return score_7
        def clean_comment(self):
            comment = self.cleaned_data.get('comment')
            return comment
        # def clean_th(self):
        #     th = self.cleaned_data.get('th')
        #     return th

# 지금은 폼에서 점수 유효성검사를 하지만 배점도 필드로 두고 유효성검사를 해야할것같다.
    def save(self):
        score = super().save(commit=False)
        if 0 <= score.score_0 <= 15 and 0 <= score.score_1 <= 15 and 0 <= score.score_2 <= 15 and 0 <= score.score_3 <= 15 and 0 <= score.score_4 <= 5 and 0 <= score.score_6 <= 10 and 0 <= score.score_5 <= 10 and 0 <= score.score_7 <= 10 :
            score.save()
        else:
            raise forms.ValidationError(_('점수를 확인해주세요.'), code='invalid')




# 지원자 정보 확인할 때 choicefield에 지원자명을 나타내주는 폼
class CheckCeoForm(forms.Form):
    # 모델의 특정 필드 데이터 값을 choicefield로 만들기 - 데이터가 안넘어옴 > ModelChoiceField를 올바른 방법으로 사용하지 않은 것 같음.
    # ceo_select = Ceo.objects.values_list('ceoname',flat=True).order_by('ceoname')
    # ceos = forms.ModelChoiceField(queryset=ceo_select)

    YEARS=(
        (2019, 2019),
        (2020, 2020),
        (2021, 2021),
    )
    years = forms.ChoiceField(choices=YEARS)
    # # models.Ceo.objects의 역할 도대체 무엇 >> return값인 ceoname만 반환했음
    ceos = forms.ModelChoiceField(models.Ceo.objects)
    # #, widget=forms.Select(attrs={'pk':'ceoname'})) ModelChoiceField 뒤에 있던 아이인데 필요없는 것 같음.

    def clean_years(self):
        checked_year = self.cleaned_data.get('years')
        return checked_year
    # years_ceo = forms.ModelChoiceField(queryset=Ceo.objects.filter(years))

    # def __init__(self, *args, **kwargs):
    #     # if kwargs.get('years', False):
    #     #     year = Ceo.objects.filter(years=kwargs.get('years'))
    #     # years_value = kwargs.get('years')
    #     # year = kwargs.pop('years')
    #     super().__init__(*args, **kwargs)
    #     # self.fields['ceos'].queryset = year
    #     # selected_years = Ceo.objects.get(years=kwargs.get('years'))
    #    # ceos = forms.ModelChoiceField(queryset=Ceo.objects.filter(years=2019))
    #     ceos = forms.ModelChoiceField(models.Ceo.objects)

    # 초기데이터에서 값이 변했을 수도 있기 때문에 그 변환된 값으로 받아줌. 아래 정보 수정 부분에서 사용.
    def clean_ceos(self):
        checked_ceo = self.cleaned_data.get('ceos')
        return checked_ceo




# forms.ModelForm을 해줘야 모델과 연동이 되어 저장이 된다(+ 메타 클래스에 모델 선언)
class CeoForm(forms.ModelForm):
    plus_points = forms.FloatField(widget=forms.TextInput(attrs={'class':'num_only num_sum'}))

    class Meta:
        model = Ceo
        fields = ['ceoname', 'years', 'item_fields', 'work_fields', 'setup_fields', 'plus_points', 'itemname']

    #수정된 데이터 받아오기(form.cleaned_data.get())
    def clean_ceoname(self):
        ceoname = self.cleaned_data.get('ceoname')
        return ceoname
    def clean_itemname(self):
        itemname = self.cleaned_data.get('itemname')
        return itemname
    def clean_years(self):
        years = self.cleaned_data.get('years')
        return years
    def clean_item_fields(self):
        item_fields = self.cleaned_data.get('item_fields')
        return item_fields
    def clean_work_fields(self):
        work_fields = self.cleaned_data.get('work_fields')
        return work_fields
    def clean_setup_fields(self):
        setup_fields = self.cleaned_data.get('setup_fields')
        return setup_fields
    def clean_plus_points(self):
        plus_points = self.cleaned_data.get('plus_points')
        return plus_points

    def save(self):
        ss = super().save(commit=False)
        if 0 <= ss.plus_points <=5 :
            ss.save()
        else:
            raise forms.ValidationError(_('점수를 확인해주세요.'), code='invalid')



# 회원가입 뷰(현재 admin에서만 사용)
# 이게 없으면 왜 유저를 생성해도 로그인이 안되지?
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = '__all__'

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



# 기본 홈 뷰
class HomeView(TemplateView):
    #Listview에는 model명을 적지 않으면 에러남
    # model = MyUser
    template_name = 'django_ex/home.html'
    # (listview를 상속받았을 경우)context_object_list의 디폴트 값은 object_list 또는 모델명소문자_list로 자동 지정된다.
    # context_object_list =

class BaseListView(TemplateView):
    template_name = 'django_ex/base_info_list.html'

class TestListView(TemplateView):
    template_name = 'django_ex/test_list.html'

# class FirstTestView(ListView):
#     """
# 	ListView 디폴트 지정 속성
# 	1) 컨텍스트 변수 : object_list
# 	2) 템플릿 파일 : 모델명소문자_list.html
# 	"""
#     form_class = CheckCeoForm
#     template_name = 'django_ex/test_1.html'
#     context_object_name = 'years_list'
#
#     def get_queryset(self):
#         # 모델 필드에 초이스 값을 쿼리
#         years = Ceo._meta.get_field('years').choices
#         list_count = len(years)
#         count = []
#         # 0 < list_count
#         for i in range(0,list_count):
#             list = years[i][0]
#             count.append(list)
#         return count
#
#     def post(self, request, *args, **kwargs):
#         selected = request.POST.get('year')
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             return render(request, 'django_ex/test_list_1.html', {'checkceoform':form})
#         return render(request, 'django_ex/test_list_1.html', {'checkceoform':form})


def select_th(request):
    return HttpResponse('aaaaaaa')


def select_year_results(request):
    # 필드명에 해당하는 필드 인스턴스를 돌려준다. (years의 choices항목들을 모두 가져옴)
    years = Ceo._meta.get_field('years').choices
    list_count = len(years)
    count = []
    # 0 < list_count
    # years 초이스 개수만큼 for문을 돌려서 count에 초이스의 항목들을 모두 담는다.
    for i in range(0,list_count):
        list = years[i][0]
        count.append(list)
    # return count

    if request.method == 'POST':
        selected_year = request.POST.get('year')
        score_list = Score.objects.filter(ceo__years=selected_year)
        return redirect('django_ex:select_th')
    else:
        form = CheckCeoForm()

    context = {
        'years_list':count,
        'ceos':form,
    }
    return render(request, 'django_ex/select_year_results.html', context)



def select_year(request):
    # 필드명에 해당하는 필드 인스턴스를 돌려준다. (years의 choices항목들을 모두 가져옴)
    years = Ceo._meta.get_field('years').choices
    list_count = len(years)
    count = []
    # 0 < list_count
    # years 초이스 개수만큼 for문을 돌려서 count에 초이스의 항목들을 모두 담는다.
    for i in range(0,list_count):
        list = years[i][0]
        count.append(list)
    # return count

    if request.method == 'POST':
        selected_year = request.POST.get('year')
        # selected_year = 2019
        ceo_list = Ceo.objects.filter(years=selected_year)
        # ceo_list = Score.objects.get(ceo__years=selected_year)
        return render(request, 'django_ex/test_list_1.html', {'ceo_list':ceo_list, 'year':selected_year})
        # form = CheckCeoForm(instance=selected_year)
        # if form.is_valid():
        #     return render(request, 'django_ex/test_list_1.html', {'ceos':form})
        # else:
        #     form.errors
    else:
        form = CheckCeoForm()

    context = {
        'years_list':count,
        'ceos':form,
    }
    return render(request, 'django_ex/select_year.html', context)


def document_results(request, current_user, current_ceo):
    forms = Ceo.objects.get(id=current_ceo)
    ceo_score_info = Score.objects.get(myuser_id=current_user, ceo_id=current_ceo)
    ceo_plus_score = Ceo.objects.get(ceo_relation=current_user, id=current_ceo)

    # sum_score = []
    list = [ceo_score_info.score_0, ceo_score_info.score_1, ceo_score_info.score_2, ceo_score_info.score_3, ceo_score_info.score_4, ceo_score_info.score_5, ceo_score_info.score_6, ceo_score_info.score_7]
    list_1 = [ceo_plus_score.plus_points]
    # sum_score.extend(list+list_1)

    middle_sum_score = sum(list)
    final_sum_score = sum(list+list_1)
    context = {
        'show_score' : ceo_score_info,
        'post' : forms,
        'sum' : middle_sum_score,
        'sum_score': final_sum_score,
    }
    return render(request, 'django_ex/document_results.html', context)


def test_total_results(request):
    score = Score.objects.filter(ceo__years=datetime.datetime.now().year)
    context = {
        'score':score,
    }
    return render(request, 'django_ex/total_results.html', context)


# ceoname을 서류평가 템플릿의 {% for in %} 태그에서 사용하기 위한 view
def document_list(request, current_user):
    # flat=True는 values_list다음 또 다른 필드의 사용을 알려주는 것이다.
    ceo_list = Ceo.objects.order_by('id')
    return render(request, 'django_ex/document_list.html', {'ceo_list':ceo_list})

#ceoname을 발표평가 템플릿의 {% for in %}태그에서 사용하기 위한 view
def presentation_list(request, current_user):
    ceoname = Ceo.objects.values_list('ceoname', flat=True).order_by('id')
    return render(request, 'django_ex/presentation_list.html', {'ceo_list':ceoname})


# ceoform을 템플릿에서 사용하기 위해 호출한 view
def base_info(request):
    try:
        if request.method == 'POST':
            ceoform = CeoForm(data=request.POST or None)
            # 폼에서 정의된 유효성 검증 규칙에 맞다면 - is_valid
            if ceoform.is_valid():
                ceoform.save()
                # messages.success(request, '저장되었습니다.')
                return redirect('django_ex:base_info')
            elif request.is_ajax():
                try:
                    g1 = request.POST['ceoname']
                    g2 = request.POST['years']
                    g3 = request.POST['item_fields']
                    g4 = request.POST['work_fields']
                    g5 = request.POST['setup_fields']
                    g6 = request.POST['plus_points']
                    g7 = request.POST['itemname']
                    return HttpResponse("sjfl")
                except KeyError:
                    return HttpResponse('Error')
            else:
                ceoform.errors
        else:
            ceoform=CeoForm()
        return render(request, 'django_ex/base_info.html', {'ceoform':ceoform})
    except ValidationError:
        messages.info(request, "가점의 범위를 벗어났습니다.")
        return render(request, 'django_ex/base_info.html', {'ceoform':ceoform})


def document_post(request, current_user, current_ceo):
    try:
        # values_list('ceoname') 메서드를 사용하면 ceoname값만 불러오기 떄문에 템플릿에서 ceoname.id값을 호출하면 id에 대한 에러가 남.
        ceo_instance = Ceo.objects.get(id=current_ceo)
        myuser_instance = MyUser.objects.get(id=current_user)
        check_exists = Score.objects.filter(myuser_id=myuser_instance.pk, ceo_id=ceo_instance.pk).exists()
        # shell api를 이용해서 연구함, post할 때 ForeignKey값을 저장하는 방법, instance 매개변수 사용
        foreign_instance = Score(myuser=myuser_instance, ceo=ceo_instance)
        # 같은 평가자와 지원자의 정보가 이미 존재할 때 결과로 리다이렉트 한다.
        if check_exists == True:
            return redirect(reverse('django_ex:document_results', args=(current_user, current_ceo)))
        elif request.method == 'POST':
            # 유저와 지원자에 대한 정보가 일치하는 score에 접근하도록 지정
            scoreform = ScoreForm(request.POST, instance=foreign_instance)
            ceoform = CeoForm(request.POST, instance=ceo_instance)
            if scoreform.is_valid():
                scoreform.save()
                # 점수 저장이 완료되어 결과값을 볼 수 있는 화면으로 리다이렉트
                return HttpResponseRedirect(reverse('django_ex:document_results', args=(current_user, current_ceo)))
            else:
                scoreform.errors
                return render(request, 'django_ex/document_post.html', {'score':scoreform})
        else:
            scoreform = ScoreForm()
            ceoform = CeoForm(instance=ceo_instance)

        context = {
            'ceoform':ceoform,
            'post':ceo_instance,
            'score':scoreform,
        }

        # 유효성 검사에 실패하였으므로 점수 입력하던 화면으로 리다이렉트(배점에 맞춰 입력해야함)
        return render(request, 'django_ex/document_post.html', context)
    except ValidationError:
        context = {
            'ceoform':ceoform,
            'post':ceo_instance,
            'score':scoreform,
        }
        messages.info(request, "점수를 확인하세요.")
        return render(request, 'django_ex/document_post.html', context)
    except IntegrityError:
        # unique_together옵션으로 평가자명과 지원자/기업명이 같으면 이미 평가가 완료된 상태를 뜻하기 떄문에 지원자 목록으로 리다이렉트 (check_exists를 생성한 이후로 불필요한 예외처리)
        return redirect('django_ex:document_list', current_user)


def base_info_check(request):
    try:
        if request.method == 'POST':
            form = CheckCeoForm(request.POST)
            input_form = CeoForm(request.POST)
            if form.is_valid():
                get_value = request.POST.get('ceos')
                get_years = request.POST.get('years')
                post = Ceo.objects.filter(years=get_years).get(id=get_value)
                context = {
                    'post':post,
                    'ceos':form,
                    'input_form':input_form,
                }
                return render(request, 'django_ex/base_info_reviews.html', context)
            else:
                form.errors
        else:
            form = CheckCeoForm()
        return render(request, 'django_ex/base_info_check.html', {'ceos':form})
    except Ceo.DoesNotExist:
        year = request.POST.get('years')
        messages.info(request, year+'년도에 지원한 지원자가 맞는지 확인해주세요.')
        return redirect('django_ex:base-info-check')

def checked_evaluation(request, current_user):
    try:
        if request.method == 'POST':
            form = CheckCeoForm(request.POST)
            # scoreform = ScoreForm(request.POST) #user 데이터는 request.user로 바로 받아올 수 있는것같음
            if form.is_valid():
                get_year = request.POST.get('years')
                get_value = request.POST.get('ceos')
                current_user = current_user
                current_ceo = get_value
                post = Ceo.objects.get(id=get_value)
                # ceo_score_info = Score.objects.get(myuser_id=current_user, ceo_id=current_ceo)
                ceo_score_info = Score.objects.filter(ceo__years=get_year).get(myuser_id=current_user, ceo_id=current_ceo)

                list = [ceo_score_info.score_0, ceo_score_info.score_1, ceo_score_info.score_2, ceo_score_info.score_3, ceo_score_info.score_4, ceo_score_info.score_5, ceo_score_info.score_6, ceo_score_info.score_7]
                list_1 = [post.plus_points]
                subtotal = sum(list)
                total = sum(list+list_1)
                context = {
                    'ceos':form,
                    'show_score':ceo_score_info,
                    'post':post,
                    'subtotal':subtotal,
                    'total':total,
                }
                # return HttpResponseRedirect(reverse('django_ex:document_results', args=(current_user, current_ceo)))
                return render(request, 'django_ex/checked_evaluation_results.html', context)
            else:
                form.errors
        else:
            form = CheckCeoForm()
        #다운로드가 진행된 코드
        # return HttpResponse(request, 'django_ex/show_evaluation.html')
        return render(request, 'django_ex/checked_evaluation.html', {'ceos':form})
    except ObjectDoesNotExist:
        messages.info(request, '해당년도의 자료가 아니거나, 평가가 완료되지 않은 지원자입니다.')
        return redirect('django_ex:checked-evaluation', current_user)


def base_info_change(request, current_ceo):
    post = Ceo.objects.get(id=current_ceo)
    if request.method == 'POST':
        ceoform = CeoForm(request.POST, instance=post)
        if ceoform.is_valid():
            ceoform.save()
            return redirect('django_ex:base-info-check')
        else:
            ceoform.errors
    else:
        ceoform = CeoForm(instance=post)
    context = {
        'ceoform':ceoform,
        'post':post,
    }
    return render(request, 'django_ex/base_info_change.html', context)


def changed_evaluation(request, current_user, current_ceo):
    try:
        ceo_score_info = Score.objects.get(myuser_id=current_user, ceo_id=current_ceo)
        post = Ceo.objects.get(id=current_ceo)
        if request.method == 'POST':
            scoreform = ScoreForm(request.POST, instance=ceo_score_info)
            if scoreform.is_valid():
                scoreform.save()
                return redirect('django_ex:checked-evaluation', current_user)
                # return render(request, 'django_ex/checked_evaluation_results.html', context)
            else:
                scoreform.errors
        scoreform = ScoreForm(instance=ceo_score_info)
        context = {
            'scoreform':scoreform,
            'post':post,
        }
        return render(request, 'django_ex/changed_evaluation.html', context)

    except ValidationError:
        context = {
            'scoreform':scoreform,
            'post':post,
        }
        messages.info(request, "점수를 확인하세요.")
        return render(request, 'django_ex/changed_evaluation.html', context)







    # ceo_score_info = Score.objects.get(myuser_id=current_user, ceo_id=current_ceo)
    # post = Ceo.objects.get(id=current_ceo)
    # if request.method == 'POST':
    #     scoreform = ScoreForm(request.POST, instance=ceo_score_info)
    #     if scoreform.is_valid():
    #         scoreform.save()
    #         return redirect('django_ex:checked-evaluation', current_user)
    #         # return render(request, 'django_ex/checked_evaluation_results.html', context)
    #     else:
    #         scoreform.errors
    # else:
    #     scoreform = ScoreForm(instance=ceo_score_info)
    #
    # context = {
    #     # 'ceos':ceos,
    #     'post':post,
    #     'scoreform':scoreform,
    # }
    # return render(request, 'django_ex/changed_evaluation.html', context)
