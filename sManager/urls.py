
from django.urls import path, include
from . import views

app_name = 'sManager'

urlpatterns = [
    path('', views.homePage, name='home-page'),
    path('supply/create/', views.CreateSupplyView.as_view(), name='create-supply'),
    path('supply/edit/<int:pk>', views.EditSupplyView.as_view(), name='edit-supply'),
    path('supply/delete/<int:pk>', views.DeleteSupplyView.as_view(), name='delete-supply'),
    path('total_sum/confirmed=<int:confirmed>/date=<str:date>/extra=<int:extra>',
         views.productSumCalculation),
    path('suppliers/', views.SuppliersListView.as_view(), name='suppliers'),
    path('suppliers/create/', views.CreateSupplierView.as_view(),
         name='supplier-create'),
    path('suppliers/edit/<int:pk>', views.EditSupplierView.as_view(),
         name='supplier-edit'),
    path('suppliers/delete/<int:pk>', views.DeleteSupplierView.as_view(),
         name='supplier-delete'),
    path('history/', views.HistoryGeneralView.as_view(), name='history'),
    path('history/<str:date>', views.historySearch, name='history-search'),
    path('history/view/<int:pk>',
         views.HistorySpecificView.as_view(), name='history-view'),
     path('delete-profile-photo/<int:id>', views.deleteProfilePhoto, name="delete-profile-photo"),
     path('finance/', views.FinancePageView.as_view(),name="finance" ),
     path('debt/', views.DebtView.as_view(),name="debt" ),
     path('clients-list', views.ClientsListView.as_view(),name="clients-list" ),
     # path('clients-list/client/<int:id>', views.process_array,name="clientData" ),
      path('clients-list/client/edit/<int:id>/', views.ClientEditView.as_view(), name='client-edit'),
      path('clients-list/client/delete/<int:pk>/', views.ClientDeleteView.as_view(), name='client-delete'),
     path('clients-list/debt/edit/<int:pk>', views.DebtEditView.as_view(),name="debt-edit" ),
     path('clients-list/debt/delete/<int:pk>', views.DebtDeleteView.as_view(),name="debt-delete" ),
     path('clients-list/debt/add-from-client', views.debtAdd,name="debt-add-from-client" ),
     path('money/add', views.moneyAdd, name='money-add'),
     path('money/edit/<int:pk>', views.MoneyEditView.as_view(), name='money-edit'),
     path('money/delete/<int:pk>', views.MoneyDeleteView.as_view(), name='money-delete'),
     

]
