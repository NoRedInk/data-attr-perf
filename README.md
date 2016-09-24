Tool to test the lengh limits of `data-*` attributes.

```
# assumes you're using some sort of ruby version manager
bundle install
bundle exec ruby testapp.rb
```

and access http://localhost:4567/?w=10&d=10&h=10

Your browser will try to parse a JSON string inside a `data-*` attribute.
You will know the parsing is over when your browser tells you:

> Hello w10 x h10 x d10 worlds!

The length of the JSON string is controlled by the query params.

To generate a set of static pages for testing in various browsers:

```
# with testapp.rb running:
python3 cache.py
ls cache
w10000xh10xd10.html    	w1000xh10xd10.html     	w100xh100xd100.html    	w10xh10000xd10.html    	w10xh10xd100.html      	w1xh100xd1.html
w10000xh1xd1.html      	w1000xh1xd1.html       	w100xh10xd10.html      	w10xh1000xd10.html     	w1xh10000xd1.html      	w1xh1xd100.html
w1000xh100xd100.html   	w100xh1000xd100.html   	w100xh1xd1.html		w10xh100xd10.html      	w1xh1000xd1.html
```

The largest filesize will be around 61M.
