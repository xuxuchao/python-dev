<html>
<head>
    <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
</head>
<body>


<div id="test-div">
  <p id="test-js">javascript</p>
  <p>Java</p>
</div>

<script>
var js = $("#test-js");
js.text("JavaScript")
js.css("color","#ff0000")
</script>

</body>
</html>

<div id="test-div">
  <p id="test-js">javascript</p>
  <p>Java</p>
</div>

<script>
var js = document.getElementById("test-js");
js.innerText = "JavaScript";
js.setAttribute("style", "color: #ff0000");
</script>
