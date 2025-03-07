package Q4;

import java.util.Scanner;
import java.util.Locale;

public class Main {

    public static void main(String[] args) {

        java.util.Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        Operacoes op = new Operacoes();

        int opcao;
        double deposito;

        do {
            System.out.print("\n=== Banco Alb ===\n");
            System.out.println("O que você deseja fazer?\n");
            opcao = sc.nextInt();
            System.out.println("1- Consultar saldo atual\n");
            System.out.println("2- Depositar\n");
            System.out.println("3- Sacar\n");
            System.out.println("4- Transferir\n");
            System.out.println("5- Realizar outra operação\n");

            switch (opcao) {
                case 1:
                    System.out.print("Saldo atual = R$" + op.exibir_saldo());
                case 2:
                    System.out.print("Qual valor você deseja depositar?");
                    deposito = sc.nextDouble();
                    op.depositar();
                case 3:

            }
        } while (opcao == 5);
    }

}
