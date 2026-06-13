/******************************************************************************

1-Considere a seguinte situação: Uma conta bancária possui um saldo e um limite. O valor máximo que o usuário da 
conta pode sacar é a soma do limite com o saldo. Crie uma função chamada sacar que recebe como parâmetro um 
valor e debite do saldo o valor solicitado.

*******************************************************************************/
#include <iostream>

using namespace std;

float sacar(float &saldo, float limite, float valor){
    if (valor <= (saldo + limite)){
        saldo -= valor;
        return true;
    } 
    else{
        cout << "Saldo indisponível" << endl;
        return false;
    }
    
}

int main()
{
    float saldo= 200.00;
    float limite= 1000.00;
    float Valor;
    
    cout<<"Digite o valor que você deseja sacar: ";
    cin >> Valor;
    
    bool resultado= sacar(saldo, limite, Valor);
    
    cout << "\n--- Extrato ---" << endl;
    if (resultado) {
        cout << "Saque realizado com sucesso!" << endl;
    }
    
    cout << "Saldo atual: R$ " << saldo << endl;
    cout << "Limite disponível: R$ " << limite << endl;

    return 0;
}