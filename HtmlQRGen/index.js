<script src="https://cdnjs.cloudflare.com/ajax/libs/qrious/4.0.2/qrious.min.js"></script>
// <script>
var qr;
(function() {
	qr = new QRious({
		element: document.getElementById("qr-code"),
		size: 200;
		value: "https://mrlearner.com"
	});
})();


function generateQRCode() {
	var qrtext = document.getElementById("qr-text").value;
	document.getElementById("qr-result").innerHTML = "QR Code for " + qrtext + ":";
	alert(qrtext);
	qr.set({
		background: "green",
		backgroundAlpha: 0.0,
		foreground: "blue",
		foregroundAlpha: 0.8,
		padding: 25,
		size: 200
	});
}

// </script>