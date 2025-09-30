Resumo do Projeto CRUD com Streamlit e MongoDB

Objetivo:
Criar um sistema para gerenciar clientes (Criar, Ler, Atualizar, Deletar) usando Streamlit para interface, MongoDB para banco de dados e Docker para rodar tudo de forma isolada.

Como funciona:

Criar: adiciona novos clientes.

Listar: exibe todos os clientes em tabela.

Atualizar: edita clientes existentes.

Deletar: remove clientes do banco.

Tecnologias:

Streamlit → interface web interativa.

MongoDB → banco NoSQL para armazenar dados.

Docker → containeriza a aplicação e o banco, garantindo portabilidade.

Execução:

Rodar docker-compose up --build.

Acessar no navegador: http://localhost:8501.

Interagir com o CRUD pelo menu lateral.

Vantagens:

Fácil de usar pelo navegador.

Dados persistentes via MongoDB.

Pode rodar em qualquer máquina com Docker.
