package pessoa1;

import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

      Locale.setDefault(Locale.US);

      Scanner input = new Scanner(System.in);
      Professor prof = new Professor();

        System.out.print("Digite seu nome: ");
        prof.nome = input.nextLine();

        System.out.print("Digite sua idade: ");
        prof.idade = input.nextInt();

        System.out.print("Digite sua altura: ");
        prof.altura = input.nextDouble();

        System.out.print("Digite a especialização: ");
        prof.setEspecialidade(input.next());

        System.out.println(Categoria.Professor);

        System.out.println("\n=== Dados Recolhidos ===\n");
        System.out.println(prof);



    }
}

