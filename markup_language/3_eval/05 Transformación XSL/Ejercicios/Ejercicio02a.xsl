<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  
  <xsl:template match="/">
    <xsl:apply-templates select="centro/ciclos/ciclo/nombre" />
  </xsl:template>

  <xsl:template match="centro/ciclos/ciclo/nombre">
    <p><xsl:value-of select="." /></p>
  </xsl:template>
</xsl:stylesheet>
