package Q3;

public class Produto {

    String nome;
    double preco;
    int quantidade_estoque;

    public void exibir(){

        System.out.println("\n=== Informações atuais ===\n");
        System.out.print("\nProduto: " + nome);
        System.out.print("\nValor do produto: R$ " + preco);
        System.out.print("\nQuantidade: " + quantidade_estoque);
        System.out.println();
    }


    public void venda(int quantidade_compra){

        quantidade_estoque = quantidade_estoque - quantidade_compra;

    }

}
