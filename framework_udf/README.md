# API Empresas - FastAPI

## Descrição
API REST para cadastro e consulta de empresas, estabelecimentos e sócios, com autenticação JWT e importação de dados públicos.

## Instalação
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

## Autenticação
- Registre um usuário em `/auth/register`
- Faça login em `/auth/login` para obter o token JWT
- Use o token para acessar rotas protegidas

## Endpoints Principais
- `/empresas` CRUD de empresas
- `/estabelecimentos` CRUD de estabelecimentos
- `/socios` CRUD de sócios
- `/auth/register` Registro de usuário
- `/auth/login` Login JWT
- `/auth/me` Dados do usuário autenticado

## Testes
Utilize o Swagger em `http://localhost:8000/docs` ou importe a coleção Postman (ver pasta `fastapi-projeto/` se existir)

## Diagrama ER
![Diagrama ER](fastapi-projeto/diagrama_er.png)

Visualize e baixe o diagrama em: [QuickDBD - Diagrama ER](https://quickdatabasediagrams.com/#/d/7QvK7g)

## Evidências

### Prints do Swagger
Inclua capturas de tela da interface Swagger (`/docs`) mostrando os endpoints e exemplos de resposta.

### Comandos utilizados
```bash
uvicorn app.main:app --reload
python -m app.scripts.import_empresas
```

### Exemplo de requisições
**Registro de usuário (admin):**
```json
POST /auth/register
{
   "username": "admin",
   "password": "123456",
   "is_admin": true
}
```

**Login:**
```json
POST /auth/login
{
   "username": "admin",
   "password": "123456"
}
```

**Criar empresa:**
```json
POST /empresas
{
   "nome": "Nova Empresa"
}
```

**Deletar empresa (admin):**
```http
DELETE /empresas/{id}
Authorization: Bearer <token>
```

### Logs de execução
Inclua prints do terminal mostrando a execução dos comandos acima e respostas da API.
