# Tienda Online

Este proyecto es una aplicación web de una tienda online que permite a usuarios registrados actuar como clientes o vendedores según su rol asignado.

## Funcionalidades

### Roles de Usuario
- **Admin**: Puede gestionar usuarios y productos.
- **Vendedor**: Puede gestionar su tienda, productos, y ver sus ventas.
- **Cliente**: Puede ver tiendas y productos, agregar productos al carrito, realizar compras, y ver su historial de pedidos.

### Funcionalidades Principales

#### Registro y Autenticación
- Los usuarios pueden registrarse como clientes o vendedores.
- Inicio de sesión autenticado según el rol del usuario.

#### Clientes
- Pueden ver listado de tiendas y productos.
- Añadir productos al carrito y proceder al checkout para realizar compras.
- Ver historial de pedidos.

#### Vendedores
- Gestionar su tienda: crear, editar y actualizar información.
- Gestionar productos: agregar, editar, y eliminar productos.
- Ver su perfil de vendedor y estadísticas de ventas.

#### Administradores
- Gestionar usuarios: crear, editar y eliminar usuarios.
- Gestionar productos globalmente: crear, editar y eliminar productos de todas las tiendas.

### Seguridad
- Acceso restringido a vistas según el rol del usuario.
- Redireccionamiento adecuado al intentar acceder a vistas no autorizadas.
- Gestión de errores 404 personalizados para vistas no encontradas.

## Modelos

### Usuario (User)
- Campos: username, email, role (choices: 'customer', 'vendor', 'admin'), created_at, image_url.

### Tienda (Store)
- Campos: name, description, address, google_maps_link, email, user (FK a User), created_at, image_url.

### Producto (Product)
- Campos: name, description, price, stock, store (FK a Store), category.

### Carrito de Compras (ShoppingCart) y Ítems del Carrito (CartItem)
- Modelos para gestionar productos en el carrito antes de realizar una compra.

### Pedidos (Orders) e Ítems de Pedido (OrderItem)
- Modelos para gestionar pedidos y productos asociados a cada pedido.

### Promociones (Promotion)
- Modelos para gestionar promociones aplicadas a productos.

## Diseño Funcional

### Vistas Principales
Las vistas se encuentran sin diseño ya que al ser un trabajo colaborativo, darle diseño fue tarea de otro miembro del equipo

- **Inicio (store_list)**: Listado de tiendas y productos.
- **Detalle de Producto (product_detail)**: Información detallada de un producto específico.
- **Carrito de Compras (cart_view)**: Vista del carrito con productos seleccionados.
- **Checkout (checkout_views)**: Proceso de compra con ingreso de datos de envío y pago.
- **Historial de Pedidos (order_history)**: Vista para clientes para ver sus pedidos anteriores.
- **Gestión de Tienda (manage_store)**: Vista para vendedores para gestionar su tienda.
- **Gestión de Productos (vendor_products)**: Vista para vendedores para gestionar sus productos.
- **Perfil de Vendedor (vendor_profile)**: Información estática de la tienda del vendedor.
- **Panel de Vendedor (vendorHome)**: Dashboard del vendedor con enlaces a gestionar tienda, productos y perfil.
