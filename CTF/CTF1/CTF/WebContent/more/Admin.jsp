<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"
    import="java.io.*"
    import="java.security.*"
    import="java.math.*"
    %>
<!DOCTYPE HTML>
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
	</head>
	<body>
		<% 
			String plaintext1 = request.getParameter("user");
			String plaintext = request.getParameter("pwd");
			String query;
			String role="";
			boolean tru=false;
			String loc="C:/Users/chuny/workspace/CTF/WebContent/check.txt";
			
			try (BufferedReader br = new BufferedReader(new FileReader(loc))) {
			    String line1;
			    String line2;
			    int num=6;
			    int i=1000;
			    String[] a={"NSA","FBI","ABC","123","456","MD5","AES","CIA"};
			    MessageDigest m = MessageDigest.getInstance("MD5");
			    m.reset();
			    m.update(plaintext.getBytes());
			    byte[] digest = m.digest();
			    BigInteger bigInt = new BigInteger(1,digest);
			    String hashtext = bigInt.toString(16);
			    while(hashtext.length() < 32 ){
			      hashtext = "0"+hashtext;
			    }
			    m.reset();
			    m.update(plaintext1.getBytes());
			    digest = m.digest();
			    bigInt = new BigInteger(1,digest);
			    String hashtext1 = bigInt.toString(16);
			    while(hashtext1.length() < 32 ){
			      hashtext1 = "0"+hashtext1;
			    }
			    
			    while ((line1 = br.readLine()) != null&&(line2 = br.readLine()) != null) {
					if (hashtext1.equals(line1)&&hashtext.equals(line2)){
						i=arrange(i);
						out.println("<h1>WELCOME "+plaintext1+" !</h1>");
						String ua = request.getHeader( "User-Agent" );
						num=i;
						if (ua.equals(a[num])){
							out.println("Heres the flag \"flag{f_l_a_g}\"");
							tru=true;
						}else{
							out.print("NO FLAG FOR YOU");
							tru=true;
						}
					}
						
					}
						
			    
			
				} catch (Exception e) {
				System.err.println("Error: " + e);
				}
			if(tru==false){
				out.print("<h1>Oops! Wrong password!</h1><p><a href=\"../index.jsp\">Return to Civilisation</a></p>");
					
			}
		%>
<%!int arrange(int i){
	i=3;
    i=(i/2);
    i=i*5-9*-11;
    i=i/2*4;
    i=i-200;
    i=i/2;
	return i;
} %>
	</body>
</html>