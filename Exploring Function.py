#Function Practice

# def mobile_price_bdt(usd_price, exchange_rate):
#     bd_price = usd_price * exchange_rate
#     return bd_price
# Xiaomi_Mobile_Price = mobile_price_bdt(320, 105)
# print(Xiaomi_Mobile_Price)


# def greetings(name):
#     #print("Hellow", name)
#     return f"Hellow {name}"
#
# one_greetings = greetings("23")
# print(one_greetings)

def voter_check(age):
    if age >= 18:
        return "You are a Voter"
    else:
        return "You are not Eligible"
print(voter_check(8))