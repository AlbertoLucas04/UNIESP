package pessoa1;

public abstract class Pessoa {

    protected String nome;

    protected int idade;

    protected double altura;

    public void aniversario( ){

        idade ++;

    }

    @Override
    public String toString() {
        return "Pessoa{" +
                "nome='" + nome + '\'' +
                ", idade=" + idade +
                ", altura=" + altura +
                '}';
    }

    public abstract void quemSouEu();
    public abstract void minhaAtividade();

}
