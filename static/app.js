window.CLASSES = ["Negative", "Positive"]
window.CSS_CLASSES = ["danger", "success"]

var progressBar = {
  show: function() {
    $(".progress").fadeIn();
  },
  hide: function() {
    $(".progress").hide();
  }
};

var prediction = {
  set: function(q, predictedValue, predictedClass) {
    $("#predicted_class").text(CLASSES[predictedClass]);
    $("#predicted_value").text(predictedValue);
    $("#predicted_query").text(q);
    prediction.toggleClasses(predictedClass);
  },
  toggleClasses: function(predictedClass) {
    $("#prediction").removeClass("alert-" + CSS_CLASSES[1 - predictedClass]);
    $("#prediction").addClass("alert-" + CSS_CLASSES[predictedClass]);
  },
  show: function() {
    $("#prediction").fadeIn();
  },
  hide: function() {
    $("#prediction").hide();
  }
};

var examples = {
  show: function() {
    $(".examples").fadeIn(1500);
  },
  add: function(q, predicted, real) {
    $line = $("<tr>")
    $div = $("<div>").html(q)
    $line.append($("<td class='text'>").text($div.text()));
    $line.append(examples.classCell(predicted));
    $line.append(examples.classCell(real));
    $(".example_items").append($line);
  },
  addAll: function(items) {
    $.each(items, function(i, item){
      predicted = parseInt(item.predicted);
      real = parseInt(item.real);
      examples.add(item.q, predicted, real);
    });
  },
  classCell: function(value){
    return $("<td>").text(CLASSES[value]).addClass(CSS_CLASSES[value]);
  }
}

$(function(){
  $("#predict_form").submit(function(e){
    e.preventDefault();
    prediction.hide();
    progressBar.show();

    $.getJSON("/predict",  $(this).serialize()).
      always(function(){
        progressBar.hide();
      }).
        done(function(data) {
          var predictedClass = parseInt(data.predicted_class);
        prediction.set(data.q, data.prediction, predictedClass);
        prediction.show();
      });
  });

  $.getJSON("/examples").done(function(data) {
    examples.addAll(data.items);
    examples.show()

    $("td.text").click(function(){
      $(this).toggleClass("hover",10000)
    });
  });
});
