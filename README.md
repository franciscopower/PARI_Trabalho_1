# PARI - Trabalho 1
## *Typing test*
Teste de escrita com limite de número de letras a testar ou limite de tempo.

### *Instruções:*

Para correr o programa na linha de comandos:

```py
./main.py [-h] [-utm] [-mv MAX_VALUE]
```
O programa deve receber argumentos de entrada que definem o modo de finalização do teste (tempo máximo ou número de inputs máximo).
O argumento `[-h] [--help]` apresenta um texto de explicação dos outros argumentos. 
Se for usado o argumento `[-utm] [--user_time_mode]` o programa corre no modeo de tempo máximo. Caso contrário, corre no modo de inputs máximos.
O argumento `[-mv] [--max_value]` é obrigatório e requer um número inteiro que define o número de inputs máximo ou tempo máximo, dependendo do modo escolhido.

O teste inicia após o utilizador pressionar uma tecla (pedido feito pelo programa). Aparece uma letra minúscula no programa (gerada aleatoriamente) e aguarda o input do utilizador (basta clicar no carater do teclado).

O desafio tem dois modos diferentes: tempo máximo ou número de inputs máximo. O teste pára se:

+ No modo de tempo máximo: o tempo de teste decorrido for maior do que o tempo que o utilizador definiu;

+ No modo de inputs máximo: quando o número de inputs dado pelo utilizador atingir o número definido;

+ Pressionar a tecla "espaço", o teste é interrompido nos dois modos e aparece uma mensagem de interrupção;

Durante o teste e após cada input do utilizador, o programa imprime uma mensagem indicando se a tecla pressionada foi ou não correta.

No final aparece no ecrã as estatísticas do desafio:

+ Pontuação; 

+ Inputs e a sua duração;

+ Número de sucessos;

+ Numero de inputs;

+ Data de inicio e fim de teste;

+ Duração média das respostas do utilizador;

+ Duração média das respostas corretas e incorretas do utilizador;

**Boa Sorte!**

Trabalho prático da unidade curricular de Projeto de Automação e Robótica Industrial, Mestrado Integrado em Engenharia Mecânica, Universidade de Aveiro

Francisco Power,Miguel Carvalhais e Rita Correia
