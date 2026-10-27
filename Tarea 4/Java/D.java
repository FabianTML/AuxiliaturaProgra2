import java.util.Scanner;

public class D {
    public static int eliminarAppsPorAncho(Laptop[] laptops, int ancho) {
        int afectadas = 0;
        for (Laptop laptop : laptops) {
            if (laptop.getPantalla().getAncho() == ancho) {
                laptop.eliminarApps();
                afectadas++;
            }
        }
        return afectadas;
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            Laptop[] laptops = A.obtenerLaptops(sc);
            System.out.println("Laptops cargadas:");
            A.mostrar(laptops);
            System.out.println();

            int ancho = Consola.leerEntero(sc, "Ancho Y de pantalla: ", 1);
            int afectadas = eliminarAppsPorAncho(laptops, ancho);
            System.out.println();
            if (afectadas == 0) {
                System.out.println("No hay laptops con pantalla de ancho " + ancho + ".");
                return;
            }
            System.out.println("Se eliminaron las aplicaciones de " + afectadas
                    + " laptop(s) con pantalla de ancho " + ancho + ".");
            System.out.println();
            System.out.println("Estado final:");
            A.mostrar(laptops);
        }
    }
}
