$("#add_rows").click(function() {
      // each click on the `+` button adds a row to the table
      $("#data_container tbody").append(`<tr><td><input type="text"></td><td><input type="text"></td><td><input type="text"></td></tr>`);
    });
    $("#submit_rows").click(function() {
      // `obj` for storing the inputs, and the `n` to make unrepeated keys
      var obj = {}, n = 0;
      // loop over the rows
      $("#data_container tbody tr").each(function(ind, tr) {
        // add an array to the object
        obj[`r${n}`] = [];
        // loop over the inputs of this row
        $(this).find("input").each(function(ind, input) {
          // add the value of the input to the array and make sure to remove any semicolon since
          // we will use it to seperate the inputs
          var val = input.value.replace(/;/g, "");
          obj[`r${n}`].push(val);
        });
        // no need for the array, just join it to a string of values separated by semicolons
        obj[`r${n}`] = obj[`r${n}`].join(";");
        // increase the value of `n`
        n++;
      });
      // log the object to the console so you can see what we are sending
      console.log(obj);
      // send the data to the server, see the console for a logging message for success
      $.post("http://127.0.0.1:5000", obj, (data, status) => console.log("Status: " + status));
    });
