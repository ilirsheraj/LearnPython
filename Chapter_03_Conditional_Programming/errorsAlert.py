# define a function send_email to be used in the code
def send_email(*email):
    print(*email)

# change console with email
# alert_system = "console"
alert_system = "email"

# error severity can also be 'low', 'medium' or 'critical'
error_severity = "critical"
error_message = "OMG! Something terrible just happened"

if alert_system == "console":
    print(error_message)

elif alert_system == "email":

    if error_severity == "critical":
        send_email("admin@example.com", error_message)
    elif error_severity == "medium":
        send_email("support.1@example.com", error_message)
    else:
        send_email("support.2@example.com", error_message)

else:
    print("There is nothing i can do!")
