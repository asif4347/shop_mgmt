from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .forms import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , authenticate
from .forms import *
from django.http import HttpResponse
from django.forms import formset_factory
from django.forms import ValidationError as FormValidationError
# https://stackoverflow.com/questions/42613200/python-django-pass-argument-to-form-clean-method
import xlwt

def loginView(request):
    if request.method == "GET":
        return render(request, 'app1/login.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(
            username=request.POST.get('username', '').strip(),
            password=request.POST.get('password', ''),
        )

        print(username)
        r = login(request, user)
        # return render(request, 'app1/index.html')
        # return render(request, "app1/base1.html")
        return HttpResponseRedirect(reverse('index'))


@login_required(login_url=loginView)
def logout(request):
    auth.logout(request)
    return render(request, 'app1/login.html')


@login_required(login_url=loginView)
def indexView(request):
    orders = Orders.objects.all()
    all_salesman = Salesman.objects.all()
    all_shops = Shop.objects.all()
    print(orders)
    return render(request, 'app1/index.html', {'orders': orders, 'all_salesman':all_salesman, 'all_shops':all_shops})

@login_required(login_url=loginView)
def DisplaySalesmanView(request):
    salesmen = Salesman.objects.all()
    return render(request, 'app1/index.html', {'salesmen':salesmen})


@login_required(login_url=loginView)
def DisplayShopView(request):
    shops = Shop.objects.all()
    return render(request, 'app1/index.html', {'shops': shops})


@login_required(login_url=loginView)
def AddSalesmanView(request):
    if request.method == 'POST':

        form = AddSalesmanForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('display_salesman'))
        else:
            print(form.errors)
        return HttpResponseRedirect(reverse('index'))

    else:
        form = AddSalesmanForm()
        return render(request, 'app1/add_item.html', {'form': form, 'header': 'Salesman'})


@login_required(login_url=loginView)
def AddShopView(request):
    if request.method == 'POST':

        form = AddShopForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('display_shops'))
        else:
            print(form.errors)
        return HttpResponseRedirect(reverse('index'))

    else:
        form = AddShopForm()
        return render(request, 'app1/add_item.html', {'form': form, 'header': 'Shop'})


# @login_required(login_url=loginView)
# def AddOrderView(request):
#     if request.method == 'POST':
#
#         form = OrderProductForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('index'))
#         else:
#             print(form.errors)
#         return HttpResponseRedirect(reverse('index'))
#
#     else:
#         form = OrderProductForm()
#         return render(request, 'app1/orders_form.html', {'form': form, 'header': 'Order'})
#

@login_required(login_url=loginView)
def EditView(request, pk, form_cls, model):
    item = get_object_or_404(model, pk=pk)
    if request.method == "POST":

        form = form_cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        if model == Salesman:
            return redirect('display_salesman')
        elif model == Shop:
            return redirect('display_shops')
        else:
            return redirect('index')


    else:
        form = form_cls(instance=item)
        if model == Salesman:
            context ={'form':form, 'header':'Salesman'}
        elif model == Shop:
            context = {'form': form, 'header': 'Shop'}
        elif model == Orders:
            context = {'form': form, 'header': 'Order'}
        elif model == Amount:
            context = {'form': form, 'header': 'Amount'}
        return render(request, "app1/edit_item.html", context)


@login_required(login_url=loginView)
def EditSalesmanView(request, pk):
    return EditView(request, pk, AddSalesmanForm, Salesman)


@login_required(login_url=loginView)
def EditShop(request, pk):
    return EditView(request, pk, AddShopForm, Shop)


@login_required(login_url=loginView)
def EditOrder(request, pk):
    return EditView(request, pk, AddOrderForm, Orders)

@login_required(login_url=loginView)
def EditAmount(request, pk):
    # item = get_object_or_404(Amount, pk=pk)
    # if request.method == "POST":
    #
    #     form = Amount(request.POST, instance=item)
    #     if form.is_valid():
    #         form.save()
    return EditView(request, pk, AddAmountForm, Amount)


@login_required(login_url=loginView)
def Deleteview(request, pk, model):
    model.objects.filter(id=pk).delete()
    items = model.objects.all()
    if model == Salesman:
        return redirect('display_salesman')
    elif model == Shop:
        return redirect('display_shops')


@login_required(login_url=loginView)
def delete_salesman(request, pk):
    return Deleteview(request, pk, Salesman)

@login_required(login_url=loginView)
def delete_shop(request, pk):
    return Deleteview(request, pk, Shop)

@login_required(login_url=loginView)
def delete_order(request, pk):
    return Deleteview(request, pk, Orders)

@login_required(login_url=loginView)
def SalesmanOrderView(request, pk):
    saleman = Salesman.objects.get(pk=pk)
    his_orders = Orders.objects.filter(salesman=saleman)
    return render(request, 'app1/index.html', {'orders': his_orders, 'his_orders': 'his_orders', 'name':saleman.name})


@login_required(login_url=loginView)
def OrderAmountView(request, pk):
    order = Orders.objects.get(pk=pk)
    amounts = order.amount_set.all()

    context = {
        'order':order,
        'amounts':amounts
    }
    return render(request, 'app1/amounts.html', context)

@login_required(login_url=loginView)
def AddAmountView(request, pk):
    order = Orders.objects.get(pk=pk)
    if request.method == 'POST':
        form = AddAmountForm(request.POST, order=order)

        if form.is_valid():
            modl = form.save(commit=False)
            modl.delivery = order
            modl.save()

        else:
            print(form.errors)
            return render(request, 'app1/add_item.html', {'form': form, 'header': 'Amount'})
        return redirect('order_amounts', order.pk)
    else:
        form = AddAmountForm(order=order)
        return render(request, 'app1/add_item.html', {'form':form, 'header': 'Amount'})


@login_required(login_url=loginView)
def filterView(request):
    start_date = request.POST.get('start-date')
    end_date = request.POST.get('end-date')
    order_id = request.POST.get('order-id')
    salesman_id = request.POST.get('salesman_id')
    shop_id = request.POST.get('shop_id')
    result = Orders.objects.none()
    if start_date and end_date:
        result = Orders.objects.filter(date__range=[start_date, end_date])
    elif start_date:
        result = Orders.objects.filter(date__range=[start_date, start_date])
    elif end_date:
        result = Orders.objects.filter(date__range=[end_date, end_date])
    elif start_date and salesman_id and shop_id:
        result = Orders.objects.filter(date__range=[start_date, end_date], salesman=salesman_id, shop=shop_id)
    elif salesman_id and shop_id:
        result = Orders.objects.filter(salesman=salesman_id, shop=shop_id)
    elif shop_id:
        result = Orders.objects.filter(shop=shop_id)
    elif salesman_id:
        result = Orders.objects.filter(salesman=salesman_id)
    all_salesman = Salesman.objects.all()
    all_shops = Shop.objects.all()
    return render(request, 'app1/index.html', {'orders': result, 'all_salesman': all_salesman, 'all_shops': all_shops})


class ProfileCreate(CreateView):
    model = Orders
    # fields = ['first_name', 'last_name']
    fields = '__all__'

class ProfileFamilyMemberCreate(CreateView):
    model = Orders
    # fields = ['first_name', 'last_name']
    fields = '__all__'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        data = super(ProfileFamilyMemberCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['familymembers'] = FamilyMemberFormSet(self.request.POST)
        else:
            data['familymembers'] = FamilyMemberFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        familymembers = context['familymembers']
        with transaction.atomic():
            self.object = form.save()

            if familymembers.is_valid():
                familymembers.instance = self.object
                familymembers.save()
            else:
                print(familymembers.errors)
                return render(self.request, 'app1/orders_form.html', {'form': form, 'familymembers': familymembers})
            # else:
            #     print(form.errors)
            #     # data['familymembers'] = FamilyMemberFormSet(self.request.POST)
            #     return render(self.request, 'app1/orders_form.html', {'form': form})
            # # return redirect('order_amounts', order.pk)
        return super(ProfileFamilyMemberCreate, self).form_valid(form)


class ProfileUpdate(UpdateView):
    model = Orders
    success_url = '/'
    # fields = ['first_name', 'last_name']
    fields = '__all__'

class ProfileFamilyMemberUpdate(UpdateView):
    model = Orders
    # fields = ['first_name', 'last_name']
    fields = '__all__'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        data = super(ProfileFamilyMemberUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['familymembers'] = FamilyMemberFormSet(self.request.POST, instance=self.object)
        else:
            data['familymembers'] = FamilyMemberFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        familymembers = context['familymembers']
        with transaction.atomic():
            self.object = form.save()
    
            if familymembers.is_valid():
                familymembers.instance = self.object
                familymembers.save()
        return super(ProfileFamilyMemberUpdate, self).form_valid(form)


class ProfileDelete(DeleteView):
    model = Orders
    success_url = reverse_lazy('profile-list')



# export

def export_orders_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="orders.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Orders')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['id', 'Salesman', 'Shop', 'Status', 'Total Amount', 'Amount Paid', 'Date']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Orders.objects.all().values_list('id', 'salesman__name', 'shop__name','status', 'total_amount', 'amount_paid','date' )
    print(rows)
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            if col_num == 6:
                date =str(row[col_num])
                ws.write(row_num, col_num, date, font_style)
            else:
                ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response