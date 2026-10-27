import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class C {
    public static List<Laptop> buscarPorModelo(Laptop[] laptops, String modelo) {
        List<Laptop> coincidencias = new ArrayList<>();
        for (Laptop laptop : laptops) {
            if (laptop.getModelo().equalsIgnoreCase(modelo.trim())) {
                coincidencias.add(laptop);
            }
        }
        return coincidencias;
    }

    public static void agregarAppA(List<Laptop> destinos, Aplicacion app) {
        for (Laptop laptop : destinos) {
            if (laptop.agregarApp(app)) {
                System.out.println("Aplicación '" + app.getNombre() + "' agregada a la laptop " + laptop.getModelo() + ".");
            } else {
                System.out.println("La laptop " + laptop.getModelo() + " ya alcanzó el máximo de "
                        + Laptop.MAX_APPS + " aplicaciones.");
            }
        }
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            Laptop[] laptops = A.obtenerLaptops(sc);
            System.out.println("Laptops cargadas:");
            A.mostrar(laptops);
            System.out.println();

            String modelo = Consola.leerTexto(sc, "Modelo X: ");
            List<Laptop> coincidencias = buscarPorModelo(laptops, modelo);
            if (coincidencias.isEmpty()) {
                System.out.println("No existe ninguna laptop del modelo " + modelo + ".");
                return;
            }

            String nombre = Consola.leerTexto(sc, "Nombre de la aplicación: ");
            int tamanio = Consola.leerEntero(sc, "Tamaño de la aplicación: ", 1);
            System.out.println();
            agregarAppA(coincidencias, new Aplicacion(nombre, tamanio));

            System.out.println();
            System.out.println("Estado final:");
            A.mostrar(laptops);
        }
    }
}
