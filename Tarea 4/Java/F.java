import java.util.Scanner;

public class F {
    public static void ordenarAppsDeCadaLaptop(Laptop[] laptops) {
        for (Laptop laptop : laptops) {
            laptop.ordenarApps();
        }
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            Laptop[] laptops = A.obtenerLaptops(sc);
            System.out.println("Antes de ordenar:");
            A.mostrar(laptops);
            System.out.println();

            ordenarAppsDeCadaLaptop(laptops);

            System.out.println("Después de ordenar (tamaño decreciente, empate por nombre):");
            A.mostrar(laptops);
        }
    }
}
