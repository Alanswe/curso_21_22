<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:template match="/">
  <html>
  <head>
    <style>
  #titulo {color:#ff0000;}
  #artista {    color:#00ff00;}
    </style>
  </head>
  <body>
  <h2>Mi colección de CDs</h2>
  <xsl:apply-templates/>
  </body>
  </html>
</xsl:template>

<xsl:template match="cd">
  <main>
  <xsl:apply-templates select="title"/>
  <xsl:apply-templates select="artist"/>
  </main>
</xsl:template>

<xsl:template match="title">
<p>
  Title: <span id="titulo">
  <xsl:value-of select="."/></span>
</p>
</xsl:template>

<xsl:template match="artist">
<p>
  Artist: <span id="artista">
  <xsl:value-of select="."/></span>
</p>
</xsl:template>

</xsl:stylesheet>