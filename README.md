# Sistema de Monitoramento de Robô Trader 📈🤖

Este projeto consiste em um sistema web desenvolvido com **Django**, focado na automação e visualização de estratégias de trading. O sistema organiza tipos de mercado (Categorias) e robôs específicos (Produtos), aplicando os padrões de arquitetura exigidos.

## 🛠️ Tecnologias e Padrões
* **Django & Django REST Framework**: Framework principal e extensão para API.
* **Padrão FrontController**: Centralização de rotas no `urls.py`.
* **Padrão MVT**: Organização em Modelos, Visões e Templates.

## 📂 Estrutura do Projeto
- `core/models.py`: Modelagem de Categorias e Robôs.
- `core/views.py`: Lógica de renderização das páginas e endpoints.
- `core/templates/`: Interface do usuário (Index, Problema, Solução, Autor).

## 🧠 O Problema e a Solução
O mercado financeiro opera 24/7. O monitoramento manual gera falhas por cansaço e latência. Nossa solução utiliza robôs algoritmos que operam sem viés emocional, garantindo execução precisa e constante.

## 🚀 Como Executar
1. Instale o Django: `pip install django djangorestframework`
2. Execute as migrações: `py manage.py migrate`
3. Inicie o servidor: `py manage.py runserver`
