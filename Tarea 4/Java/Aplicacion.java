import java.util.Comparator;

public class Aplicacion {
    public static final Comparator<Aplicacion> POR_TAMANIO_DESC_Y_NOMBRE =
            Comparator.comparingInt(Aplicacion::getTamanio).reversed()
                    .thenComparing(Aplicacion::getNombre, String.CASE_INSENSITIVE_ORDER);

    private final String nombre;
    private final int tamanio;

    public Aplicacion(String nombre, int tamanio) {
        if (nombre == null || nombre.trim().isEmpty()) {
            throw new IllegalArgumentException("El nombre de la aplicación es obligatorio");
        }
        if (tamanio <= 0) {
            throw new IllegalArgumentException("El tamaño de la aplicación debe ser positivo");
        }
        this.nombre = nombre.trim();
        this.tamanio = tamanio;
    }

    public String getNombre() {
        return nombre;
    }

    public int getTamanio() {
        return tamanio;
    }

    @Override
    public String toString() {
        return nombre + " - tamaño: " + tamanio;
    }
}
