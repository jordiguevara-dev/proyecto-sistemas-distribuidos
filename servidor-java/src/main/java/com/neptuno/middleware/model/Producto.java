package com.neptuno.middleware.model;

import jakarta.persistence.*;
import lombok.Data;

@Entity
@Table(name = "productos")
@Data
public class Producto {
    @Id
    @Column(name = "IdProducto")
    private Integer id;

    @Column(name = "NombreProducto")
    private String nombre;

    @Column(name = "UnidadesEnExistencia")
    private Integer stock;
}