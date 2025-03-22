public class Product_Control {

    private String nome, tamanho, cor;
    private int codigo, quantidade, qtd_parcelas;
    private double peso, valor_produto, valor_pago;


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

    public double getValor() {
        return valor_produto;
    }

    public void setValor(double valor) {
        this.valor_produto = valor;
    }

    public double getValor_pago() {
        return valor_pago;
    }

    public void setValor_pago(double valor_pago) {
        this.valor_pago = valor_pago;
    }

    public double pagtoComDesconto(double valor_produto) {
        return (this.valor_produto - (this.valor_produto*0.05));
    }

    public double troco(double valor_produto, double valor_pago){
        return (this.valor_pago - this.valor_produto);
    }

    public double pagtoParcelado(double valor_produto, int qtd_parcelas){
        return (valor_produto/qtd_parcelas);
    }



}
