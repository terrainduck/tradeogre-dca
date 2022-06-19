# TradeOgre DCA

## About
This is a little script i intend to use to Dollar Cost Average through the bear market. You may use it and or modify it as much as you want. While I personally find this to be very useful it's quite self explanatory that I take no responsibility whatsoever if this script creates any unintended consequences. Use at your own risk.

## Setup
To get started, clone the repo to some Linux system with constant access to the internet, for exampel a VPS.

Copy the file `config.example.json` to `config.json` and paste in your API keys from TradeOgre. In the array "markets" you can add the trading pairs where you want to Dollar cost average. `quantity` is the quantity of crypto to crate a buy order for. Please try it out with a relatively small amount first. `maxPrice` is your maximum market price for accumulation. The buy order will only be created if there are sell orders below your maxiumum price.

Then set up a cronjob with the command `python3 <pathToTheRepo>/main.py >> <pathToTheRepo>/dca.log`. You can for instance set up the cronjob to run every 24 hours or every hour. You will be able to view the results of the script in the log file. If you see buy orders created in your TradeOgre account it works.

## Contact
If you have any questions or feedback, send an email to mathilda1337@tutanota.com

