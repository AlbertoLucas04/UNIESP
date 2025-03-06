package Q1_Calculadora_Salario_Inss;



public class Calc_contracheque {

    String nome;
    int matricula;
    int casas_decimais = 2;


    double salario_bruto, salario_liquido, inss;


    public double deducao_inss() {

        inss = salario_bruto * 0.15;
        return inss;
    }


    public double salario_descontado() {

        salario_liquido = salario_bruto - (inss);
        return salario_liquido;
    }

}
