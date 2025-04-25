package pessoa1;

public final class Aluno extends Pessoa{

    private int matricula;

    public int getMatricula() {
        return matricula;
    }

    public void setMatricula(int matricula) {
        this.matricula = matricula;
    }

    @Override
    public void quemSouEu() {
        System.out.print("Eu sou o aluno " + nome);
    }

    @Override
    public void minhaAtividade() {
        System.out.println("Eu aprendo!");
    }
}
