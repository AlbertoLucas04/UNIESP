
import java.util.Locale;
import java.util.Scanner;

public class Main_exemplo2 {

    public static void main(String[] args) {

        Locale.setDefault(Locale.US);



        Scanner sc = new Scanner(System.in);
        Scanner sc2 = new Scanner(System.in);

        int x = 0;

        do {

            System.out.println("=== PÁGINA DE CADASTRO ===");
            System.out.println();

            System.out.print("Informe seu nome: ");
            String nome = sc.nextLine();


            System.out.print("Informe sua idade: ");
            int idade = sc.nextInt();


            System.out.print("Informe sua altura: ");
            Double altura = sc.nextDouble();
            sc2.nextLine();

            System.out.println();
            System.out.println("Dados colhidos:");
            System.out.println("Nome: " + nome);
            System.out.println("Idade: " + idade);
            System.out.println("Altura: " + altura);
            System.out.println();

        }while (x == 0);

    }

}
