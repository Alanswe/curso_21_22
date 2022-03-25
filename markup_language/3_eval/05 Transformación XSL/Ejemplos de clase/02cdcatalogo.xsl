<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:template match="/">
    <html>
      <head>
        <style>
      table { border:2px black solid;}
      tr { background-color: #9acd32;}
      #pais {text-align:right;}
    </style>
      </head>
      <body>
        <h2>Mi colección de CDs</h2>
        <table>
          <tr>
            <th>Título</th>
            <th>Artista</th>
            <th>País</th>
            <th>Precio</th>
          </tr>
          <!--<xsl:for-each select="catalog/cd[country!='UK']">-->
          <xsl:for-each select="catalog/cd[price&lt;='9.90']">

              <xsl:sort select="artist"/>
              <xsl:if test="country!='UK'">

            <tr>
              <td>
                <xsl:value-of select="title"/>
              </td>
              <td>
                <xsl:value-of select="artist"/>
              </td>
              <td id="pais">
                <xsl:value-of select="country"/>
              </td>
             <td id="pais">
                <xsl:value-of select="price"/>
            </td>
            </tr>
        </xsl:if>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
