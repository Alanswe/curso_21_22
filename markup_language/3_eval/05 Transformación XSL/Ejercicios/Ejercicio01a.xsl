<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:template match="ciclo">
        <xsl:value-of select="nombre"/>
        <br/>
  </xsl:template>


 <!-- <xsl:template match="/">
    <xsl:for-each select="centro/ciclos/ciclo">
      <xsl:value-of select="nombre"/>
      <br/>
    </xsl:for-each>
  </xsl:template>-->
</xsl:stylesheet>
