public class Product_Control {

    private String nome, tamanho, cor;
    private int codigo, quantidade, qtd_cliente;
    private double peso, valorProduto;



    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getTamanho() {
        return tamanho;
    }

    public void setTamanho(String tamanho) {
        this.tamanho = tamanho;
    }

    public String getCor() {
        return cor;
    }

    public void setCor(String cor) {
        this.cor = cor;
    }

    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public int getQuantidade() {
        return quantidade;
    }

    public void setQuantidade(int quantidade) {
        this.quantidade = quantidade;
    }

    public double getPeso() {
        return peso;
    }

    public void setPeso(double peso) {
        this.peso = peso;
    }

    public double getvalorProduto() {
        return valorProduto;
    }

    public void setvalorProduto(double valor_produto) {
        this.valorProduto = valor_produto;
    }

    // Métodos



    public double valorFinal(double valorProduto, int qtd_cliente) {
        return (this.getvalorProduto() * qtd_cliente);
    }

    public double troco(double valor_pago, double valor_produto){
        return (valor_pago - pagtoComDesconto(valorFinal(getvalorProduto(), qtd_cliente), qtd_cliente));
    }

    public double pagtoParcelado(double valor_produto, int qtd_parcelas){
        return (valor_produto/qtd_parcelas);
    }

    public int controleDeEstoque(int qtd_cliente){
        return (this.getQuantidade() - qtd_cliente);
    }

    public double pagtoComDesconto(double valor_produto, int qtd_cliente) {
        return (valorFinal(this.getvalorProduto(), qtd_cliente) - (valorFinal(this.getvalorProduto(), qtd_cliente)*0.05));
    }


}
