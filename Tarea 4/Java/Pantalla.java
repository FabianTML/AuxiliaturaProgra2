public class Pantalla {
    private final String tipo;
    private final int ancho;
    private final int alto;

    public Pantalla(String tipo, int ancho, int alto) {
        if (tipo == null || tipo.trim().isEmpty()) {
            throw new IllegalArgumentException("El tipo de pantalla es obligatorio");
        }
        if (ancho <= 0 || alto <= 0) {
            throw new IllegalArgumentException("Las dimensiones de la pantalla deben ser positivas");
        }
        this.tipo = tipo.trim();
        this.ancho = ancho;
        this.alto = alto;
    }

    public String getTipo() {
        return tipo;
    }

    public int getAncho() {
        return ancho;
    }

    public int getAlto() {
        return alto;
    }

    @Override
    public String toString() {
        return tipo + " " + ancho + "x" + alto;
    }
}
