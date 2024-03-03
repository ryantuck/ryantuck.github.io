## DNS Setup for pointing to replit

_Saving for posterity, despite moving to GitHub Pages and it being much easier to configure._

With my domain registrar, I couldn't redirect all bare traffic from `ryantuck.io` to repl.it, so I had to set up `www` forwarding and then set up a secondary redirect.

### `www.ryantuck.io` > `ryantuck.repl.co`

Set up `CNAME` pointing `www.ryantuck.io` to some long `{hash}.repl.co` address

### `ryantuck.io` > `www.ryantuck.io`

Set up naked domain forwarding (`ryantuck.io` to `www.ryantuck.io`) via [wwwizer](http://wwwizer.com/naked-domain-redirect) by pointing the main `A` record to their provided IP address of `174.129.25.170`.

This was such a relief after slogging through dozens of "well actually DNS doesn't work that way here's how it does work blah blah blah" Stack Overflow posts. Just point stuff here and it Just Works. Beautiful. Have no clue how secure that is.
