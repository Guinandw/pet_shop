#import pdfkit as pdf
from .models import Orden, Orden_detalle
from django.utils import dateformat

def encabezado(orden:Orden):
    if orden.no_factura:
        no_fac = orden.no_factura
    else:
        no_fac = 'PENDIENTE'
    enc = f'''
        <html>
            <head>
                <meta name="pdfkit-page-size" content="Legal"/>
                <meta name="pdfkit-orientation" content="Landscape"/>
                <style>
                .encabezado \u007b
    				margin-left: 10px;
					backgroun-color:crimson;

		\u007d
				.ml-10 \u007b
    				margin-left: 10px;
					

		\u007d
               
                </style>
            </head>
         <section class="ftco-section ftco-cart">
			<div class="container">
				<div class="row">
    			<div class="col-md-12 ftco-animate">
                    <h3 class="text-center mt-5 text-primary" >DETALLES DE ENVIO </h3>
    				<div class="cart-list">
	    				<table class="table">
						    <thead class="thead-primary ">
						      <tr class="text-center encabezado">
						        <th class="ml-10">Fecha</th>
						        <th class="ml-10">Factura</th>
                                <th class="ml-10">Estado</th>
						        <th class="ml-10">Total</th>
						      </tr>
						    </thead>
						    <tbody>
								
						      <tr class="text-center mt-5">
						        <th class="product-name">{dateformat.format(orden.fecha, 'Y-m-d H:i:s' )}</th>
                                <th class="product-name">{no_fac}</th>
                                <th class="product-name">{orden.estado.upper()}</th>
						        <th class="product-name">{orden.total}</th>
						      </tr><!-- END TR-->
							  

							 
						    </tbody>
						</table>
      <br>
      <br>
      <br>
                        <table class="table">
						    <thead class="thead-primary">
						      <tr style:'background-color:crimson;'>
						        <th>Datos de Envio</th>
						        <th style:'text-align:left;'>Descripción</th>
						      </tr>
						    </thead>
						    <tbody>
								
						      <tr class="ml-10">
						        <th style:'backgroun-color:crimson;'>Nombre:</th>
                                <th style:'text-align:left;'>{orden.nombre}</th>
						      </tr><!-- END TR-->
							  <tr class="ml-10">
						        <th style:'text-align:center;'>Apellido:</th>
                                <th style:'text-align:left;'>{orden.apellido}</th>
						      </tr><!-- END TR-->
                              <tr class="ml-10">
						        <th style:'text-align:center;'>Direccion:</th>
                                <th style:'text-align:left;'>{orden.direccion}</th>
						      </tr><!-- END TR-->
                              <tr class="ml-10">
						        <th style:'text-align:center;'>Ciudad:</th>
                                <th style:'text-align:left;'>{orden.ciudad}</th>
						      </tr><!-- END TR-->
							 <tr class="ml-10">
						        <th style:'text-align:center;'>Telefono:</th>
                                <th style:'text-align:center;'>{orden.telefono}</th>
						      </tr class="ml-10><!-- END TR--><tr class="text-center mt-5">
						        <th class="product-name">Usuario:</th>
                                <th class="product-name">{orden.cliente.username}</th>
						      </tr><!-- END TR-->
						    </tbody>
						</table>
      
       <br>
      <br>
      <br>
      
      		<table class="table">
						    <thead class="thead-primary">
						      <tr class="text-center">
						        <th class="ml-10">Producto</th>
						        <th class="ml-10">Cantidad</th>
              					<th class="ml-10">Precio Unitario</th>
                                <th class="ml-10">Descuentos</th>
						        <th class="ml-10">Subtotal</th>
						      </tr>
						    </thead>
							<tbody>

    '''
    return enc

def agg_detalle(orden_detalle:Orden_detalle, encabezado:str):

	encabezado += f'''
 		 
								
						      <tr class="text-center mt-5">
                                <th style:'text-align:left;'>{orden_detalle.producto.nombre}</th>
                                <th style:'text-align:left;'>{orden_detalle.cantidad}</th>
                                <th style:'text-align:left;'>{orden_detalle.precio_unitario}</th>
                                <th style:'text-align:left;'>{orden_detalle.descuento}</th>
                                <th style:'text-align:center;'>{orden_detalle.subtotal}</th>
						      </tr><!-- END TR-->
						
   
   	'''
	return encabezado


 
def agg_finalbody(encabezado):
    
    encabezado += '''
    
					    </tbody>
						</table>
    
    				  </div>
    			</div>
    		</div>
			</div>
		</section>
    '''
    
    return encabezado