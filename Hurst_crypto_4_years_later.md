# Hurst exponent in Crypto (4 years later)

The [Hurst exponent](https://en.wikipedia.org/wiki/Hurst_exponent) can be used to determine the fractal dimension of a time series, that is if a series of data over time exhibits some kind of [fractal](https://en.wikipedia.org/wiki/Fractal) behavior. It compares the series with itself, and there are three possible outcomes:
- 0.5, the data is random;
- between 0 and 0.5, the data is negatively correlated;
- > 0.5 and < 1, the data is positively correlated.


If you've thought about applying it to Bitcoin and friends, you've probably stumbled into [this article](https://quantdare.com/demystifying-the-hurst-exponent/) from 2018 which tries to replicate [another paper](https://www.sciencedirect.com/science/article/pii/S0275531917309200)'s findings about market efficiency in four major (at the time) cryptocurrencies.

Given four years have passed, I've decided to try and replicate the results with more data, starting with the same code of the article (since no code is available in the paper). The conclusions in 2018 where mainly two:
- the three methods used for approximating the Hurst exponent  (DSOD, R/S, DMA) don't yield the same result consistently, so they're somewhat unreliable;
-  market efficiency in cryptocurrencies couldn't be asserted based on the kind of analysis done in the paper (which only focused on the R/S method for approximating the Hurst exponent).

The code needed a slight modification because the API used to retrieve prices limits its results to only 2000 data points at a time, so two calls are needed to get the full 2013-2022 range of price data. You can find it on [GitHub](https://github.com/fedeb95/crypto_persistence).

Let's first plot BTC, ETH, LTC, and DASH prices up to date (16/05/2022).

![Plot of prices up to 2022](https://github.com/fedeb95/crypto_persistence/raw/main/images/plot_prices_2022.png)

By looking at it, it would seem that at least BTC and ETH follow some kind of fractal pattern. But let's try and approximate the Hurst exponent with the three methods used in the article, first an all the data available.

![Table of Hurst exponents on all data up to 2022](https://github.com/fedeb95/crypto_persistence/raw/main/images/hurst_table.png)

Now the old data, for comparison:

![Table of Hurst exponents from the article](https://github.com/fedeb95/crypto_persistence/raw/main/images/hurst_table_old.png)

The difference isn't very clear, for instance while for BTC the three methods have a lower variability, for ETH the difference in estimations has increased. 

Let's go on and plot a Hurst exponent calculated over the previous 300 days at intervals of 50 days:

![Plot of rolling Hurst exponent](https://github.com/fedeb95/crypto_persistence/raw/main/images/plot_rolling_hurst.png) 

While the DSOD and DMA methods exhibit a pretty random behavior, the R/S method (the one also used originally by Hurst) seems a bit more consistent, now that we have more data points, especially for BTC. 

If we stick to R/S analysis, the Hurst exponent should be somewhere between 0.5 and 0.7 for BTC, 0.5-0.7 for ETH, 0.4-0.7 for DASH and LTC.

Can we conclude that BTC and ETH are somewhat fractal, up to now? I can't be really sure, we may need to wait for the next big swing up or down. Or for many years of random prices.

Now let me challenge the methodology a bit: parameters for computing the Hurst exponent seem to have been chosen rather arbitrarily, not only in the web article, which was just trying to replicate the original paper results, but by that paper itself, which in turn quotes [this article](https://virtusinterpress.org/IMG/pdf/10-22495cocv11i2c5p4.pdf) in which it's clearly stated that the 300 days rolling window was chosen after some trial and error because other windows exhibited too much variability in results. Furthermore, that paper analyzed stock prices during a crisis, so a completely different thing (we're analyzing cryptocurrencies without any crisis - except for that period in 2020/21).

This of course isn't enough to revert the paper conclusions: given the data and the methods used we can't neither confirm neither deny that cryptocurrency prices are fractal neither prove or refuse the efficient market hypothesis. 

For the sake of it, let's do the same calculations over the four major crypto excluding BTC and ETH (by market capitalization, at the time of writing). This are BNB, ADA, XRP and SOL.

![4 major altcoins rolling Hurst](https://github.com/fedeb95/crypto_persistence/raw/main/images/4_major_altcoins_rolling_hurst.png)

The results are pretty much the same.

Let's try, for instance, with a rolling window of 600 days:

![Plot of rolling Hurst exponent over 600 days](https://github.com/fedeb95/crypto_persistence/raw/main/images/plot_rolling_hurst_600.png)

The results with the R/S method are better, not much with the others. This makes me question either the other methods or the original R/S analysis. Should we go and invest everything in crypto because it will always go up? Should we dump every crypto we hold and start hating on crypto? As often happens with science, we are a bit more skeptical in regard to both positions and this kind of analysis.
