# Todo - Django Tenants

Esse é um projeto de estudos para aperfeiçoar os conhecimentos nos projetos de Saas Software as a Services.

Projeto com django utilizando ambiente isolados de dados usando schemas do postgres.

## Tecnologias

- <a href="https://www.python.org/">Python 3.10</a>
- <a href="https://www.djangoproject.com/">Django 4</a>
- Postgres Latest
- Django Tenants Latest


### Snapshots

> Observações no OSX foi realizado a alteração no arquivo private/etc/hosts para redirecionadas as rotas: adm.todo.local, cliente.todo.local, cliente2.todo.local para o local host.

*requisições em http://cliente.todo.local:8000/beforeidie e http://cliente2.todo.local:8000/beforeidie*
`- retorna as mesmas listagens já que esse models está em shared apps`

![](https://i.imgur.com/XDOetkk.png)

----
*requisição em http://cliente.todo.local:8000/*

`- retorna apenas os resultas da listagem do cliente 1`

![](https://i.imgur.com/e2suaMd.png)

----
*requisição em http://cliente.todo.local:8000/*
`- retorna apenas os resultados da listagem do cliente 2`

![](https://i.imgur.com/kAAXb7c.png)

------
*painel do admin nos 3 ambientes cliente1, cliente2 e global*
![](https://i.imgur.com/JHoDoOa.png)
![](https://i.imgur.com/tgrNtKP.png)
![](https://i.imgur.com/wOE8WqI.png)


*O banco de dados fica com 1 schema para **cada ambiente de usuário***

![](https://i.imgur.com/msMg0zl.png)

-----

### Upgrade para django rest framework usando isolamento de ambientes de clientes com dados exclusivos e compartilhados.

-------
*Resposta da api para http://cliente.todo.local:8000/api/beforeidie/ e http://cliente2.todo.local:8000/api/beforeidie/ com dados compartilhados*
![](https://i.imgur.com/HW7K8lk.png)

-------
*Resposta da api para http://cliente.todo.local:8000/api/mylist/ com dados exclusivo do cliente 1*
![](https://i.imgur.com/Q9W6CAC.png)


-------
*Resposta da api para http://cliente2.todo.local:8000/api/mylist/ com dados exclusivo do cliente 2*
![](https://i.imgur.com/uZNK1MJ.png)
