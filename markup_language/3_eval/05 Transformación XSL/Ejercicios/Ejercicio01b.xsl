<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

  <xsl:template match="ciclos">
    <html>
        <xsl:apply-templates />
    </html>
  </xsl:template>

  <xsl:template match="ciclo">
     <p><xsl:value-of select="nombre"/></p>
  </xsl:template>
<!-- 
  <xsl:template match="/">
    <xsl:for-each select="centro/ciclos/ciclo">
      <p><xsl:value-of select="nombre"/></p>
    </xsl:for-each>
  </xsl:template>
  -->
</xsl:stylesheet>
