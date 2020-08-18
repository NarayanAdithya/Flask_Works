var n=1;
$("#add_rows").click(function() {
      // each click on the `+` button adds a row to the table
      $("#data_container tbody").append("<tr><td><input name='Task"+n+"1' type=\"text\"></td><td><input name='Start"+n+"2'  type=\"date\"></td><td><input name='Finish"+n+"3' type=\"date\"></td></tr>");
      n++;
    });
