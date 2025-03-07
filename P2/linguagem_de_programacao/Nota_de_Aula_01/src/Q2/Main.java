package Q2;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Matematica mat = new Matematica();
        Scanner input = new Scanner(System.in);

        int option;
        int repeat;
        double n3, n4;
        do {

            System.out.println("=== CALCULADORA ===");

            System.out.println();

            System.out.print("Número 01 -> ");
            mat.n1 = input.nextDouble();
            System.out.print("Número 02 -> ");
            mat.n2 = input.nextDouble();

            System.out.println();

            System.out.println("O que você deseja fazer?");
            System.out.println();
            System.out.println("1. Somar");
            System.out.println("2. Subtrair");
            System.out.println("3. Multiplicar");
            System.out.println("4. Dividir");
            System.out.println();

            option = input.nextInt();

            switch (option) {

                case 1:
                    System.out.println("\nSoma = " + mat.somar());
                    break;
                case 2:
                    System.out.println("\nSubtração = " + mat.subtrair());
                    break;
                case 3:
                    System.out.println("\nMultiplicação = " + mat.multiplicar());
                    break;
                case 4:
                    System.out.println("\nDivisão = " + mat.dividir());
                    break;
                default:
                    System.out.println("Insira um número válido.");
            }
            System.out.println();
            System.out.print("Digite 5 para repetir -> ");
            repeat = input.nextInt();
        } while (repeat == 5);
    }
}


