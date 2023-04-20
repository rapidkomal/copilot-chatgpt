#install stripe
#pip install stripe
import stripe
from stripe.api_resources.payment_intent import PaymentIntent

STRIPE_PUBLIC_KEY='pk_test_51MtsqOSJDcfPOfrVtZItVFkrrino5kiki8sc3TvylEwxHHiJzPte3FXIhjWJ70ANLDq8sZDZCvWTcygT4r1zAVM700iqeTrVDr'
STRIPE_SECRET_KEY='sk_test_51MtsqOSJDcfPOfrVpyzSN6mLC9I408UP1KimKC8kFIdzLvgI42lqw6Qj7QCGQmRa91kw93s9Af0hZHkXSYbK9W2700Koco54aN'
# Api_key=    'sk_test_51J9Z4 ...'
stripe.api_key = STRIPE_SECRET_KEY
# create function for stripe payment
def stripe_payment():
    # create object of stripe class
    payment = stripe.PaymentIntent.create(
        amount=1000,
        currency='inr',
        payment_method_types=['card'],
        receipt_email='test',
    )
    return f'{payment} : payment done'
stripe_payment()
# create function for stripe payment with payment method id
def stripe_payment_with_payment_method_id():
    # create object of stripe class
    payment = stripe.PaymentIntent.create(
        amount=1000,
        currency='inr',
        payment_method_types=['card'],
        receipt_email='test',
        payment_method='test',
    )
    return f'{payment} : payment done'
stripe_payment_with_payment_method_id()

#AttributeError: partially initialized module 'stripe' has no attribute 'PaymentIntent' (most likely due to a circular import)
# import stripe
# STRIPE_PUBLIC_KEY='pk_test_51MtsqOSJDcfPOfrVtZItVFkrrino5kiki8sc3TvylEwxHHiJzPte3FXIhjWJ70ANLDq8sZDZCvWTcygT4r1zAVM700iqeTrVDr'

