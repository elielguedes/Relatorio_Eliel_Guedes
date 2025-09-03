# Documentação da API Empresas FastAPI

## Sumário
- [Introdução](#introducao)
- [Instalação e Execução](#instalacao-e-execucao)
- [Importação de Dados](#importacao-de-dados)
- [Autenticação JWT](#autenticacao-jwt)
- [Endpoints](#endpoints)
- [Proteção de Rotas](#protecao-de-rotas)
- [Testes e Evidências](#testes-e-evidencias)
- [Diagrama ER](#diagrama-er)

---

## Introdução
API REST desenvolvida com FastAPI, SQLite e SQLAlchemy para cadastro e consulta de empresas, estabelecimentos e sócios. Possui autenticação JWT e importação de dados públicos via CSV.

## Instalação e Execução
1. Clone o repositório
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute a API:
   ```bash
   uvicorn app.main:app --reload
   ```

## Importação de Dados
Execute o script para importar empresas:
```bash
python -m app.scripts.import_empresas
```

## Autenticação JWT
- Registre um usuário em `/auth/register`
- Faça login em `/auth/login` para obter o token JWT
- Use o token para acessar rotas protegidas

## Endpoints
### Empresas
- `GET /empresas` - Lista empresas
- `POST /empresas` - Cria empresa
- `GET /empresas/{id}` - Consulta empresa
- `DELETE /empresas/{id}` - Deleta empresa (admin)

### Estabelecimentos
- `GET /estabelecimentos` - Lista estabelecimentos
- `POST /estabelecimentos` - Cria estabelecimento
- `GET /estabelecimentos/{id}` - Consulta estabelecimento
- `DELETE /estabelecimentos/{id}` - Deleta estabelecimento (admin)

### Sócios
- `GET /socios` - Lista sócios
- `POST /socios` - Cria sócio
- `GET /socios/{id}` - Consulta sócio
- `DELETE /socios/{id}` - Deleta sócio (admin)

### Autenticação
- `POST /auth/register` - Registro de usuário
- `POST /auth/login` - Login JWT
- `GET /auth/me` - Dados do usuário autenticado

## Proteção de Rotas
- Apenas usuários autenticados podem acessar rotas protegidas
- Apenas admin pode deletar empresas, estabelecimentos e sócios

## Testes e Evidências
- Utilize o Swagger em `http://localhost:8000/docs`
- Coleção Postman disponível em `fastapi-projeto/postman_collection.json`
- Prints do Swagger, terminal e exemplos de requisições estão descritos no README

## Diagrama ER
- ![Diagrama ER](diagrama_er.png)
- Visualize e baixe o diagrama em: [QuickDBD - Diagrama ER](https://quickdatabasediagrams.com/#/d/7QvK7g)

---

**Dúvidas ou problemas? Consulte o README ou entre em contato com o desenvolvedor.**
