#
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
