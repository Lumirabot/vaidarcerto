def format_currency(amount):
    return f"${amount:,.2f}"

def format_message(user, action, amount):
    return f"{user} has {action} {format_currency(amount)}."

def check_positive_balance(balance):
    if balance < 0:
        raise ValueError("Balance cannot be negative.")
    return True

def get_user_mention(user_id):
    return f"<@{user_id}>"

def log_action(action):
    # Placeholder for logging actions
    print(f"Action logged: {action}")