from datasource.ib_connector import IBConnector

def main():
    connector = None
    
    try:
        while True:
            # take input from terminal logic
            
            # receive position / account P&L data logic
            connector = IBConnector()
            connector.connect('127.0.0.1', 7496, 0)
            connector.reqPnLSingle(0, account_no, "", 8314);

            connector.run()          
    except Exception as e:
        if connector:
            connector.disconnect()

        main()

if __name__ == '__main__':
    main()