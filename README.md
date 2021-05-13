# MercaFacil-challenge
Desafio para a MercaFacil


## Como testar
Faça a build do docker com:
```shell
docker-compose up --build -d
```

Na primeira execução, pode acontecer um erro com a conexão no banco de dados, por conta do tempo não consegui resolver este problema, mas para resolver basta reiniciar o container web:

```shell
docker-compose restart web
```

Para acessar os logs da aplicação execute:
```shell
docker-compose logs -f web
```

Para criar os usários da aplicação execute:
```shell
docker-compose exec web bash
```
Após isso acesse o shell python e execute o conteudo de create_users.py

