/*
Calculadora Simples (Operações Básica)
Desenvolvida utilizando o paradigma de Programação Orientada a Objetos (POO)
*/

#include <iostream>
#include <locale>

using namespace std;

class Calculadora{
public:
    double resultado = 0;
    
    //Função para somar 
    void somar(double valor) {
        resultado += valor; //Soma e atribui o valor de 'valor'
    }

    //Função para subtrair 
    void subtracao(double valor){
        resultado -= valor; //Subtrai e atribui o valor de 'valor'
    }

    //Função para multiplicar 
    void multiplicacao(double valor){
        resultado *= valor; //Multiplica e atribui o valor de 'valor'
    }

    //Função para dividir 
    void divisao(double valor){
        resultado /= valor; //Divide e atribui o valor de 'valor'
    }

    //Função para exibir o resultado
    void exibir(){
        cout << "O resultado atual é: " << resultado << endl;
    } 
};

int main() {
    setlocale(LC_ALL, "Portuguese"); //Configura o programa para português

    Calculadora c; //Instancia (cria) o objeto 'c' baseado na classe Calculadora
    double valor = 0;   
    char opcao;

    while (true){
        cout << "--- Calculadora ---" << endl;
        c.exibir(); //Chama o método do objeto para mostrar o valor guardado em 'resultado'

        cout << "===== OPERAÇÕES =====" << endl;
        cout << "[ + ] Somar" << endl;
        cout << "[ - ] Subtrair" << endl;
        cout << "[ x ] Multiplicar" << endl;
        cout << "[ / ] Dividir" << endl;
        cout << "---------------------" << endl;
        cout << "[ C ] Zerar Calculadora" << endl;
        cout << "[ S ] Sair do Programa" << endl;
        cout << "=====================" << endl;

        cout << "Digite qual operação você quer: " << endl;
        cin >> opcao; //Guarda o caractere digitado pelo usuário

        //Avalia qual caractere foi digitado na variável 'opcao'
        switch (opcao) {

            case 'C': 
                c.resultado = 0; //Acessa diretamente o atributo do objeto e reseta seu valor para zero
                break; //Sai do bloco switch e volta para o início do while
        
            case '+': 
                cout << "Digite um número para somar: " << endl;
                cin >> valor;
                c.somar(valor); //Passa o número digitado como argumento para o método 'somar'
                break;
            

            case '-': 
                cout << "Digite um número para subtrair: " << endl;
                cin >> valor;
                c.subtracao(valor); //Passa o número digitado como argumento para o método 'subtracao'
                break;
            
            case 'x': 
                cout << "Digite um número para multiplicar: " << endl;
                cin >> valor;
                c.multiplicacao(valor); //Passa o número digitado como argumento para o método 'multiplicacao'
                break;

            case '/':
                cout << "Digite um número para dividir: " << endl;
                cin >> valor;

                //Impede o cálculo caso o divisor seja zero
                if (valor == 0) {
                    cout << "Erro! Não existe divisão por zero.";
                }
                else{

                    //Só chama o método se o valor for seguro (diferente de zero)
                    c.divisao(valor); //Passa o número digitado como argumento para o método 'divisao'
                }
                break;

            case 'S':
                cout << "Saindo do programa..." << endl;
                return 0; //Encerra a função main() imediatamente, fechando o programa por completo
            
            //Caso o usuário digite qualquer coisa que não seja +, -, x, /, C ou S
            default:
                cout << "Incorreto, você deve escolher uma das opções" << endl;
        }
    }

    return 0;
}
