/******************************************************************************

1-Considere a seguinte situação: Uma conta bancária possui um saldo e um limite. 
O valor máximo que o usuário da conta pode sacar é a soma do limite com o saldo. 
Crie uma função chamada sacar que recebe como parâmetro um valor e debite do saldo 
o valor solicitado.

*******************************************************************************/
#include <iostream>

using namespace std;

//Função 'sacar': recebe o saldo por referência (&) para que as alterações alterem a variável original.
//O limite e o valor a ser sacado são passados por valor (apenas cópias).
//Retorna 'true' se o saque for bem-sucedido e 'false' caso contrário.
float sacar(float &saldo, float limite, float valor){
    
    //Verifica se o valor solicitado é menor ou igual à soma do saldo disponível com o limite
    if (valor <= (saldo + limite)){

        //Deduz o valor solicitado diretamente do saldo
        saldo -= valor; 

        //Retorna verdadeiro indicando que a operação foi realizada
        return true;    
    } 
    else{

        //Se o valor for maior que o saldo + limite, exibe mensagem de erro
        cout << "Saldo indisponível" << endl;

        //Retorna falso indicando falha na operação
        return false;   
    }
}

int main()
{
    //Inicialização das variáveis da conta bancária
    float saldo = 200.00;
    float limite = 1000.00;

    //Armazenará o valor que o usuário deseja sacar
    float Valor; 
    
    //Solicita a entrada de dados do usuário
    cout << "Digite o valor que você deseja sacar: ";
    cin >> Valor;
    
    //Chama a função 'sacar' passando as variáveis correspondentes.
    //O resultado da função (true ou false) é armazenado na variável 'resultado'.
    bool resultado = sacar(saldo, limite, Valor);
    
    //Impressão do extrato bancário
    cout << "\n--- Extrato ---" << endl;
    
    //Se o 'resultado' for true, significa que o saque foi aprovado
    if (resultado) {
        cout << "Saque realizado com sucesso!" << endl;
    }
    
    //Exibe os valores atualizados na tela
    cout << "Saldo atual: R$ " << saldo << endl;
    cout << "Limite disponível: R$ " << limite << endl;

    return 0;
}