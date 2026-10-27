import java.util.Scanner;

public class A {
    private static final String[] MODELOS = {"ThinkPad", "MacBook", "Inspiron", "Aspire", "ZenBook", "Pavilion"};
    private static final String[] TIPOS = {"LED", "OLED", "IPS", "LCD"};
    private static final int[] ANCHOS = {1366, 1600, 1920, 2560};
    private static final int[] ALTOS = {768, 900, 1080, 1440};
    private static final String[] NOMBRES_APPS = {
            "Chrome", "Word", "Excel", "Zoom", "Spotify", "Slack",
            "Teams", "Photoshop", "VSCode", "Steam", "Discord", "Firefox"
    };
    private static final int[] TAMANIOS_APPS = {120, 450, 120, 800, 450, 200};

    public static Laptop[] instanciarDeEjemplo(int n) {
        Laptop[] laptops = new Laptop[n];
        for (int i = 0; i < n; i++) {
            int pantalla = i % ANCHOS.length;
            laptops[i] = new Laptop(
                    MODELOS[i % MODELOS.length] + "-" + (i + 1),
                    TIPOS[(i / 2) % TIPOS.length],
                    ANCHOS[pantalla],
                    ALTOS[pantalla]);
            int cantidad = 2 + (i * 7) % 11;
            for (int j = 0; j < cantidad; j++) {
                laptops[i].agregarApp(new Aplicacion(
                        NOMBRES_APPS[(i + j) % NOMBRES_APPS.length],
                        TAMANIOS_APPS[(i * 3 + j) % TAMANIOS_APPS.length]));
            }
        }
        return laptops;
    }

    public static Laptop[] instanciarManual(Scanner sc, int n) {
        Laptop[] laptops = new Laptop[n];
        for (int i = 0; i < n; i++) {
            System.out.println("--- Laptop " + (i + 1) + " de " + n + " ---");
            String modelo = Consola.leerTexto(sc, "Modelo: ");
            String tipo = Consola.leerTexto(sc, "Tipo de pantalla: ");
            int ancho = Consola.leerEntero(sc, "Ancho de pantalla: ", 1);
            int alto = Consola.leerEntero(sc, "Alto de pantalla: ", 1);
            Laptop laptop = new Laptop(modelo, tipo, ancho, alto);
            int cantidad = Consola.leerEntero(sc,
                    "Cantidad de aplicaciones (0-" + Laptop.MAX_APPS + "): ", 0, Laptop.MAX_APPS);
            for (int j = 0; j < cantidad; j++) {
                String nombre = Consola.leerTexto(sc, "  Aplicación " + (j + 1) + " - nombre: ");
                int tamanio = Consola.leerEntero(sc, "  Aplicación " + (j + 1) + " - tamaño: ", 1);
                laptop.agregarApp(new Aplicacion(nombre, tamanio));
            }
            laptops[i] = laptop;
        }
        return laptops;
    }

    public static Laptop[] obtenerLaptops(Scanner sc) {
        int n = Consola.leerEntero(sc, "Cantidad de laptops (N): ", 1);
        boolean manual = Consola.leerSiNo(sc, "¿Cargar los datos manualmente? Con 'n' se usan datos de ejemplo");
        System.out.println();
        return manual ? instanciarManual(sc, n) : instanciarDeEjemplo(n);
    }

    public static void mostrar(Laptop[] laptops) {
        for (int i = 0; i < laptops.length; i++) {
            System.out.println((i + 1) + ") " + laptops[i]);
        }
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            Laptop[] laptops = obtenerLaptops(sc);
            System.out.println("Se instanciaron " + laptops.length + " laptops:");
            mostrar(laptops);
        }
    }
}
