
## Projeto: Teste de Sistema - SauceDemo
Responsável pelos Testes: Raul Santos

Data: (29/12/2025)

**Objetivo:**  Simular testes Funcional Automatizado utilizando plataforma Gratuita SauceDemo

**Módulo:** Autenticação / Carrinho / Checkout

**Tipo de Teste:** Teste Funcional Automatizado

### Ambiente:
- **Navegador:** Chrome 
- **Linguagem:** Python  
- **Framework de Automação:** Selenium WebDriver  
- **Gerenciador de Dependências:** pip  
- **Ambiente Virtual:** venv  
- **Sistema Operacional:** Windows 10
- **URL:** https://www.saucedemo.com/

## Caso de Teste 01: 	TC-01
**Título:**	Adicionar Produtos ao Carrinho
- **Pré-condição:**	Usuário cadastrado no sistema, Produto "Sauce Labs Backpack" e "Sauce Labs Bolt T-Shirt"
- **Dados de Teste:**	Usuário válido e senha válida
### Passos	
  - **1.** Acessar a página principal da plataforma SauceDemo
  - **2.** preencher Caixa de texto Username com login válido (Oferecido pela propria plataforma)
  - **3.** Preencher caixa de texto Password com senha válida (Oferecida pela própria plataforma)
  - **4.** Clicar no Botão Login
  - **5.** Validar se o usuário foi redirecionado para a página principal da plataforma de vendas
  - **6.** CLicar no link para acessar a página do Produto 01 com Descrição "Sauce Labs Backpack"
  - **7.** CLicar no link para acessar o carrinho"
  - **8.** Validar se o produto está adicionado ao carrinho
  - **9.** "Voltar a página de compras usando o botão "Continue Shopping"
  - **6.** CLicar no link para acessar a página do Produto 02 com Descrição "Sauce Labs Bolt T-Shirt"
  - **7.** CLicar no link para acessar o carrinho"
  - **8.** Validar se o Produto 02 está adicionado ao carrinho"

Resultado Esperado: O usuário deve ter sucesso ao fazer login adicionar dois itens ao carrinho


## Caso de Teste 02: 	TC-02
**Título:**	Login com credenciais válidas
- **Pré-condição:**	Usuário cadastrado no sistema
- **Dados de Teste:**	Usuário válido e senha válida
### Passos	
  - **1.** Acessar a página principal da plataforma SauceDemo
  - **2.** preencher Caixa de texto Username com login válido (Oferecido pela propria plataforma)
  - **3.** Preencher caixa de texto Password com senha válida (Oferecida pela própria plataforma)
  - **4.** Clicar no Botão Login
  - **5.** Validar se o usuário foi redirecionado para a página principal da plataforma de vendas

Resultado Esperado: Usuário deve ser redirecionado para a página Products

## Caso de Teste 03: 	TC-03
**Título:**	Login com credenciais inválidas
- **Dados de Teste:**	Usuário i e senha inválido
### Passos	
  - **1.** Acessar a página principal da plataforma SauceDemo
  - **2.** preencher Caixa de texto Username com login válido (Oferecido pela propria plataforma)
  - **3.** Preencher caixa de texto Password com senha incorreta
  - **4.** Clicar no Botão Login
  - **5.** Validar mensagem de erro que aparecerá em PopUP na tela.

Resultado Esperado: O sistema rejeitará o pedido de login e exibirá um popUP vermelha com mensagem descrevendo o erro.


## Caso de Teste 04: 	TC-04
**Título:**	Adicionar Produtos ao Carrinho
- **Pré-condição:**	Usuário cadastrado no sistema, Produto "Sauce Labs Backpack" e "Sauce Labs Bolt T-Shirt"
- **Dados de Teste:**	Usuário válido e senha válida
### Passos	
  - **1.** Fazer todos os passos do Teste **TC-03**
  - **2.** Clicar no botão Checkout
  - **3.** Preencher formulário com Name, Lastname e Zipcode
  - **4.** Clicar no botão Finish
  - **5.** Validar se a mensagem de confirmação da compra foi exibida.


Resultado Esperado: O usuário deve ter sucesso ao inserir todos os itens ao carrinho, preencer com seus dados o formulário de Checkout e visualizar a lista de itens comprados na tela de pagamento.




