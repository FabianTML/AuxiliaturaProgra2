import java.util.Scanner;

public class E {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            Laptop[] laptops = A.obtenerLaptops(sc);
            System.out.println("Laptops cargadas:");
            A.mostrar(laptops);
            System.out.println();
            B.mostrarConMasApps(laptops);
        }
    }
}
