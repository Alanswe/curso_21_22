<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:template match="/">
    <html>
    <head>
      <style>
      table {border-collapse: collapse;}
      th { border:2px black solid;}
        td { text-align:center; border:2px black solid;}
        .precio1 {background-color:#FF0000;}
        .precio2  {background-color:#00FF00;}
        .precio3  {background-color:#0000FF;}
        tr td:nth-child(3) { text-align:right;}
      </style>
    </head>
    <body>
    <h1>Mi biblioteca</h1>
    <table>
      <tr><th>Título</th><th>Autor</th><th>Precio</th></tr>
      <xsl:for-each select="libreria/libro">
      <tr>
          <xsl:choose>
            <xsl:when test="precio &lt; 12.50">
              <td class="precio1"><xsl:value-of select="titulo"/></td>
              <td class="precio1"><xsl:value-of select="autor"/></td> 
              <td class="precio1"><xsl:value-of select="precio"/></td>               
            </xsl:when>
            <xsl:when test="precio &lt; 25.50">
              <td class="precio2"><xsl:value-of select="titulo"/></td>
              <td class="precio2"><xsl:value-of select="autor"/></td>
              <td class="precio2"><xsl:value-of select="precio"/></td>   
            </xsl:when>     
            <xsl:otherwise>
              <td class="precio3"><xsl:value-of select="titulo"/></td>
              <td class="precio3"><xsl:value-of select="autor"/></td>
              <td class="precio3"><xsl:value-of select="precio"/></td>   
            </xsl:otherwise>   
        </xsl:choose>
      </tr>
      </xsl:for-each>
    </table>
    </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
