public class Main_Q4 {

    public static void main(String[] args) {

        double salario = 0;
        double desc_1 = salario - (0.05 * salario);
        double desc_2 = salario - (0.10 * salario);
        double desc_3 = salario - (0.20 * salario);

        if (salario <= 900) {
            System.out.println("\nVocê é isento de Imposto de Renda!\n");
        } else if (salario > 900 && salario <= 1501 ) {
            System.out.println("\nVocê terá um desconto de 05% no seu salário referente ao Imposto de Renda, totalizando R$ " + desc_1);
            
        } else if (salario > 1501 && salario <= 2500) {
            System.out.println("\nVocê terá um desconto de 10% no seu salário referente ao Imposto de Renda, totalizando R$ " + desc_2 );
        }
        else{
            System.out.println("\nVocê terá um desconto de 20% no seu salário referente ao Imposto de Renda, totalizando R$ " + desc_3 );
        }
        
    }
}
