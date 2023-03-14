

from django.shortcuts import render, redirect

from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View

class Signup(View):

    def get(self, req):    
            return render(req, 'signup.html')

    def post(self, req):
        postdate = req.POST
        name = postdate.get('first_name')
        last = postdate.get('last_name')    
        phone = postdate.get('phone_number')
        email = postdate.get('email')
        password = postdate.get("password")

        value ={
            "first_name": name,
            "last_name": last,
            "phone": phone,
            "email":  email
        }

        error_msg = None

        customer = Customer(first_name= name,
                                    last_name=last,
                                    phone=phone,
                                    password=password,
                                    email= email
                                    )

        error_msg = self.validation(customer)

        if (not error_msg): 
            customer.password = make_password(customer.password)
            customer.register()
            req.session['customer'] = customer.id
            return redirect("homepage")
        else:
            data={
                'error': error_msg,
                'value': value
            }
            return render (req, 'signup.html', data)
        

    def validation(self, customer):
        error_msg = None
        if (not customer.first_name):
            error_msg = "First Name Required!"
        elif(len(customer.first_name))< 4:
            error_msg = "First Name must be 4 char long or more"
        elif not customer.last_name:
            error_msg = "Last Name Required"
        elif len(customer.last_name) < 4:
            error_msg = 'Last Name must be 4 char long or more'
        elif not customer.phone:
            error_msg ="Phone number Required"
        elif len(customer.phone) < 10:
            error_msg ="Phone number must be 10 char long or more"  
        elif len(customer.email) < 5:
            error_msg ="Email must be 5 char long"        
        elif(len(customer.password)) < 6:
            error_msg="Password must be 6 char long" 
        elif customer.isExit():
            error_msg ="email already exites"
        return error_msg    


