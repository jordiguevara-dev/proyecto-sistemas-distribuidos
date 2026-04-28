package com.neptuno.middleware.controller;

import com.neptuno.middleware.model.Producto;
import com.neptuno.middleware.repository.ProductoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.Map;

@RestController
@RequestMapping("/api/inventario")
public class ProductoController {

    @Autowired
    private ProductoRepository productoRepository;
    @GetMapping("/lista")
    public java.util.List<Producto> listarProductos() {
        return productoRepository.findAll();
    }
    @PostMapping("/pedido")
    public String realizarPedido(@RequestBody Map<String, Integer> pedido) {
        try {
            Integer id = pedido.get("id");
            Integer cantidad = pedido.get("cantidad");

            Producto producto = productoRepository.findById(id)
                    .orElseThrow(() -> new RuntimeException("Producto no encontrado en Neptuno"));

            if (producto.getStock() < cantidad) {
                return "Error: Stock insuficiente para " + producto.getNombre() + ". Disponible: " + producto.getStock();
            }

            producto.setStock(producto.getStock() - cantidad);
            productoRepository.save(producto);

            return "Pedido realizado con éxito. Nuevo stock de " + producto.getNombre() + ": " + producto.getStock();
            
        } catch (Exception e) {
            return "Error en el Middleware: " + e.getMessage();
        }
    }
    @PostMapping("/registrar")
    public String crearProducto(@RequestBody Producto nuevoProducto) {
        try {
            // El ID lo recibimos del cliente
            if (productoRepository.existsById(nuevoProducto.getId())) {
                return "Error: El ID " + nuevoProducto.getId() + " ya existe.";
            }
            productoRepository.save(nuevoProducto);
            return "Producto '" + nuevoProducto.getNombre() + "' registrado correctamente con ID " + nuevoProducto.getId();
        } catch (Exception e) {
            return "Error al registrar: " + e.getMessage();
        }
    }
}
