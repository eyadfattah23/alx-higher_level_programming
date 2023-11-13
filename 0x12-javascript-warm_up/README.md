# JavaScript - Warm up

## Notes:-

### Variables:

> For a start, if you write a multiline JavaScript program that declares and initializes a variable, you can actually declare a variable with var **after you initialize it and it will still work**. For example:

```js
myName = "Chris";

function logName() {
  console.log(myName);
}

logName();

var myName;
```

> Secondly, when you use var, you can declare the same variable as many times as you like, but with let you can't. The following would work:

```js
var myName = "Chris";
var myName = "Bob";
```

> But the following would throw an error on the second line:

```js
let myName = "Chris";
let myName = "Bob";
```

> You'd have to do this instead:

```js
let myName = "Chris";
myName = "Bob";
```

> As well as variables, you can declare constants. These are like variables, except that:

>     you must initialize them when you declare them

>     you can't assign them a new value after you've initialized them.

> For example, using let you can declare a variable without initializing it:

```js
let count;
```

> If you try to do this using const you will see an **error**:

```js

const count;
```

> Similarly, with let you can initialize a variable, and then assign it a new value (this is also called reassigning the variable):

```js
let count = 1;
count = 2;
```

> If you try to do this using const you will see an **error**:

```js
const count = 1;
count = 2;
```

> Note that although a constant in JavaScript must always name the same value, you can change the content of the value that it names. This isn't a useful distinction for simple types like numbers or booleans, but consider an object:

```js
const bird = { species: "Kestrel" };
console.log(bird.species); // "Kestrel"
```

> You can update, add, or remove properties of an object declared using const, because even though the content of the object has changed, the constant is still pointing to the same object:

```js
bird.species = "Striated Caracara";
console.log(bird.species); // "Striated Caracara"
```

resources:

> [Module patterns](http://darrenderidder.github.io/talks/ModulePatterns/#/6)

> [**var, let and const explaination**](https://www.youtube.com/watch?v=sjyJBL5fkp8)
