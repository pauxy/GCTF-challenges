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
			String nume = request.getParameter("num");
			int numbe=0;
			boolean numb=true;
			try{
				numbe=Integer.parseInt(nume);
			}catch(Exception e){
				numb=false;
			}
			String query;
			String role="";
			boolean tru=false;
			String loc="C:/Users/chuny/workspace/CTF/WebContent/check.txt";
			if(numb){
				try (BufferedReader br = new BufferedReader(new FileReader(loc))) {
				    String line1;
				    String line2;
				    int num=6;
				    int i=numbe;
				    String[] a={"NSA","FBI","ABC","123","456","currently108elements","MD5","AES","CIA","ASD","KKK","GAK","286","420","BLA","ZEI","TXX","howslife?","idunnowhattowrite","d1ff1cul+","3e25y5y0u","1337","hax0r","whatsthis??????","iwonderthelengthofthisarray","magic","magi","mag","ma","mag","magi","magic","nothing","null","true","false","secret","agent","007","nowmuchmore","probablynotthatmuch","goodluck","longarrayislong","idontknowanymore","notascomplicatedasitlooks","orisitdifficult?","OUT","LINE","AVAIL","ABL","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","IWANTZEFLAG","FLAG","FLAGISNICEFLAG?","GIVEFLAGPLEASE","IAMHERE","MAGICALLY","IAMHERE","CHOOSEME","IAMHEREEE","HEREIAM","CHOOSEEMEEE","LINE14","ARRANGEME","WHOISTHEONE?","i am","isitme?","GCTF","admin","member","SHA512","WHATAMIDOING","IS","THIS","ASECR","ET","MESSAGE","???","ORISITNOT","IDONTACTUALLY","KNOW","HOWMANYELEMENTS","INTHIS","ARRAYOF","WORDS","NICESONGS","ILIKE","BADSONGS","IDONT","AN","EYEFO","RAN","EYE","303","8262017","PM","AM","SERVER","LOCA","LH","OST","LAST","ONE","DONE"};
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
							System.out.println(a[num]);
							if (ua.equals(a[num])){
								out.println("Dear authorised agent,<br>");
								Cookie[] all=request.getCookies();
								for(Cookie I:all){
									if(I.getName().equals("CookieDonationBox")){
										int number=0;
										try{
											number=Integer.parseInt(I.getValue());
										}catch(Exception e){
										}
										if(number>0){
											out.println("Sufficiently paid!<br>Heres the flag \"GCTF{w3_ar3_7h3_c00k13_ag3nc9}\"");
										}else{
									    	out.println("you may be real...but you'll have to pay the required cookies to enter!");
										}
									}
								}
								tru=true;
							}else{
								out.print("YOU ARE NOT THE AGENT IM LOOKING FOR! <br>GO AWAY!");
								tru=true;
							}
						}
							
						}
							
				    
				
					} catch (Exception e) {
					System.err.println("Error: " + e);
					}
			}
			if(tru==false){
				out.print("<h1>Oops! Wrong password!</h1><p><a href=\"../index.jsp\">Return to Civilisation</a></p>");
					
			}
		%>
<%!int arrange(int i){
	i=i+3;
	i=(i/2);
    i=i*5-9*-11;
    i=i/2*4;
    i=i-200;
    i=i/2;
    i=i+100;
    i=i%100;
	i=i+20;
	
	if(i!=20){
		return i;
		
	}
	for(int k=0;k<4;k++)
		i=arrange(i);
	i=i+i;
	return i;
} %>
	</body>
</html>