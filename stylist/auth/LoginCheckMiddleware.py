from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect
class LoginCheckMiddleware(MiddlewareMixin):

    def process_view(self,request,view_func,view_args,view_kwargs):
        modulename = view_func.__module__
        user = request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename ==  "index.AdminViews":
                    pass
                elif modulename == "index.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("admin_home"))
            elif user.user_type == "2":
                if modulename ==  "index.ClientViews":
                    pass
                elif modulename == "index.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("client_home"))
            elif user.user_type == "3":
                if modulename ==  "index.StylistViews":
                    pass
                elif modulename == "index.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("stylist_home"))
            else:
                return HttpResponseRedirect(reverse("show_login"))
        else:
            if request.path == reverse("show_login") or request.path == reverse("do_login"):
                pass
            else:
                return HttpResponseRedirect(reverse("show_login"))