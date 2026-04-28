package com.neptuno.middleware;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;
import org.springframework.boot.autoconfigure.orm.jpa.HibernateJpaAutoConfiguration;
import org.springframework.boot.autoconfigure.jdbc.DataSourceTransactionManagerAutoConfiguration;

// Aquí excluimos todo lo que tenga que ver con bases de datos para que el test pase "en seco"
@SpringBootTest
@EnableAutoConfiguration(exclude = {
    DataSourceAutoConfiguration.class, 
    DataSourceTransactionManagerAutoConfiguration.class, 
    HibernateJpaAutoConfiguration.class
})
class MiddlewareApplicationTests {

    @Test
    void contextLoads() {
        // Al excluir las configuraciones de BD, este test solo valida que 
        // tus controladores y lógica de Java no tengan errores de sintaxis.
    }

}