#delShutter {
background: #333;
position: fixed;
top: 0;
left: 0;
height: 100%;
width: 100%;
opacity: .8;
z-index: 1000;
}

#delInfo {
border: 6px double #4b4;
width: 320px;
position: fixed;
left: 50%;
padding: 5px 15px;
/* 320 / 2 + 15 + 6 */
margin-left: -181px;
background: #eee;
z-index: 1001;
top: 90px;
font: 15px georgia;
}

#delForm {
padding: 0;
margin: 0;
}

#delInfo table {
width: 100%;
margin: 0;
}

#delTitle {
font: 35px georgia, serif;
color: #444;
padding: 0;
border-bottom: 3px solid #4b4;
margin-bottom: 5px;
}

.delSmall {
font-size: 0.8em;
padding: 0;
}


#delInfo input[type=text] {
padding: 2px;
display: block;
width: 90%;
border: 2px inset #ddd;
}

#delInfo input[type=button] { background: #ddd; }

#delInfo input[type=button],#delInfo input[type=submit] {
padding: 2px 6px;
font: 17px verdana;
margin: 3px;
}

#delSubmit {
border: 2px outset #4b4;
background: #4b4;
color: #fff;
}

#delInfo input[type=submit]:active {
border: 2px inset #4b4;
}

#delCenter {
text-align: center;
padding-top: 10px;
}
