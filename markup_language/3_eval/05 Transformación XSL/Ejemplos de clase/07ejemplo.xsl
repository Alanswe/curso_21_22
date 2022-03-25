<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0"> 
 <xsl:variable name="IVA" select="16"/>
 
<xsl:template match="/">

 <h1>Ejemplo de aplicación de IVA (<xsl:value-of select="$IVA"/>%)</h1>
<xsl:apply-templates/>
</xsl:template>

  


  <xsl:template match="producto">
  <h2><strong>Nombre producto</strong>: <xsl:value-of select="denominacion"/></h2>
  <p>Precio sin IVA:<xsl:value-of select="precio"/> €</p>
<xsl:variable name="precioConIVA" select="precio+precio*$IVA div 100"/>
<p>Precio con IVA: <strong><xsl:value-of select='$precioConIVA'/>€</strong></p>
<p>Precio con IVA (redondeado a 2 decimales): <strong><xsl:value-of select='format-number( round(100*$precioConIVA) div 100 ,"##0.00" )'/>€</strong></p>
  </xsl:template>
</xsl:stylesheet>
