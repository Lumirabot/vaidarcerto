# Star Bot - Discord Economy Bot

Star é um bot do Discord que implementa um sistema de economia simples, permitindo que os usuários ganhem e gerenciem "star coins" através de várias atividades. Este projeto é uma ótima maneira de aprender sobre a construção de bots para Discord e gerenciamento de dados.

## Funcionalidades

- **Trabalhar**: Os usuários podem trabalhar para ganhar "star coins".
- **Estudar**: Os usuários podem estudar para aumentar seus ganhos.
- **Transferir**: Os usuários podem transferir "star coins" entre si.
- **Ranking**: Visualize a classificação dos usuários com base na quantidade de "star coins".
- **Daily**: Reivindique uma quantia diária de "star coins".
- **Roubar**: Os usuários podem tentar roubar "star coins" de outros usuários.
- **Pescar**: Os usuários podem pescar para ganhar "star coins".

## Estrutura do Projeto

```
star-bot
├── src
│   ├── bot.py
│   ├── cogs
│   │   ├── economy
│   │   │   ├── work.py
│   │   │   ├── study.py
│   │   │   ├── transfer.py
│   │   │   ├── daily.py
│   │   │   ├── rob.py
│   │   │   └── fish.py
│   │   └── misc
│   │       └── ranking.py
│   ├── utils
│   │   ├── db.py
│   │   └── helpers.py
│   └── models
│       └── user.py
├── data
│   └── schema.sql
├── tests
│   └── test_economy.py
├── requirements.txt
├── pyproject.toml
├── .env.example
├── .gitignore
└── README.md
```

## Instalação

1. Clone o repositório:
   ```
   git clone <URL_DO_REPOSITORIO>
   cd star-bot
   ```

2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

3. Configure o arquivo `.env` com seu token do Discord.

## Uso

Para iniciar o bot, execute o seguinte comando:
```
python src/bot.py
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou relatar problemas.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.