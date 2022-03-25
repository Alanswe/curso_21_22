<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output method="html" version="4.0" encoding="UTF-8" indent="yes" />
  
 
  <xsl:template match="/">
    <html>
      <head>
        <style>
          body {
             width:60%;
             border:3px black solid;
             margin: 0 auto;}

          h1 { 
            text-transform: uppercase; 
            text-align:center;}
            ol { width: 60%; margin:0 auto;}
        </style>
      </head>
      <body>
        <main>
          <h1><xsl:value-of select="centro/@nombre" /></h1>
          <xsl:apply-templates select="centro/ciclos" />
        </main>
      </body>
    </html>
  </xsl:template>


  <xsl:template match="centro/ciclos">
    <ol>
      <xsl:apply-templates select="ciclo" >
        <xsl:sort select="nombre" order="descending" />
      </xsl:apply-templates>
    </ol>
  </xsl:template>


  <xsl:template match="centro/ciclos/ciclo">
    <li><xsl:apply-templates select="nombre" /> (<xsl:apply-templates select="grado" />)</li>
  </xsl:template>


  <xsl:template match="centro/ciclos/ciclo/nombre">
    <xsl:value-of select="." />
  </xsl:template>


  <xsl:template match="centro/ciclos/ciclo/grado">
    <strong><xsl:value-of select="." /></strong>
  </xsl:template>
</xsl:stylesheet>

