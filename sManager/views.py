from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse_lazy
from django.db.models import Q, Sum
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

from typing import Any
from itertools import groupby
from datetime import timedelta

from sManager.models import *
from sManager.forms import *
    
# Create your views here.


def replace_none_with_zero(input_dict):
    for key, value in input_dict.items():
        if value is None:
            input_dict[key] = 0
    return input_dict

def str_to_int(string):
    return int(''.join(filter(str.isdigit, string)))



class AccessRestrictionMixin:
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        # Проверка на то, принадлежит ли объект текущему пользователю
        if self.object.creator != self.request.user:
            context = {
                'message': "You don't have permission for this action."
            }
            return render(request, 'general/permission.html', context)

        return super().get(request, *args, **kwargs)

class DeleteObjectMixin(LoginRequiredMixin, AccessRestrictionMixin, DeleteView):
    template_name = 'general/delete_template.html'
    success_url = reverse_lazy('sManager:home-page')

   


@login_required
def homePage(request):
    current_datetime = timezone.now().date()
    filter_option = request.GET.get('confirmationFilter', 'default')
    products_gen = Product.objects.filter(creator=request.user).filter(
            Q(date__gt=current_datetime) | Q(date=current_datetime))
    

    if filter_option in ['True', 'False']:
        products = products_gen.filter(confirmed=(filter_option == 'True')).order_by('date')
    else:
        products = products_gen.order_by('date')

    grouped_products = {}
    for date, group in groupby(products, key=lambda x: x.date):
        grouped_products[date] = list(group)
    
    return render(request, 'sManager/home.html', {
        'grouped_products': grouped_products,
        'today': current_datetime,
        'filter': filter_option
    })

@login_required
def redirectToHomePage(request):
    return redirect('sManager:home-page')

#** IMPORTANT: Supply 
class CreateSupplyView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'sManager/supply/create_supply.html'
    success_url = reverse_lazy('sManager:home-page')
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        # form.cost = str_to_int(request.POST.get('cost'))
        # return HttpResponse(str_to_int(request.POST.get('cost')))
        # return HttpResponse(int(''.join(filter(str.isdigit, request.POST.get('cost')))))
        if form.is_valid():
            form = form.save(commit=False)
            form.name = Supplier.objects.get(
                name=request.POST.get('supply-input'))
            form.creator = request.user
            form.cost = str_to_int(request.POST.get('cost'))

            form.save()
            messages.success(
                self.request,
                f'Поставка «{form.name}» успешно добавлена.'
            )
            return redirect('sManager:home-page')
        else:
            return HttpResponse('pro')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['suppliers'] = Supplier.objects.filter(
            creator=self.request.user).order_by('name')

        return context

# class EditSupplyView(LoginRequiredMixin, AccessRestrictionMixin,UpdateView):
#     model = Product
#     form_class = SupplyEditForm
#     template_name = 'sManager/supply/update_supply.html'
#     success_url = reverse_lazy('sManager:home-page')

   
#     def post(self, request, *args, **kwargs):
#         # return HttpResponse(1)
#         if len(request.FILES.getlist('files')) > 0:

#             ProductImages.objects.filter(supply_id=self.kwargs['pk']).delete()
#             for uploaded_file in request.FILES.getlist('files'):
#                 ProductImages.objects.create(
#                     images=uploaded_file, supply_id=self.kwargs['pk'])
#         self.object = self.get_object()

#         # print(self.object)
#         # print('posted: ', self.get_object().payment)
#         return super().post(request, *args, **kwargs)

#     def form_valid(self, form):
#         form_instance = form.save(commit=False)
#         cost = str_to_int(self.request.POST.get('cost'))
#         # return HttpResponse(int(''.join(filter(str.isdigit, cost))))
#         if form_instance.confirmed:
#             if form_instance.payment == 'mix':
#                 # return HttpResponse(self.request.POST.get('mix-transfer'))
#                 form_instance.cash_amount = v
#                 form_instance.transfer_amount =str_to_int(self.request.POST.get('mix-transfer'))
#             elif form_instance.payment == 'cash':
#                 form_instance.transfer_amount = 0
#                 form_instance.cash_amount = cost

#             elif form_instance.payment == 'transfer':
#                 form_instance.transfer_amount = cost
#                 form_instance.cash_amount = 0
#         else:
#             form_instance.payment = 'cash'
#         form_instance.cost = cost
#         form_instance.creator = self.request.user
        
#         form_instance.save()

#         messages.success(
#             self.request,
#             f'Поставка «{form_instance.name}» успешно изменена. '
#         )
#         return super().form_valid(form)
#     def form_invalid(self, form):
#         print("Form is invalid")
#         print(form.errors)
#         return HttpResponse('Form is invalid')
#         return super().form_invalid(form)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['date'] = self.object.date
#         context['today'] = timezone.now().date()
#         # context['']

#         return context


class EditSupplyView(LoginRequiredMixin,AccessRestrictionMixin, UpdateView):
    model = Product
    form_class = SupplyEditForm
    template_name = 'sManager/supply/update_supply.html'
    success_url = reverse_lazy('sManager:home-page')

   
    def post(self, request, *args, **kwargs):
        if len(request.FILES.getlist('files')) > 0:

            ProductImages.objects.filter(supply_id=self.kwargs['pk']).delete()
            for uploaded_file in request.FILES.getlist('files'):
                ProductImages.objects.create(
                    images=uploaded_file, supply_id=self.kwargs['pk'])
        self.object = self.get_object()

        # print(self.object)
        print('posted: ', self.get_object())
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form_instance = form.save(commit=False)
        cost = str_to_int(self.request.POST.get('cost'))
        if form_instance.payment == 'mix':
            # cash = self.request.POST.get('mix-cash')
            # transfer = self.request.POST.get('mix-transfer')
            form_instance.cash_amount = str_to_int(self.request.POST.get('mix-cash'))
            form_instance.transfer_amount = str_to_int(self.request.POST.get('mix-transfer'))
        elif form_instance.payment == 'cash':
            
            form_instance.transfer_amount = 0
            form_instance.cash_amount = cost
        elif form_instance.payment == 'transfer':
            
           
            form_instance.transfer_amount = cost
            form_instance.cash_amount = 0
        form_instance.creator = self.request.user
        form_instance.cost=  cost
        form_instance.save()

        messages.success(
            self.request,
            f'Поставщик «{form_instance.name}» успешно изменен. '
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = self.object.date
        context['today'] = timezone.now().date()
        # context['']

        return context

class DeleteSupplyView(DeleteObjectMixin):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = 'sManager:home-page'
        return context




def productSumCalculation(request, confirmed=True, date=timezone.now(), extra=False, json=True):
    request_db_result_dict = {
        'cash':0,
        'transfer':0
    }
    if confirmed:
        request_db = Product.objects.filter(creator=request.user).filter(
            date=date).filter(confirmed=confirmed)

        for obj in request_db:
            if obj.payment == 'mix':
                 request_db_result_dict['cash'] += obj.cash_amount
                 request_db_result_dict['transfer'] += obj.transfer_amount
            elif obj.payment == 'cash':
                request_db_result_dict['cash'] += obj.cash_amount
            else:
                request_db_result_dict['transfer'] += obj.transfer_amount
        

    else:
        request_db = Product.objects.filter(
            creator=request.user).filter(date=date).all()

    request_db_result_dict['total'] = request_db.aggregate(total=Sum('cost'))[
        'total']
    if extra:
            request_db_extra = Money.objects.filter(creator=request.user).filter(
            date=date)
            # return HttpResponse(request_db_extra)
            request_db_result_dict['income'] = 0
            request_db_result_dict['expense'] = 0
            for obj in request_db_extra:
                if obj.content[0] == '+':
                    request_db_result_dict['income'] += str_to_int(obj.content)
                else:
                    request_db_result_dict['expense'] += str_to_int(obj.content)
            request_db_result_dict['income']
            request_db_result_dict['expense']
   
    
    # return JsonResponse(replace_none_with_zero(request_db_result_dict))
    if json:
        return JsonResponse(replace_none_with_zero(request_db_result_dict))
    else:
        return replace_none_with_zero(request_db_result_dict)


#** IMPORTANT: Supplier
class SuppliersListView(LoginRequiredMixin, ListView):
    template_name = 'sManager/supplier/suppliers.html'
    model = Supplier
    context_object_name = 'suppliers'

    def get_queryset(self) -> QuerySet[Any]:
        return Supplier.objects.filter(
            creator=self.request.user).order_by('-published')

class CreateSupplierView(LoginRequiredMixin, CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'sManager/supplier/create-suppliers.html'
    success_url = reverse_lazy('sManager:suppliers')

    def form_valid(self, form):
        form_instance = form.save(commit=False)
        form_instance.creator = self.request.user
        form_instance.save()

        messages.success(
            self.request,
            f'Поставщик «{form_instance.name}» успешно создан.'
        )
        return super().form_valid(form)
    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        print(form.errors)
        return HttpResponse('Form is invalid')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        json_data = Supplier.objects.filter(
            creator=self.request.user).values('id', 'name')
        context['suppliers'] = list(json_data)

        return context

class DeleteSupplierView(DeleteObjectMixin):
    model = Supplier
    success_url = reverse_lazy('sManager:suppliers')

    def post(self, request, *args, **kwargs):
        messages.success(
            request,
            f'Поставщик «{self.get_object()}» успешно удален.')

        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = 'sManager:suppliers'
        return context

class EditSupplierView(LoginRequiredMixin, AccessRestrictionMixin,UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'sManager/supplier/update_supplier.html'
    success_url = reverse_lazy('sManager:suppliers')

   
    def form_valid(self, form):
        form_instance = form.save(commit=False)
        form_instance.creator = self.request.user
        form_instance.save()

        messages.success(
            self.request,
            f'Поставщик «{form_instance.name}» успешно изменен.'
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        json_data = Supplier.objects.filter(
            creator=self.request.user).values('id', 'name')
        context['suppliers'] = list(json_data)

        return context


#** IMPORTANT: Client
class ClientsListView(LoginRequiredMixin, ListView):
    template_name = 'sManager/client/clients-list.html'
    model = Client
    context_object_name = 'clients'
    def get_queryset(self):
        sort_order = self.request.GET.get('sort', 'default')

        # Получаем клиентов, отсортированных по `is_chosen` и дате изменения
        clients = Client.objects.filter(creator=self.request.user).order_by('-is_chosen', '-last_modified')

        # Вычисляем сумму долгов для клиентов, используя аннотацию
        clients = clients.annotate(debt_summ=Sum('debt__content'))

        if sort_order == 'debt_asc':
            clients = clients.order_by('-is_chosen', 'debt_summ', '-last_modified')
        elif sort_order == 'debt_desc':
            clients = clients.order_by('-is_chosen', '-debt_summ', '-last_modified')
        elif sort_order == 'oldest':
            clients = clients.order_by('-is_chosen', '-last_modified')
        elif sort_order == 'newest':
            clients = clients.order_by('-is_chosen', 'last_modified')
        else:
            clients = clients.order_by('-is_chosen', '-last_modified')

        return clients

class ClientEditView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'sManager/client/client.html'
    context_object_name = 'client'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('sManager:clients-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        client_id = self.object.id
        debts = Debt.objects.filter(creator=user, client_id=client_id)
        
        array = [{'content': obj.content, 'date': obj.date, 'id': obj.id} for obj in debts]
        
        transactions = []
        current_operations = []
        current_refund = []
        current_balance = 0

        for item in array:
            value = item['content']
            number = int(value)
            if number >= 0:
                current_operations.append(item)
            else:
                current_refund.append(item)
            current_balance += number

            if number < 0 or item == array[-1]:
                transactions.append({
                    'operations': current_operations.copy(),
                    'sum': eval(''.join([op['content'] for op in current_operations])),
                    'refund': current_refund.copy(),
                    'balance': current_balance
                })
                current_operations = [{'content': str(current_balance), 'date': item['date'], 'id': item['id']}] if number < 0 else []
                current_refund = []
        json_data = Client.objects.filter(
            creator=self.request.user).values('id', 'name')
        context['all_clients'] = list(json_data)
        context['transactions'] = transactions
        context['client'] = Client.objects.filter(creator = self.request.user, id = self.object.id).first()
        return context
    def post(self, request, *args, **kwargs):
        messages.success(
            request,
            f'Клиент «{self.get_object()}» успешно обновлен.')

        return super().post(request, *args, **kwargs)

class ClientDeleteView(DeleteObjectMixin):
    model = Client
    success_url = reverse_lazy('sManager:clients-list')

    def post(self, request, *args, **kwargs):
        messages.success(
            request,
            f'Клиент «{self.get_object()}» успешно удален.')

        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = 'sManager:clients-list'
        return context

#** IMPORTANT: Debt
class DebtView(LoginRequiredMixin, ListView):
    template_name = 'sManager/client/debt.html'
    model = Client
    form_class = DebtForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()  # Instantiate the form class
        context['clients'] = Client.objects.filter(
            creator=self.request.user)

        return context
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            name = request.POST.get('client_name')
            content = request.POST.get('content')
            if content in ['+', '-']:
                messages.error(self.request,f'Недопустимое значение: «{content}»')
                return redirect('sManager:clients-list')
            try:
                client_instance = Client.objects.get(
                    name=name, creator=request.user)
            except Client.DoesNotExist:
                # If the client doesn't exist, create a new one
                phone_number = request.POST.get('tel_number')
                about = request.POST.get('about')
                client_instance = Client.objects.create(
                    name=name,about = about, phone_number = phone_number, creator=request.user)

            obj.client = client_instance
            if content[0] not in ['+','-']:
                content = '+' + content
            obj.content = content
            
            obj.creator = request.user
            obj.save()
            messages.success(
            request,
            f'Долг в размере «{content}» успешно добавлен клиенту «{client_instance}».')
            return redirect('sManager:clients-list')
        else:
            return HttpResponse('non valid')

class DebtEditView(LoginRequiredMixin,AccessRestrictionMixin, UpdateView):
    model = Debt
    form_class = DebtForm
    template_name = 'sManager/client/debt-edit.html'
    success_url = reverse_lazy('sManager:clients-list')

    def form_valid(self, form):
        content =  self.request.POST.get('content')
        if self.request.POST.get('content') in ['+', '-']:
            messages.error(self.request,f'Недопустимое значение: «{content}»')
            return redirect('sManager:clients-list')
        if content[0] not in ['+','-']:
                content = '+' + str(int(content))
        else:
            content = content[0] + str(abs(int(content)))
        form_instance = form.save(commit=False)
        form_instance.creator = self.request.user
        form_instance.save()

        messages.success(
            self.request,
            f'Долг успешно изменен.'
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['page'] = 'sManager:debt-edit'
        context['debt_date'] = Debt.objects.get(id = self.kwargs['pk']).date
        return context
    
class DebtDeleteView(DeleteObjectMixin):
    model = Debt
    success_url = reverse_lazy('sManager:clients-list')

    def post(self, request, *args, **kwargs):
        messages.success(
            request,
            f'Поставщик «{self.get_object()}» успешно удален.')

        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = 'sManager:clients-list'
        return context

#** IMPORTANT: History
class HistoryGeneralView(LoginRequiredMixin, ListView):
    template_name = 'sManager/history/history.html'
    model = Product
    context_object_name = 'supplies'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        json_data = Supplier.objects.filter(
            creator=self.request.user).values('id', 'name')
        context['suppliers'] = list(json_data)

        return context


def historySearch(request, date):
    products = Product.objects.filter(creator=request.user, date=date)
    data = {'products': list(products.values())}
    return JsonResponse(data)


class HistorySpecificView(LoginRequiredMixin, AccessRestrictionMixin, DetailView):
    template_name = 'sManager/history/history-view.html'
    model = Product

    


class ProfilePageView(LoginRequiredMixin, ListView):
    template_name = 'sManager/profile.html'
    model = Product
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_image'] = ProfileForm()  # Добавьте форму в контекст
        try:
            context['profile'] = get_object_or_404(Profile, profile=self.request.user)  # Предполагая, что у пользователя есть профиль
        except:
            context['profile'] = None  # Предполагая, что у пользователя есть профиль
        return context
    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid(): 
            profile_image = form.cleaned_data['image']

            # Получаем профиль пользователя
            profile, created = Profile.objects.update_or_create(
                profile=self.request.user,  # Предполагая, что у вас есть поле user в модели Profile
                defaults={'image': profile_image}
            )
            return redirect('profile')  # Перенаправьте на страницу профиля или другую страницу по вашему выбору
        else:
            context = self.get_context_data()
            context['form_image'] = form
            return render(request, self.template_name, context)

@login_required
def updateUserData(request):

    username = request.POST.get('username')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    if request.POST.get('current_password'):
        user_pass = User.objects.get(username=request.user)
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')

        user = request.user
        if user.check_password(current_password):
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Password changed successfully')
            user = authenticate(request, username=user, password=new_password)
            login(request, user)
           
        else:
            messages.error(request, 'Current password is incorrect')
    else:
        # return HttpResponse(request.user.id)
        user_db = User.objects
        if user_db.filter(username=username).exclude(id=request.user.id).exists():
            messages.error(request, 'Пользователь с таким именем уже существует.')
           
        else:
            user_db.filter(id=request.user.id).update(username=username, first_name=first_name, last_name=last_name, email=email)
            messages.success(request, 'Информация о пользователе успешно изменена.')
 
    return redirect('profile')

@login_required
def deleteProfilePhoto(request, id):
    Profile.objects.get(profile_id=id).delete()
    return redirect('profile')


class SettingsPageView(LoginRequiredMixin, ListView):
    template_name = 'sManager/settings.html'
    model = Supplier

class FinancePageView(LoginRequiredMixin, ListView):
    template_name = 'sManager/finance.html'
    model = Money
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_date = timezone.now().date()
        context['moneys'] = Money.objects.filter(creator = self.request.user).filter(date = current_date).order_by('-datetime')
        context['records'] = FinanceRecord.objects.filter(creator = self.request.user).filter(date__lt = current_date)
        context['today'] = productSumCalculation(self.request, confirmed=True, date=current_date, extra=True, json=False)
        print(context['today'])

        return context



@login_required
def moneyAdd(request):

    content = request.POST.get('moneyInput')
    text = request.POST.get('moneyText')
    if content in ['+', '-'] or str_to_int(content) < 1:
                messages.error(request,f'Недопустимое значение: «{content}»')
                return redirect('sManager:finance')
    if content[0] not in ['+','-']:
                content = '+' + str(int(content))
    else:
        content = content[0] + str(abs(int(content)))
    
    if content[0] == '+':
        messages.success(
            request,
            f'Вложение в размере «{content}» успешно создано.')
    else: 
        messages.success(
            request,
            f'Расход в размере «{content}» успешно создан.')
    Money.objects.create(content = content, text = text, creator = request.user)
    
    return redirect('sManager:home-page')

@login_required
def debtAdd(request):
    id = request.POST.get('clientId')
    content = request.POST.get('content')
    if content in ['+', '-'] or str_to_int(content) < 1:
        messages.error(request,f'Недопустимое значение: «{content}»')
        return redirect('sManager:client-edit', id = id)
    if content[0] not in ['+','-']:
                content = '+' + str(int(content))
    else:
        content = content[0] + str(abs(int(content)))
    description = request.POST.get('description')
    obj = Debt.objects.create(client_id = id, content = content, description = description, creator = request.user)
    obj.save()
    messages.success(
            request,
            f'Долг в размере «{content}» успешно добавлен клиенту.')
    return redirect('sManager:client-edit', id = id)



class MoneyEditView(LoginRequiredMixin, AccessRestrictionMixin, UpdateView):
    model = Money
    form_class = MoneyForm
    template_name = 'sManager/client/debt-edit.html'
    success_url = reverse_lazy('sManager:finance')

    

    def form_valid(self, form):
        form_instance = form.save(commit=False)
        content = self.request.POST.get('content')
        if content in ['+', '-'] or str_to_int(content) < 1:
            messages.error(self.request,f'Недопустимое значение: «{content}»')
            return redirect('sManager:finance')
        if content[0] not in ['+','-']:
                content = '+' + str(int(content))
        else:
            content = content[0] + str(abs(int(content)))
        form_instance.content = content
        form_instance.creator = self.request.user
        form_instance.save()

        messages.success(
            self.request,
            f'успешно изменен.'
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['page'] = 'sManager:money-delete'
        return context
    
class MoneyDeleteView(DeleteObjectMixin):
    model = Money

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = 'sManager:home-page'
        return context