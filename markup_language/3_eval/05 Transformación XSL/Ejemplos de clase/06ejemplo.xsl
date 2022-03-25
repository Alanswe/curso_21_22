<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<!-- ESTRUCTURA PRINCIPAL -->
  <xsl:template match="/">
  <html>
  <head>
    <style>
    p { font-weight: bold;}
    div p:nth-child(1)::before {content:"*";}
    div p:nth-child(2) { text-indent:35px;}
  #titulo {color:#ff0000;}
  #artista {    color:#00ff00;}
    </style>
  </head>
  <body>
  <h2>Mi colección de CDs</h2>
  <main>
  <xsl:apply-templates/> <!-- se incluyen todas  las plantillas que se definan posteriormente -->
  </main>
  </body>
  </html>
</xsl:template> 
<!-- FIN de la ESTRUCTURA PRINCIPAL -->

<xsl:template match="cd"> <!-- se define  la plantilla para el elemento CD -->
  <div>
  <xsl:apply-templates select="title"/> <!-- se indica se incluya la plantilla del elemento title -->
  <xsl:apply-templates select="artist"/>
   <xsl:value-of select="country"/>
  </div>
</xsl:template>

<xsl:template match="title"> <!-- se define  la plantilla para el elemento title -->
<p>
  Título: <span id="titulo">
  <xsl:value-of select="."/></span> <!-- con el . hacemos referencia al lugar del árbol que hemos indicado con match -->
</p>
</xsl:template>

<xsl:template match="artist"><!-- se define  la plantilla para el elemento artist -->
<p>
  Artista: <span id="artista">
  <xsl:value-of select="."/></span> <!-- con el . hacemos referencia al lugar del árbol que hemos indicado con match -->
</p>
</xsl:template>

</xsl:stylesheet>