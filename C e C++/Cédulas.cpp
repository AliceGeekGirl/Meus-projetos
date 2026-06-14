#include <iostream>

using namespace std;

int main() {
    //Declaração das variáveis
    int i;
    int N;
    
    //Vetor que armazena os valores das cédulas disponíveis, em ordem decrescente
    int cedulas[7] = {100, 50, 20, 10, 5, 2, 1};
    
    //Lê o valor inteiro N (removida a mensagem "Digite o valor" para evitar erro na plataforma)
    cin >> N;

    //A plataforma exige que a primeira linha da saída seja o próprio valor lido
    cout << N << endl;

    //Loop que passa por cada uma das 7 cédulas do vetor
    for (i = 0; i < 7; i++) {
        
        //Calcula quantas notas da cédula atual cabem no valor de N
        //Como 'N' e 'cedulas[i]' são inteiros, a divisão é inteira (descarta os decimais)
        int notas = N / cedulas[i];
        
        //Atualiza N com o resto da divisão, ou seja, o que sobrou para ser pago com as próximas notas
        N = N % cedulas[i];
        
        //Imprime a quantidade de notas e o valor da cédula no formato exato exigido pelo problema
        cout << notas << " nota(s) de R$ " << cedulas[i] << ",00" << endl;
    }
    
    //Indica que o programa foi executado com sucesso, retornando (mostrando) o programa
    return 0;
}