# Orientação a Objetos Python - Exercicios (parte 1)
---

## Instruções

* Separe cada exercício em uma pasta separada (exemplo: "exercicio-0").
* Cada classe deverá estar um arquivo com o mesmo nome (exemplo: classe Pessoa no arquivo pessoa.py)
* Para cada exercício, crie um arquivo principal (main.py) que irá importar as classes que são utilizadas
* O arquivo main.py será o único que irá receber dados de entrada do usuário (input) e imprimir dados de saída (print), chamando as classes para executar as operações quando lhe for conveniente.

## Exercícios:

0. Crie uma classe Pessoa que modele uma pessoa contendo: 
- Atributos: nome, idade, peso e altura 
- Métodos: Envelhecer, engordar, emagrecer, crescer. 
- Adicionais:
  - Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
  - Pode possuir ou não parâmetros
  
1. Crie uma classe para representar um jogador de futebol, com os atributos nome, posição, data de nascimento, nacionalidade, altura e peso. Crie os métodos públicos necessários para sets e gets e também um método para imprimir todos os dados do jogador. Crie um método para calcular a idade do jogador e outro método para mostrar quanto tempo falta para o jogador se aposentar. Para isso, considere que os jogadores da posição de defesa se aposentam em média aos 40 anos, os jogadores de meio-campo aos 38 e os atacantes aos 35.

2. Crie uma classe chamada ContaBancaria, que deverá conter os atributos numero, agencia, saldo tipo (codigo e nome do tipo - "01" = corrente e "02" = poupança); além disso, implemente os métodos validar_tipo_conta (utilizada no construtor), mostrar_saldo, depositar e sacar. Depois, crie uma classe ContaImposto que herda de conta e possui um atributo percentualImposto. Esta classe também deve possuir um método calcularImposto() que subtrai do saldo, o valor do próprio saldo multiplicado pelo percentual do imposto. Crie um programa para criar as instâncias de ContaImposto e utilizar todos os métodos das 3 classes (ex.: sacar, depositar, calcularImposto).

3. Crie uma classe chamada Ingresso, que possui um valor em reais e um método imprimirValor(). Crie uma classe IngressoVIP, que herda de Ingresso e possui um valor adicional. Crie um método que retorne o valor do ingresso VIP (com o adicional incluído). Crie um programa para criar as instâncias de Ingresso e IngressoVIP, mostrando a diferença de preços.

4. Crie uma classe Elevador para armazenar as informações de um elevador de prédio. A classe deve armazenar o andar atual (térreo = 0), total de andares no prédio (desconsiderando o térreo), capacidade do elevador e quantas pessoas estão presentes nele. A classe deve também disponibilizar os seguintes métodos:
  * **Inicializar:** que deve receber como parâmetros a capacidade do elevador e o total de andares no prédio (os elevadores sempre começam no térreo e vazio);
  * **Entrar:** para acrescentar uma pessoa no elevador (só deve acrescentar se ainda houver espaço);
  * **Sair:** para remover uma pessoa do elevador (só deve remover se houver alguém dentro dele);
  * **Subir:** para subir um andar (não deve subir se já estiver no último andar);
  * **Descer:** para descer um andar (não deve descer se já estiver no térreo);
  - Obs.: Encapsular todos os atributos da classe (criar os métodos set e get).
  
**5. Crie uma classe chamada Fatura que possa ser utilizado por uma loja de suprimentos de informática para representar uma fatura de um item vendido na loja. Uma fatura deve incluir as seguintes informações como atributos:**
  * o número do item faturado,
  * a descrição do item,
  * a quantidade comprada do item e
  * o preço unitário do item.

  Sua classe deve ter um construtor que inicialize os quatro atributos. Se a quantidade não for positiva, ela deve ser configurada como 0. Se o preço por item não for positivo ele deve ser configurado como 0.0. Forneça os métodos get/set para cada variável de instância. Além disso, forneça um método chamado calcular_valor_fatura que calcula o valor da fatura (isso é, multiplica a quantidade pelo preço por item) e depois retorna o valor. Escreva também um programa de teste (main) que demonstra as capacidades da classe Fatura.

**6. A fim de representar empregados em uma empresa, crie uma classe chamada Empregado que inclui as três informações a seguir como atributos:**
  * um primeiro nome,
  * um sobrenome, e
  * um salário mensal.

  Sua classe deve ter um construtor que inicializa os três atributos. Forneça os métodos método get/set para cada atributo. Se o salário mensal não for positivo, configure-o como 0.0. Escreva um aplicativo de teste que demonstra as capacidades da classe. Crie duas instâncias da classe e exiba o salário anual de cada instância (soma dos salários mensais). Então dê a cada empregado um aumento de 10% e exiba novamente o salário anual de cada empregado.

**7. Crie uma classe para representar datas. Represente uma data usando três atributos: o dia, o mês, e o ano.**
  * Sua classe deve ter um construtor que inicializa os três atributos e verifica a validade dos valores fornecidos.
  * Caso as datas não sejam passadas no construtor (devem ser parâmetros opcionais), inicialize a data com a data atual fornecida pelo sistema operacional.
  * Forneça os métodos get/set para cada atributo.
  * Forneça o método \__str__ para retornar uma representação da data como string. Considere que a data deve ser formatada mostrando o dia, o mês e o ano separados por barra (/).
  * Forneça uma operação para avançar uma data para o dia seguinte.
  * Escreva um programa de teste que demonstra as capacidades da classe.


**8. Crie uma classe abstrata chamada CartaoMensagem. Essa classe representa todos os tipos de cartões de mensagem contendo apenas um atributo: destinatario. Nessa classe você deverá também declarar o método retornarMensagem(remetente).**
  * Crie três classes filhas (sub-classes) da classe CartaoMensagem:
      1. MensagemDiaDosNamorados
      2. MensagemNatal
      3. MensagemAniversario.
  * Cada uma dessas classes deve conter um método construtor que receba o nome do destinatário do cartão. Cada classe também deve implementar o método retornarMensagem(remetente), retornando uma mensagem ao usuário com o nome do destinatário, um texto que seja específico para a data de comemorativa do cartão, acrescido do remetente ao final da mensagem. Por exemplo, essa poderia ser uma mensagem de um cartão de dia dos namorados:
    “Querida Maria,
    Feliz Dia dos Namorados!
    Espero que esse tenha gostado do meu cartão de dia dos namorados! De todo meu coração, João”
  * Crie um programa para demonstrar o uso das classes criadas. Para isso, crie um array (ex.: listaMsg = []) e insira de forma alternada instâncias dos 3 tipos de cartões (ex.: listaMsg.append(cartao)). Em seguida, use um laço de repetição (ex.: for msg in listMsg:) para exibir as mensagens dos cartões. Chame o método mostrarMensagem(String remetente) dos objetos, utilizando como argumento o seu nome para remetente. Utilize o método input para receber dados do usuário.
