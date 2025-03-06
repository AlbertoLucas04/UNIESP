package Q2_Calculadora_Media;
import java.util.Scanner;
import java.util.Locale;

public class Main {

    public static void main(String[] args) {

        Locale.setDefault(Locale.US);

        Scanner input = new Scanner(System.in);
        Aluno aluno = new Aluno();

        System.out.println("=== Calculadora de média ===\n");

        System.out.print("Insira seu nome: ");
        aluno.nome = input.nextLine();

        System.out.print("Insira sua primeira nota: ");
        aluno.nota1 = (input.nextDouble());

        System.out.print("Insira sua segunda nota: ");
        aluno.nota2 = (input.nextDouble());

        System.out.print("Média =  " + aluno.media_aluno() + "\n");

        if (aluno.media >= 7) {
            System.out.println("\nVocê está aprovado!");
        }else if (aluno.media < 4){
            System.out.println("\nVocê está reprovado!");
        }else{
            System.out.println("\nVocê está na final!");
        }

    }
}
