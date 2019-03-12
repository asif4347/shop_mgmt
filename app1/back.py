# class ProfileList(ListView):
#     model = Orders
#
#
# class OrderProductCreate(CreateView):
#     model = Orders
#     fields = '__all__'
#     success_url = reverse_lazy('index')
#     template_name = 'app1/orders_form.html'
#
#     def get_context_data(self, **kwargs):
#         data = super(OrderProductCreate, self).get_context_data(**kwargs)
#         if self.request.POST:
#             data['orderproducts'] = OrderProductFormSet(self.request.POST)
#         else:
#             data['orderproducts'] = OrderProductFormSet()
#         return data
#
#     def form_valid(self, form):
#         context = self.get_context_data()
#         orderproducts = context['orderproducts']
#         with transaction.atomic():
#             self.object = form.save()
#
#             if orderproducts.is_valid():
#                 orderproducts.instance = self.object
#                 orderproducts.save()
#         return super(OrderProductCreate, self).form_valid(form)
#
#
# class OrderUpdate(UpdateView):
#     model = Orders
#     success_url = '/'
#     fields = '__all__'
#
#
# class OrderProductUpdate(UpdateView):
#     model = Orders
#     exclude = ()
#     success_url = reverse_lazy('profile-list')
#
#     def get_context_data(self, **kwargs):
#         data = super(OrderProductUpdate, self).get_context_data(**kwargs)
#         if self.request.POST:
#             data['orderproducts'] = OrderProductFormSet(self.request.POST, instance=self.object)
#         else:
#             data['orderproducts'] = OrderProductFormSet(instance=self.object)
#         return data
#
#     def form_valid(self, form):
#         context = self.get_context_data()
#         orderproducts = context['orderproducts']
#         with transaction.atomic():
#             self.object = form.save()
#
#             if orderproducts.is_valid():
#                 orderproducts.instance = self.object
#                 orderproducts.save()
#         return super(OrderProductUpdate, self).form_valid(form)
#
#
# class OrderDelete(DeleteView):
#     model = Orders
#     success_url = reverse_lazy('index')
#
#
#
# class OrderUpdate(UpdateView):
#     model = Orders
#     success_url = '/'
#     fields = ['first_name', 'last_name']
#
#
# class ProfileFamilyMemberUpdate(UpdateView):
#     model = Orders
#     fields = ['first_name', 'last_name']
#     success_url = reverse_lazy('index')
#
#     def get_context_data(self, **kwargs):
#         data = super(ProfileFamilyMemberUpdate, self).get_context_data(**kwargs)
#         if self.request.POST:
#             data['orderproducts'] = OrderProductFormSet(self.request.POST, instance=self.object)
#         else:
#             data['orderproducts'] = OrderProductFormSet(instance=self.object)
#         return data
#
#     def form_valid(self, form):
#         context = self.get_context_data()
#         orderproducts = context['orderproducts']
#         with transaction.atomic():
#             self.object = form.save()
#
#             if orderproducts.is_valid():
#                 orderproducts.instance = self.object
#                 orderproducts.save()
#         return super(ProfileFamilyMemberUpdate, self).form_valid(form)
#
