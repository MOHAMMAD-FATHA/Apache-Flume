To write python code for getting live stock data using the link provided(python3)

Generate API(Application programming interface) key from following link: https://www.alphavantage.co/

Get the required url and python code for the stock data from following link: https://www.alphavantage.co/documentation/#

Create a .env file in VS Code and declare your API key in that. Create a Stock.py file and write the python code.

Create a configuration file stock.conf in cd apache-flume-1.9.0-bin/conf.

Run the following command to send the python source to hdfs:

bin/flume-ng agent –conf ./conf/ -f conf/flume.conf -n StockDataAgent -Dflume.root.logger=DEBUG

Note: Set the configuration file name and agent name accordingly.

Open localhost:9870 to see the transferred file:
