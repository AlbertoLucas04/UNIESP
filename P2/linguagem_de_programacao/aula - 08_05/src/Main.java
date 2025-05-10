import controller.ProfessorController;
import model.Professor;

import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        ProfessorController professorController = new ProfessorController();
        Professor p = new Professor();

        System.out.print("Digite o nome do professor: ");
        p.setNome(sc.next());

        System.out.print("Digite a idade do professor: ");
        p.setIdade(sc.nextInt());

        System.out.print("Digite a especialização do professor: ");
        p.setEspecialização(sc.next());

        //Cadastrar Professor
        professorController.cadastrarProfessor(p);







        //Cadastrar Aluno


    }
}