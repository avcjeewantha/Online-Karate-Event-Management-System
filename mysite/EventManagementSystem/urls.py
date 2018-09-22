from django.conf.urls import url, include
from views import genericUser, slkf, district, province, association

urlpatterns = [
    url(r'^$', genericUser.index, name='index'),
    # url(r'^login$', views.login, name='login')

    # User auth urls

    url(r'^accounts', include('django.contrib.auth.urls')),

    url(r'^accounts/signup$', slkf.SignUpDirectingView.as_view(), name='signup'),
    # This directs to a html page with buttons to choose which type of user to create.

    url(r'^accounts/signup/association$', association.AssociationSignUpView.as_view(), name='association_signup'),
    url(r'^accounts/signup/district$', district.DistrictSignUpView.as_view(), name='district_signup'),
    url(r'^accounts/signup/province', province.ProvinceSignUpView.as_view(), name='province_signup'),

    url(r'^accounts/signup/signup-success$', genericUser.signupSuccess, name='signup-success'),

    # Login urls.
    url(r'^accounts/login$', genericUser.customLogin, name='login'),
    url(r'^accounts/auth$', genericUser.userAuth, name='auth'),
    url(r'^accounts/loggedin$', genericUser.loggedin, name='loggedin'),
    url(r'^accounts/logout$', genericUser.logout, name='logout'),
    url(r'^accounts/invalid$', genericUser.invalidLogin, name='invalid'),

    # User creation can only be done by the SLKF and super admin.
    # url(r'^create-user', views.signupUser, name='signup'),
    # url(r'^signed-up$', views.signupSuccess, name='signedup'),

    url(r'^slkf-portal', slkf.slkfPortal.as_view(), name='slkf-portal'),

    # Create new SLKF user
    url(r'^accounts/signup/slkf$', slkf.SlkfSignUpView.as_view(), name='slkf_signup'),

]
