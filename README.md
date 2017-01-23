# STK-INF4000 Web Scraping Repository

The contents of this repository were created mainly by `scrapy`'s
`startproject` function, calling

    scrapy startproject stk_inf4000

We can then proceed to generate a spider like so:

     scrapy genspider stk_inf_gh "dhesse.github.io/stk_inf_scraping/example.html"

All we need to do is populate the `parse` function in the spider that
is now saved at [stk_inf4000/spiders/stk_inf_gh.py][stkgh].

## docs

The [docs](docs) folder contains the pages that we are going to
scrape, available [here][p1] and [here][p2].

# Downloading

You can download the code using the green button above, or use `git`,
calling

    git clone git@github.com:dhesse/stk_inf_scraping.git


[stkgh]: stk_inf4000/spiders/stk_inf_gh.py
[p1]: https://dhesse.github.io/stk_inf_scraping/example.html
[p2]: https://dhesse.github.io/stk_inf_scraping/example2.html
