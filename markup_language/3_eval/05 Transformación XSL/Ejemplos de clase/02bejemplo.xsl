<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

  <xsl:template match="CentroRecreativo"> <!-- de esta forma no hay que ir arrastrando CentroRecreativo/-->
<xsl:for-each select="Miembro">

    <p>Bienvenido <xsl:value-of select="Nombre"/></p>
    
    <xsl:if test="@nivel='premier'">
		  Por ser miembro especial le ofrecemos lo siguiente.....
		</xsl:if>

    <xsl:if test=" @nivel='basica'">
		  Le recordamos que si asciende su membresía a <strong>premier</strong> obtiene.....
		</xsl:if>
		
</xsl:for-each>
</xsl:template>

</xsl:stylesheet>
