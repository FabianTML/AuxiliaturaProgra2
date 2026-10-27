import java.util.Arrays;

public class Laptop {
    public static final int MAX_APPS = 50;

    private final String modelo;
    private int cantApps;
    private final Aplicacion[] apps;
    private final Pantalla pantalla;

    public Laptop(String modelo, String tipoPantalla, int ancho, int alto) {
        if (modelo == null || modelo.trim().isEmpty()) {
            throw new IllegalArgumentException("El modelo de la laptop es obligatorio");
        }
        this.modelo = modelo.trim();
        this.cantApps = 0;
        this.apps = new Aplicacion[MAX_APPS];
        this.pantalla = new Pantalla(tipoPantalla, ancho, alto);
    }

    public boolean agregarApp(Aplicacion app) {
        if (app == null || cantApps == MAX_APPS) {
            return false;
        }
        apps[cantApps++] = app;
        return true;
    }

    public void eliminarApps() {
        Arrays.fill(apps, 0, cantApps, null);
        cantApps = 0;
    }

    public void ordenarApps() {
        Arrays.sort(apps, 0, cantApps, Aplicacion.POR_TAMANIO_DESC_Y_NOMBRE);
    }

    public String getModelo() {
        return modelo;
    }

    public int getCantApps() {
        return cantApps;
    }

    public Pantalla getPantalla() {
        return pantalla;
    }

    public Aplicacion getApp(int indice) {
        if (indice < 0 || indice >= cantApps) {
            throw new IndexOutOfBoundsException("Índice de aplicación inválido: " + indice);
        }
        return apps[indice];
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Laptop ").append(modelo)
                .append(" | Pantalla: ").append(pantalla)
                .append(" | Aplicaciones: ").append(cantApps);
        for (int i = 0; i < cantApps; i++) {
            sb.append(System.lineSeparator())
                    .append("    ").append(i + 1).append(". ").append(apps[i]);
        }
        return sb.toString();
    }
}
