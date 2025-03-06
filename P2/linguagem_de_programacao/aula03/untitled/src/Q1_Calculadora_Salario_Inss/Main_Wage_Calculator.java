package Q1_Calculadora_Salario_Inss;

import java.util.Scanner;
import java.util.Locale;


public class Main_Wage_Calculator {

    public static void main(String[] args) {

        Locale.setDefault(Locale.US);

        Calc_contracheque inss_calc = new Calc_contracheque();
        Scanner input = new Scanner(System.in);

        System.out.println("=== Calculadora de salário ===\n");

        // Inserido antes dos double ou int, para não dar bug.
        System.out.print("Insira seu nome: ");
        inss_calc.nome = input.nextLine();

        System.out.print("Insira a sua matrícula: ");
        inss_calc.matricula = input.nextInt();

        System.out.print("Insira o seu salário bruto = R$ ");
        inss_calc.salario_bruto = input.nextDouble();

        System.out.println("\n=== Contracheque ===\n");

        System.out.println("Matrícula: " + inss_calc.matricula);
        System.out.println("Nome: " + inss_calc.nome);
        System.out.println("Salário Bruto = R$ " + inss_calc.salario_bruto);
        System.out.println("Dedução do INSS = R$ " + inss_calc.deducao_inss());
        System.out.println("Salário Líquido = R$ " + inss_calc.salario_descontado());
    }




}
