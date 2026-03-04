
Projeto Final: API REST com Django Framework 🚀
Este projeto consiste na implementação de uma API RESTful utilizando Django e Django REST Framework (DRF),
desenvolvida como parte da avaliação final. O objetivo foi criar um sistema de backend capaz de gerenciar categorias
e produtos através de endpoints JSON.

📋 Funcionalidades
Gestão de Categorias: Listagem e cadastro de categorias.

Gestão de Produtos: Listagem e cadastro de produtos com relacionamento de chave estrangeira.

Interface Navegável: Uso da Browsable API do DRF para testes rápidos.

Versionamento: Controle de versão total via Git com uso de branches.

🛠️ Tecnologias Utilizadas
Python 3.14: Linguagem base.

Django 6.0.2: Framework web principal.

Django REST Framework 3.16.1: Extensão para criação da API.

SQLite: Banco de dados padrão para desenvolvimento.

Git/GitHub: Controle de versão e deploy do código.

📝 Passo a Passo da Implementação
1. Preparação do Ambiente
Criação da branch de desenvolvimento: git checkout -b rest.

Instalação do framework: py -m pip install djangorestframework.

Configuração em settings.py adicionando rest_framework aos INSTALLED_APPS.

2. Modelagem de Dados (models.py)
Criação da classe Categoria (nome).

Criação da classe Produto (nome, preço e vínculo com Categoria).

Execução de py manage.py makemigrations e py manage.py migrate.

3. Serialização e Visualização (serializers.py e views.py)
Implementação de ModelSerializer para converter modelos em JSON.

Uso de viewsets.ModelViewSet para criar automaticamente a lógica de CRUD (Criar, Ler, Atualizar, Deletar).

4. Roteamento (urls.py)
Uso do DefaultRouter para mapear os caminhos /api/categorias/ e /api/produtos/.

🧠 Desafios Superados (Relato Técnico)
Durante o desenvolvimento, enfrentei e resolvi os seguintes obstáculos:

Estrutura de Módulos: Ajuste da localização do arquivo serializers.py para dentro da pasta da aplicação (core), garantindo que o Django localizasse as classes corretamente.

Conflitos de Branch: O Git local não reconhecia a branch master inicialmente. A solução foi criar a branch principal com git checkout -b master e realizar o merge manual da branch rest.

Configuração Remota: Erro de conexão com o repositório origin. Resolvido configurando o link remoto via git remote add origin para permitir o push final.

Comandos de Ambiente: Adaptação do uso de python para py no terminal Windows/PowerShell para execução dos scripts de gerenciamento.

🚀 Como Rodar o Projeto
Clone o repositório.

Instale as dependências: pip install django djangorestframework.

Inicie o servidor: py manage.py runserver.

Acesse: http://127.0.0.1:8000/api/.

✅ Checklist de Entrega (Prints no PDF)
[ ] Print do terminal: git branch mostrando a branch rest.

[ ] Print do terminal: Sucesso nos comandos makemigrations e migrate.

[ ] Print do Navegador: Página Raiz da API funcionando.

[ ] Print do Navegador: Cadastro de um produto (POST 201 Created).
