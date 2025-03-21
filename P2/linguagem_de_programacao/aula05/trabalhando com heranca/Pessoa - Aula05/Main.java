import java.util.Locale;
import java.util.Scanner;

public class Main {
    public Main() {

    }

    public static void main(String[] args) {

        Locale.setDefault(Locale.US);

        Scanner sc = new Scanner(System.in);
        Pessoa pessoa = new Pessoa();
        Aluno aluno1 = new Aluno("João", 123);
        Aluno aluno2 = new Aluno("Maria", 456);
        Aluno aluno3 = new Aluno("Ana", 789);
        Professor professor = new Professor();



        System.out.print("\n === Sistema Escolar === \n");

        System.out.print("O que você deseja cadastrar?\n1.Aluno\n2.Professor\n");

        int option = sc.nextInt();

        switch (option) {


            case 1:
                System.out.print("\n === Sistema Escolar -> Aluno === \n");
                System.out.print("Nome: ");
                aluno1.setNome(sc.next());
                System.out.print("\nMatricula: ");
                aluno1.setMatricula(sc.nextInt());
                System.out.print("Idade: ");
                aluno1.setIdade(sc.nextInt());

            case 2:
                System.out.print("\n === Sistema Escolar -> Professor === \n");
                System.out.print("Nome: ");
                professor.setNome(sc.next());
                System.out.print("Salário = R$ " + professor.getSalario());

            case 3:
                System.out.print("OPÇÃO INVÁLIDA");
        }


    }
}