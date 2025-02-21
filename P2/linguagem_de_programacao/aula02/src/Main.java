import java.util.Locale;
import java.util.Scanner;

public class Main  {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);

        String r ;

        Scanner sc = new Scanner(System.in);

       do {
           System.out.println("=== Seja bem-vindo(a) a Loja! ===");

           System.out.println("1. Vou dar uma olhadinha. ");
           System.out.println("2. Qual o valor da blusa? ");
           System.out.println("3. Quero falar com um atendente. ");

           System.out.print("Opção => ");

           int r = sc.nextLine();

           switch (r) {
               case 1:
                   System.out.println("Fique à vontade!");
                   break;
               case 2:
                   System.out.println("O valor da blusa é R$ 2,00.");
                   break;
               case 3:
                   System.out.println("Atendente solicitado!");
                   break;
               default:
                   System.out.println("Opção inválida.");
                   break;
           }
           System.out.println("Para repetir, digite 0.");
            r = sc.nextInt();

       } while (r.equalsIgnoreCase("S"));

    }
}