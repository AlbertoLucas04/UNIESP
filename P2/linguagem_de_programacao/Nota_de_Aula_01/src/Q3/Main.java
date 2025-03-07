package Q3;

import java.util.Scanner;
import java.util.Locale;
public class Main {

    public static void main(String[] args) {

        java.util.Locale.setDefault(java.util.Locale.US);
        Produto prod = new Produto();
        Scanner input = new Scanner(System.in);

        System.out.print("Digite o nome do produto: ");
        prod.nome = input.nextLine();

        System.out.print("Digite o valor do produto: R$ ");
        prod.preco = input.nextDouble();

        System.out.print("Digite a quantidade do produto: ");
        prod.quantidade_estoque = input.nextInt();

        // Exibição após o cadastro
        prod.exibir();

        System.out.print("\nDigite quantos deseja comprar: ");
        int quantidade_compra = input.nextInt();

        prod.venda(quantidade_compra);

        // Exibição após a compra
        prod.exibir();

    }

}
