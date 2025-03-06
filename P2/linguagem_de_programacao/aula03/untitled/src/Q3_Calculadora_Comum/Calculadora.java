package Q3_Calculadora_Comum;

public class Calculadora {

    double n1, n2, soma, subtracao, multiplicacao, divisao;

    public double somar() {
        soma = n1 + n2;
        return soma;
    }

    public double subtrair() {
        subtracao = n1 - n2;
        return subtracao;
    }

    public double multiplicar() {
        multiplicacao = n1 * n2;
        return multiplicacao;
    }

    public void dividir() {
        divisao = n1 / n2;
        System.out.println("Divisão: " + divisao);
    }
}
