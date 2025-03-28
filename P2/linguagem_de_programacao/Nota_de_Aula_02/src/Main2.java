import java.util.Locale;
import java.util.Scanner;

public class Main2 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        Locale.setDefault(Locale.US);
        Product_Control pc = new Product_Control();

        int option = 0;
        int option_compra = 0;
        int parcelas = 0;
        double valor_pago = 0;
        int qtd_cliente = 0;


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
                    pc.setvalorProduto(sc.nextDouble());

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
                    System.out.print("===== Sistema de Controle -> Produto -> Comprar um produto =====");

                    System.out.print("\nProduto: " + pc.getNome());
                    System.out.print("\nValor: R$ " + pc.getvalorProduto());
                    System.out.print("\nQuantidade em estoque: " + pc.controleDeEstoque(qtd_cliente));

                    System.out.print("\nQuantos você deseja levar? ");
                    qtd_cliente = sc.nextInt();

                    System.out.println("\nValor final da compra: R$ " + pc.valorFinal(pc.getvalorProduto(), qtd_cliente));

                    System.out.println("\nQual será a forma de pagamento?");
                    System.out.print("1. À vista\n2. Débito\n3. Crédito");
                    System.out.print("\n=» ");
                    option_compra = sc.nextInt();

                    System.out.println("Valor final da compra: R$ " + pc.valorFinal(pc.getvalorProduto(), qtd_cliente));

                    switch (option_compra) {

                        case 1:
                            System.out.println("Meus parabéns! Por pagar à vista, você acaba de ganhar um desconto de 5%.");
                            System.out.println("Valor final da compra (Com desconto): R$ " + pc.pagtoComDesconto(pc.valorFinal(pc.getvalorProduto(),qtd_cliente),qtd_cliente));
                            System.out.print("\nInsira o valor em mãos: R$ ");
                            valor_pago = sc.nextDouble();


                            if (valor_pago > pc.pagtoComDesconto(pc.valorFinal(pc.getvalorProduto(),qtd_cliente),qtd_cliente)) {
                                System.out.print("\nSeu troco é de R$ " + pc.troco(valor_pago, pc.pagtoComDesconto(pc.valorFinal(pc.getvalorProduto(),qtd_cliente),qtd_cliente)));
                                System.out.println("\nObrigado, volte sempre!");
                            } else if (valor_pago == pc.pagtoComDesconto(pc.valorFinal(pc.getvalorProduto(),qtd_cliente),qtd_cliente)) {
                                System.out.println("\nObrigado, volte sempre!");
                            } else {
                                System.out.print("\nInsira um valor válido!");
                            }
                            break;

                        case 2:
                            System.out.println("\nObrigado, volte sempre!");
                            break;

                        case 3:
                            System.out.println("\nNós parcelamos em até 3x sem juros. Em quantas parcelas você deseja pagar?");
                            System.out.print("=» ");
                            parcelas = sc.nextInt();

                            System.out.println("\nSerão " + parcelas + " parcelas de R$ " + pc.pagtoParcelado(pc.getvalorProduto(), parcelas));
                            break;

                        default:
                            System.out.print("\nInsira uma opção válida.");
                    }
                    break;

                case 3:
                    System.out.println("\nObrigado, volte sempre!");
                    break;

                default:
                    System.out.print("\nInsira uma opção válida.");
            }

        } while (option != 3);

    }
}
