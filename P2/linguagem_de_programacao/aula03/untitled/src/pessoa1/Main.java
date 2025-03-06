package pessoa1;

import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

      Locale.setDefault(Locale.US);

      Scanner input = new Scanner(System.in);
      Pessoa pessoa = new Pessoa();

        System.out.print("Digite seu nome: ");
        pessoa.nome = input.nextLine();

        System.out.print("Digite sua idade: ");
        pessoa.idade = input.nextInt();

        System.out.print("Digite sua altura: ");
        pessoa.altura = input.nextDouble();

        System.out.println();
        System.out.println("=== Dados Recolhidos ===");
        System.out.println();
        System.out.println("Nome: " + pessoa.nome);
        System.out.println("Idade: " + pessoa.idade);
        System.out.println("Altura: " + pessoa.altura);


    }
}

