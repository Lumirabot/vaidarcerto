def work(user):
    import random
    from src.utils.db import update_user_balance

    # Simula o trabalho e ganha entre 10 a 50 "star coins"
    earnings = random.randint(10, 50)
    
    # Atualiza o saldo do usuário no banco de dados
    update_user_balance(user.id, earnings)
    
    return f"{user.name}, você trabalhou e ganhou {earnings} star coins!"