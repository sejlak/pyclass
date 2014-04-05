html_str = """
<table border=1>
     <tr>
       <th>Number</th>
       <th>Square</th>
     </tr>
     <indent>
     <% for i in range(10): %>
       <tr>
         <td><%= i %></td>
         <td><%= i**2 %></td>
       </tr>
     </indent>
</table>
"""

Html_file= open("test.html","w")
Html_file.write(html_str)
Html_file.close()