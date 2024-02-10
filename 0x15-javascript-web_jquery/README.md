# JavaScript - Web jQuery

## Resources:

- https://learn.jquery.com/ajax/

* https://api.jquery.com/

* https://jquery.com/

* https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong

* [summary in videos](https://www.youtube.com/watch?v=0tEW8rB1bbU&list=PLoYCgNOIyGACnrXwo5HMCfOH9VT05znGv&index=7)

* https://jquery-tutorial.net/ajax/the-get-and-post-methods/

* [api documentation](https://oscarotero.com/jquery/)

* https://jquery-tutorial.net/dom-manipulation/the-append-and-prepend-methods/

* https://jquery-tutorial.net/dom-manipulation/getting-and-setting-css-classes/

* https://jquery-tutorial.net/dom-manipulation/getting-and-setting-content/

* Using elements, ID's and classes

* [what's js ](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)

## General:

To make a GET request using jQuery's AJAX method, you can follow this example:

```javascript
// Make a GET request to a specific URL
$.ajax({
  url: "https://api.example.com/data", // Replace with your URL
  method: "GET", // Specify the HTTP method (GET in this case)
  success: function (response) {
    // Handle the successful response here
    console.log("Response:", response);
  },
  error: function (xhr, status, error) {
    // Handle errors here
    console.error("Error:", error);
  },
});
```

Explanation of the parameters:

- `url`: The URL to which the request will be made.
- `method`: The HTTP method to be used (`GET` in this case).
- `success`: A function to be called if the request succeeds. It will receive the response data as a parameter.
- `error`: A function to be called if the request fails. It will receive the XMLHttpRequest object, a string describing the type of error that occurred, and an optional exception object.

You can customize the URL, and you may also add other parameters such as `data` for sending additional data with the request, `dataType` for specifying the expected data type of the response, and more depending on your specific requirements.

To make a POST request using jQuery's AJAX method, you can follow this example:

```javascript
// Data to be sent in the POST request (if any)
var postData = {
  key1: "value1",
  key2: "value2",
};

// Make a POST request to a specific URL
$.ajax({
  url: "https://api.example.com/post-endpoint", // Replace with your URL
  method: "POST", // Specify the HTTP method (POST in this case)
  data: postData, // Data to be sent in the request body
  success: function (response) {
    // Handle the successful response here
    console.log("Response:", response);
  },
  error: function (xhr, status, error) {
    // Handle errors here
    console.error("Error:", error);
  },
});
```

Explanation of the parameters:

- `url`: The URL to which the request will be made.
- `method`: The HTTP method to be used (`POST` in this case).
- `data`: The data to be sent in the request body. It can be a plain object, a string, or a serialized form.
- `success`: A function to be called if the request succeeds. It will receive the response data as a parameter.
- `error`: A function to be called if the request fails. It will receive the XMLHttpRequest object, a string describing the type of error that occurred, and an optional exception object.

You can customize the URL, the data to be sent in the request body (`postData` in this case), and other parameters such as `dataType` for specifying the expected data type of the response, `contentType` for specifying the content type of the request, and more depending on your specific requirements.

To listen or bind to DOM events using jQuery, you can use the `.on()` method or shortcut methods such as `.click()`, `.submit()`, `.keydown()`, etc. Here's how you can do it:

1. Using `.on()` method:

```javascript
// Bind a click event to all elements with class "my-button"
$(".my-button").on("click", function () {
  // Event handler function
  console.log("Button clicked!");
});
```

2. Using shortcut methods:

```javascript
// Bind a click event to all elements with class "my-button"
$(".my-button").click(function () {
  // Event handler function
  console.log("Button clicked!");
});
```

Here's another example of binding to the submit event of a form:

```javascript
// Bind a submit event to the form with id "my-form"
$("#my-form").on("submit", function (event) {
  // Prevent the default form submission behavior
  event.preventDefault();

  // Event handler function
  console.log("Form submitted!");
});
```

In all these examples:

- `$(".my-button")` selects all elements with class "my-button". You can use any valid CSS selector to target specific elements.
- `.on()` method attaches an event handler to selected elements. It takes two arguments: the event type (e.g., "click", "submit", "keydown", etc.) and the event handler function.
- Event handler function is the function that gets executed when the event occurs. You can perform any desired action within this function.
- The `event` parameter in the event handler function contains information about the event (e.g., event type, target element, etc.). You can use it if needed, for example, to prevent default behavior using `event.preventDefault()`.

These are basic examples. You can bind to many other events such as mouse events (`mouseenter`, `mouseleave`), keyboard events (`keydown`, `keyup`), form events (`submit`, `change`), and more.

## More Info

### Import JQuery

<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
