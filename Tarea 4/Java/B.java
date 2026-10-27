import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class B {
    public static List<Laptop> conMasApps(Laptop[] laptops) {
        List<Laptop> resultado = new ArrayList<>();
        int maximo = -1;
        for (Laptop laptop : laptops) {
            if (laptop.getCantApps() > maximo) {
                maximo = laptop.getCantApps();
                resultado.clear();
                resultado.add(laptop);
            } else if (laptop.getCantApps() == maximo) {
                resultado.add(laptop);
            }
        }
        return resultado;
    }

    public static void mostrarConMasApps(Laptop[] laptops) {
        List<Laptop> ganadoras = conMasApps(laptops);
        if (ganadoras.isEmpty()) {
            System.out.println("No hay laptops cargadas.");
            return;
        }
        if (ganadoras.get(0).getCantApps() == 0) {
            System.out.println("Ninguna laptop tiene aplicaciones instaladas.");
            return;
        }
        System.out.println(ganadoras.size() == 1
                ? "Laptop con más aplicaciones:"
                : "Laptops empatadas con más aplicaciones:");
        for (Laptop laptop : ganadoras) {
            System.out.println(laptop);
        }
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            Laptop[] laptops = A.obtenerLaptops(sc);
            System.out.println("Laptops cargadas:");
            A.mostrar(laptops);
            System.out.println();
            mostrarConMasApps(laptops);
        }
    }
}
