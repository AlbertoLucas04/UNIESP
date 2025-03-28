/*
import java.util.Locale;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        Locale.setDefault(Locale.US);
        Product_Control pc = new Product_Control();

        int option = 0;
        int option_compra = 0;
        int parcelas = 0;
        double valor_pago = 0;

        do {
            System.out.println("\n===== Sistema de Controle -> Produtos =====\n");
            System.out.println("O que você deseja fazer?");
            System.out.println("1. Cadastrar um produto\n2. Comprar um produto\n3. Sair do Sistema");
            System.out.print("=» ");
            option = sc.nextInt();

            switch (option) {

                case 1:
                    System.out.print("===== Sistema de Controle -> Produto -> Cadastrar um produto =====\n");

                    System.out.print("Nome: ");
                    pc.setNome(sc.next());

                    System.out.print("Preço (R$): ");
                    pc.setValor(sc.nextDouble());

                    System.out.print("Tamanho (P, M, G, NDef, ...): ");
                    pc.setTamanho(sc.next());

                    System.out.print("Peso (Kg): ");
                    pc.setPeso(sc.nextDouble());

                    System.out.print("Quantidade (Un): ");
                    pc.setQuantidade(sc.nextInt());

                    System.out.print("Código (XXXX): ");
                    pc.setCodigo(sc.nextInt());

                    System.out.print("Cor: ");
                    pc.setCor(sc.next());

                    break;

                case 2:

                    System.out.print("===== Sistema de Controle -> Produto -> Comprar um produto =====\n");

                    System.out.print("Produto:" + pc.getNome());
                    System.out.print("\nValor: R$" + pc.getValor());
                    System.out.print("\nQuantidade:" + pc.getQuantidade());

                    System.out.println("Qual será a forma de pagamento?");
                    System.out.print("1. À vista\n2. Débito\n3. Crédito");
                    option_compra = sc.nextInt();

                    switch (option_compra) {

                        case 1:

                            System.out.print("Insira o valor em mãos: R$ ");
                            valor_pago = sc.nextDouble();
                            pc.setValor_pago(valor_pago);

                            if (pc.getValor_pago() > pc.getValor()) {

                                System.out.print("Seu troco é de R$ " + pc.troco(pc.getValor_pago(), pc.getValor()));
                                System.out.println("Obrigado, volte sempre!");
                                break;

                            } else if (pc.getValor_pago() == pc.getValor()) {

                                System.out.println("Obrigado, volte sempre!");
                                break;

                            } else {
                                System.out.print("Insira um valor válido!");
                            }

                    }
                    break;

                        case 2:

                            System.out.println("Obrigado, volte sempre!");
                            break;

                        case 3:

                            System.out.println("Nós parcelamos em até 3x sem juros. Em quantas parcelas você deseja pagar?");
                            System.out.print("=» ");
                            parcelas = sc.nextInt();

                            System.out.println("Serão " + parcelas + " parcelas de " + pc.pagtoParcelado(pc.getValor(), parcelas));
                            break;
                        default:
                            System.out.print("Insira uma opção válida.");

            }

                case 3:
                    System.out.println("Obrigado, volte sempre!");
                    break;

            } while (option != 3);

        }
    }
}
*/