Práctica 1 TecWeb. Página web sobre el mítico y legendario Roadster Mazda MX-5 Miata (Cochazo)

Se han empleado los estilos vistos en clase, para hacer que las imágenes "aumenten" de tamaño cuando el cursor está encima se ha empleado:
.gallery, .grid-gallery {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 10px;
    padding: 20px;
}

.gallery img, .grid-gallery img {
    width: 200px;
    height: auto;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    transition: transform 0.3s;
}

.gallery img:hover, .grid-gallery img:hover {
    transform: scale(1.1);
}
