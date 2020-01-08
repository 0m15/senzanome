---
title: Noname - a simple static content generator powering this site
date: 2020-01-07
---

If there is something I've ever been bad at, is mantaining my site.
In the last two years, I've been used to develop static sites using Gatsby and react.

So I did for my personal site. I grab a starter with markdown support, then added some cool plugins (like imagesharp) and started building content. But, as every personal site, there can pass months without the site being touched.

So I realized that mantaining my site was like this:

- Launch the dev command
- Something doesn't work
- Look for help on github/stackoverflow
- Remove node_modules and re-install
- Upgrade some dependency
- Seems to work now!
- Made an update to a markdown file
- Everything breaks
- Look for help on github/stackoverflow/etc
- Switch node version
- Yeah! Now it works for real!
- 45 seconds to build...

The 80% of time is consumed by things like updating dependencies, deleting node_modules, having to deal with graphql oddities (for instance, I still can't have optional fields in the frontmatter).

This is not like having a journal/blog. This is a nightmare.

So, the last time I decided to make my fucking own static site generator.
I ended up with a single file and just one dependency (markdown2, proven to be very fast).

It's written in python and it leverages (read it: it hacks) python3 template strings as template engine.

It works, of course, for my needs. 
It's written by me, and it does just what I needed it to do. This is an huge advantage when I'll get back at the source code to add that feature

Plus, the total build time is just about 0.15s on my 2015 MBP.
Gatsby was taking about 1 minute...

Source code is here: http://github.com/0m15/noname

