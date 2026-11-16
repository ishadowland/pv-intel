<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://security.unboundcompute.com/php-object-injection -->
<!-- fetched_at: 2026-11-17 07:12:36 -->
<!-- sha256: 5ac0e167d4c5f8327117822fc5f5380aadc17937d36a8633714f570ae6563020 -->

PHP Object Injection: When unserialize() Builds the Attacker's Objects

Skip to content

PHP Object Injection: When unserialize() Builds the Attacker’s Objects

Written by

UnboundCompute

in

Deep Dives

PHP object injection happens the moment an application calls unserialize() on data an attacker can shape. When you search for php object injection , what you are really asking about is this handoff: a serialized string from a cookie, a hidden form field, or an API body gets turned back into live PHP objects. The attacker never types a line of code. They choose which classes get built and what values the properties hold, and the methods PHP runs on its own do the rest.

This is one flavor of insecure deserialization , and it is the one PHP developers meet first. To see how single objects get strung together into a full exploit, read the deserialization gadget chain overview once you finish here.

What php object injection actually is

PHP can flatten an object into a string with serialize() and rebuild it with unserialize() . The serialized form is plain text that lists the class name, each property name, and each value. Here is a small user object:

O:4:"User":1:{s:4:"name";s:5:"alice";}
Read it as: an object of class User with one property, name , set to the string alice . Now picture an app that stores this in a cookie and calls unserialize($_COOKIE['session']) on every request. The attacker controls that cookie. They can hand back a serialized string that names a different class and sets any property to any value they like. PHP will build that object. That is the whole bug.

The magic methods that fire on their own

Building an object would be harmless if nothing ran. The problem is that PHP calls certain methods automatically at set points in an object’s life. These are the magic methods, and three of them matter most for this bug:

__wakeup() runs the instant an object is rebuilt by unserialize() .

__destruct() runs when the object is thrown away at the end of the request.

__toString() runs when the object is used where a string is expected, such as in a log line or an echo.

The attacker does not need to write these methods. They only need a class, already loaded somewhere in the app or its libraries, whose magic method does something useful. Consider a logging helper that ships with a project:

class Logger {
public $logfile;
public $data;
public function __destruct() {
file_put_contents($this->logfile, $this->data);
}
}
On its own this class is fine. But if an attacker can make unserialize() build a Logger with logfile set to shell.php and data set to a small block of PHP, then the end of the request writes a working web shell to disk. No call to eval , no call to system , just a file write that the author never meant to expose to user input.

Composing a POP chain out of classes already loaded

One class with a tidy magic method is a gift. Real targets are rarely that kind. So attackers build a chain. The technique is called property oriented programming, and the idea is to reuse method calls that already exist in the codebase instead of injecting new code.

It starts with a magic method, say a __destruct() that calls $this->handler->close() . The attacker sets handler to an object of a second class whose close() method does something more interesting, which in turn calls a method on a third object, and so on. Each step is legal code. The attacker only supplies the property values that decide which objects sit at each link. String enough together and the final step reaches a dangerous call. This is exactly the shape covered in pop chains and property oriented programming , and the role of the automatic triggers is spelled out in magic methods in deserialization attacks .

The attacker never ships code. They ship a data structure that tells objects you already trust to call each other in an order you never intended.

Because the gadgets live in libraries and framework code, the same chain often works across many apps that share a dependency. A serialized payload built for one project can land on another that pulls in the same package.

Where the untrusted data sneaks in

The sink is always unserialize() , but the source hides in ordinary places:

Session or preference data kept in a cookie and deserialized on each request.

A hidden field in a form that the server round trips through unserialize() .

An API that accepts a serialized blob because an older client sent one.

Cache entries or message queue payloads that an attacker can write to.

A second path needs no visible unserialize() call at all. The phar:// stream wrapper triggers deserialization of archive metadata when a filesystem function touches an attacker path. That route gets its own treatment in phar deserialization .

How to fix php object injection

The fixes are direct, and they stack.

Do not call unserialize() on anything a user can influence. This is the rule that closes the bug. If the data came from a client, treat it as hostile.

Use a data only format instead. For structured data, json_encode() and json_decode() move plain arrays and values with no class names and no magic methods. JSON cannot build a Logger , so it cannot start a chain.

If you must accept serialized PHP, allowlist the classes. Since PHP 7, unserialize() takes an options array:
$data = unserialize($input, ['allowed_classes' => false]);
Passing false forbids every class, so the result holds only plain values. If you truly need a few types, name them instead: ['allowed_classes' => ['SafeDTO']] .

Sign the data if it has to make a round trip. Attach an HMAC that the server checks before it deserializes. If the signature fails, the input never reaches the sink.

For more bugs that turn trusted input handling against an app, browse the injection and input category.

This is the kind of flaw that hides behind clean looking code, because the dangerous call is one line and the gadgets live in libraries you did not write. UnboundCompute reasons about whether untrusted input can actually reach an unserialize() call and fire a chain of magic methods, rather than matching a fixed pattern. Read how that works on our about page .

Frequently asked questions

What causes PHP object injection?

It happens when an application calls unserialize() on data a user can control, such as a cookie or form field. PHP rebuilds whatever classes the serialized string names and sets their properties to attacker chosen values. If any rebuilt class has a magic method that does something useful, the attacker gets to steer it.

Which PHP magic methods are used in these attacks?

The common ones are __wakeup(), which runs when an object is rebuilt, __destruct(), which runs when the object is discarded at the end of the request, and __toString(), which runs when the object is used as a string. Attackers pick classes whose magic methods reach a dangerous call, then chain them into a POP chain.

How do I prevent PHP object injection?

Do not call unserialize() on any input a user can influence. Use json_decode() for structured data instead, since JSON carries no class names. If you must accept serialized PHP, pass allowed_classes set to false so no objects are built, and sign round tripped data with an HMAC the server checks first.

Is json_decode safe from object injection?

Yes for this bug. json_decode() produces plain arrays and scalar values and cannot instantiate arbitrary classes, so it cannot fire a magic method or start a gadget chain. That is why moving session and preference data to JSON closes the object injection path that unserialize() opens.

Put an autonomous researcher on your own systems

UnboundCompute is an autonomous security researcher that reasons about how an application fits together and proves the access control and injection bugs it finds. We are opening a small number of founding design partner seats: private early access pointed at a staging target you choose, and a say in what it looks for. If your team ships software worth pressure testing, apply to the design partner program .

More posts

Detecting HTTP Request Smuggling Safely

October 11, 2026

Connection State Request Smuggling

October 11, 2026

Request Tunnelling Attack Explained

October 11, 2026

Capturing Other Users Requests With a Desync

October 11, 2026
