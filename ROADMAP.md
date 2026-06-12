# 🚀 Projeto SaaS - Distribuidora Fácil

## Objetivo Geral

Criar um sistema SaaS para pequenas distribuidoras de bebidas com:

* Controle de estoque
* Cadastro de clientes
* Registro de vendas
* Controle de fiado
* Dashboard gerencial
* Login de usuários
* Multiempresa
* Recursos de IA

---

# FASE 0 - Preparação do Ambiente

## Estrutura Inicial

* [x] Criar pasta do projeto
* [x] Abrir projeto no VS Code
* [x] Criar estrutura principal:

  * [x] backend/
  * [x] frontend/
  * [x] docs/

---

## Backend

* [x] Criar ambiente virtual (venv)
* [x] Ativar ambiente virtual
* [x] Instalar FastAPI
* [x] Instalar SQLAlchemy
* [x] Instalar PostgreSQL
* [x] Instalar JWT
* [x] Instalar bibliotecas auxiliares
* [x] Gerar requirements.txt
* [x] Criar primeira API
* [x] Validar Swagger (/docs)

---

## Frontend

* [x] Instalar Node.js
* [x] Criar projeto React com Vite
* [x] Instalar Material UI
* [x] Instalar Axios
* [x] Instalar React Router
* [x] Validar execução do frontend

---

# FASE 0.5 - Base Profissional

## Documentação

* [x] Criar README.md
* [x] Criar ROADMAP.md
* [x] Criar docs/arquitetura.md
* [x] Criar docs/banco_dados.md
* [x] Criar docs/api_endpoints.md

---

## Configuração

* [x] Criar .gitignore
* [x] Criar .env.example
* [x] Configurar variáveis de ambiente

---

## Git e GitHub

* [x] Inicializar Git
* [x] Criar repositório GitHub
* [x] Vincular repositório remoto
* [x] Realizar primeiro commit
* [x] Realizar primeiro push
* [x] Validar .gitignore

---

## Estrutura Profissional

* [x] Validar organização backend/frontend/docs
* [x] Validar README
* [x] Validar documentação inicial

---

## Meta da Fase

* [x] Projeto estruturado profissionalmente
* [x] Versionamento funcionando
* [x] Documentação criada
* [x] Repositório online

---

# FASE 1 - Autenticação

## Banco de Dados

* [x] Configurar conexão PostgreSQL
* [x] Configurar SQLAlchemy
* [x] Criar Session Local
* [x] Criar Base Declarativa
* [x] Testar conexão com banco
* [x] Criar tabela empresas
* [x] Criar tabela usuarios
* [x] Criar relacionamento empresa → usuarios
* [x] Instalar Alembic
* [x] Inicializar Alembic
* [x] Configurar Alembic
* [x] Criar primeira migration
* [x] Executar migration
* [x] Validar tabelas no PostgreSQL

## Backend

* [x] Criar schemas Pydantic
* [x] Criar dependência get_db
* [x] Endpoint de cadastro
* [x] Criptografia de senha
* [x] Testar cadastro via Swagger
* [x] Criar schema de resposta da empresa
* [x] Criar schema de resposta do usuário
* [x] Salvar senha criptografada
* [x] Criar utilitário JWT
* [x] Gerar Access Token
* [x] Criar schema Login
* [x] Criar endpoint /auth/login
* [x] Validar email e senha
* [x] Retornar token JWT
* [x] Testar login via Swagger
* [x] Buscar usuário autenticado no banco
* [x] Retornar dados completos do usuário
* [x] Testar endpoint /auth/me
* [x] Instalar python-dotenv
* [x] Criar SECRET_KEY no .env
* [x] Ler variáveis de ambiente
* [x] Remover SECRET_KEY hardcoded
* [x] Testar autenticação usando .env

## Frontend

* [ ] Tela Login
* [ ] Tela Cadastro
* [ ] Salvar token
* [ ] Rotas protegidas
* [ ] Logout

## Meta da Fase

* [ ] Usuário consegue criar conta
* [ ] Usuário consegue fazer login
* [ ] Usuário acessa dashboard protegido

---

# FASE 2 - Produtos e Estoque

## Banco

* [ ] Criar tabela produtos
* [ ] Criar relacionamento empresa → produtos

## Backend

* [ ] Criar produto
* [ ] Editar produto
* [ ] Excluir produto
* [ ] Listar produtos

## Frontend

* [ ] Tela Produtos
* [ ] Formulário de cadastro
* [ ] Tabela de produtos
* [ ] Busca de produtos

## Meta da Fase

* [ ] Estoque funcional

---

# FASE 3 - Clientes

* [ ] Criar tabela clientes
* [ ] Criar CRUD de clientes
* [ ] Criar tela de clientes
* [ ] Cadastro completo de clientes

---

# FASE 4 - Vendas

* [ ] Criar tabela vendas
* [ ] Criar tabela itens_venda
* [ ] Registrar venda
* [ ] Baixa automática de estoque
* [ ] Tela de vendas
* [ ] Venda reduz estoque automaticamente

---

# FASE 5 - Dashboard

* [ ] Faturamento do dia
* [ ] Quantidade de vendas
* [ ] Estoque baixo
* [ ] Clientes cadastrados
* [ ] Vendas por dia
* [ ] Produtos mais vendidos
* [ ] Faturamento mensal

---

# FASE 6 - Controle de Fiado

* [ ] Criar tabela contas_receber
* [ ] Registrar dívida
* [ ] Registrar pagamento
* [ ] Atualizar status
* [ ] Tela contas a receber

---

# FASE 7 - Multiempresa

* [ ] Isolar dados por empresa
* [ ] Validar permissões
* [ ] Testar acesso cruzado

---

# FASE 8 - Inteligência Artificial

* [ ] Previsão de reposição de estoque
* [ ] Produtos mais lucrativos
* [ ] Tendência de vendas
* [ ] Alertas automáticos

---

# FASE 9 - Comercialização

* [ ] Configurar VPS
* [ ] Configurar domínio
* [ ] Configurar HTTPS
* [ ] Criar landing page
* [ ] Criar vídeo demonstrativo
* [ ] Captar primeiros clientes

---

# MARCOS TÉCNICOS

* [x] Ambiente configurado
* [x] Projeto versionado no GitHub
* [x] Banco de dados estruturado
* [x] Cadastro funcionando
* [x] Login JWT funcionando
* [x] Primeira rota protegida funcionando
* [ ] Frontend integrado ao backend

---

# MARCOS IMPORTANTES (MVPs)

* [ ] MVP 1 - Login funcionando
* [ ] MVP 2 - Estoque funcionando
* [ ] MVP 3 - Vendas funcionando
* [ ] MVP 4 - Dashboard funcionando
* [ ] MVP 5 - Primeiro cliente usando
* [ ] MVP 6 - Primeiro cliente pagante

---

# VISÃO FINAL

* [ ] Login
* [ ] Multiempresa
* [ ] Estoque
* [ ] Clientes
* [ ] Vendas
* [ ] Fiado
* [ ] Dashboard
* [ ] IA
* [ ] Clientes pagantes
