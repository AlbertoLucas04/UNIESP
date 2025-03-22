import java.util.Locale;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        Locale.setDefault(Locale.US);
        Product_Control pc = new Product_Control();

        int option = 0;


        do {
            System.out.println("\n===== Sistema de Controle -> Produtos =====\n");

            System.out.println("O que você deseja fazer?");

            System.out.println("1. Cadastrar um produto\n2. Comprar um produto 3. Sair do Sistema");
            sc.nextInt(option);

            switch (option) {

                case 01:

                    System.out.print("===== Sistema de Controle -> Produto -> Cadastrar um produto =====");

                    System.out.print("Nome: ");
                    pc.setNome(sc.next());

                    System.out.print("Preço (R$): ");
                    pc.setValor(sc.nextDouble());

                    System.out.print("Tamanho (P, M, G, ...): ");
                    pc.setTamanho(sc.next());

                    System.out.print("Peso (Kg): ");
                    pc.setPeso(sc.nextDouble());

                    System.out.print("Quantidade (Un): ");
                    pc.setQuantidade(sc.nextInt());

                    System.out.print("Código (XXXX): ");
                    pc.setCodigo(sc.nextInt());

                    System.out.print("Cor: ");
                    pc.setCor(sc.next());


                case 02:

                default:
                    System.out.print("Insira uma opção válida.");;




            }



        } while (option != 3);
    }

}