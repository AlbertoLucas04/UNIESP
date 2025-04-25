package pessoa1;

public final class Professor extends Pessoa implements FolhaDePagamento {

    public Categoria categoria;

    private String especialidade;

    private double salario, bonus;

    public double getBonus() {
        return bonus;
    }

    public void setBonus(double bonus) {
        this.bonus = bonus;
    }


    public double getSalario() {
        return salario;
    }

    public void setSalario(double salario) {
        this.salario = salario;
    }

    public String getEspecialidade() {
        return especialidade;
    }

    public void setEspecialidade(String especialidade) {
        this.especialidade = especialidade;
    }

    @Override
    public String toString() {
        return "Professor{" +
                ", nome='" + nome + '\'' +
                ", idade=" + idade +
                ", altura=" + altura +
                ", especialidade='" + especialidade + '\'' +
                '}';
    }

    @Override
    public void quemSouEu() {
        System.out.print("Sou o Professor " + nome);
    }

    @Override
    public void minhaAtividade() {
        System.out.println("Eu ensino!");
    }


    public Categoria getCategoria() {
        return categoria;
    }

    @Override
    public void CalcularSalario() {
        salario = this.salario + this.bonus;
    }

    @Override
    public void aplicarBonus() {
        this.bonus = bonus;
    }



}
