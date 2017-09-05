<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"
    import="java.util.Random"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Cookie Agency</title>

  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
</head>
<p style="font-size:3em;background-color:powderblue;">INTERNATIONAL COOKIE AGENCY &#x1F36A;<br></p>
<body background="others/cookiecookie.jfif">
<%  Random randomGenerator = new Random();
	int randomInt = randomGenerator.nextInt(10000);
	Cookie k=new Cookie("CookieDonationBox","0");
	k.setMaxAge(10000000);
	response.addCookie(k);
%>
<br><br><br>
<div class="col-md-4 col-md-offset-4"  style="background-color:#CCD1D1 ;">
<h1>AGENT LOGIN PAGE</h1>
<form action="Admin.jsp" method="post"class="form-inline">
					<label>User name: </label>
					<br>
					<input type="text" class="form-control"name="user">
					<br><br>
					<label>Password: </label>
					<br>
					<input type="password" class="form-control"name="pwd">
					<input value=<%=randomInt%> name="num" type="hidden">
					<input class="btn btn-success" type="submit" name="btnSubmit" value="Login">
					<br><br>
</form>
</div>
</body>
</html>










