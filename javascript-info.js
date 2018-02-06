/* 
The following JavaScript would be run in a browser!
Features of JS:
 - Runs in most modern webbrowsers
 - Written within HTML and can be ran directly from a webpage
 - Designed to make webpages 'alive'
 - Scripts do not need to be compiled to be ran
 - Runs within a JavaScript virtual machine
   Chrome uses the V8 JS VM, Firefox uses SpiderMonkey
 - Files usually end in .js
*/

console.log("Hello World!");

function whatsYourName(msg) {
	var temp = prompt(msg);
	return name;
}

var name;
name = whatsYourName("What's your name, user?");
if (name == "Albert") {
	console.log("Hey Albert!");
} else {
	console.log(name + " is such a lovely name!");
}