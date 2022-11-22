from btc import BTCDaemon


class PPCDaemon(BTCDaemon):
    name = "PPC"
    DEFAULT_PORT = 5011

    def load_electrum(self):
        import electrum_ppc

        self.electrum = electrum_ppc


if __name__ == "__main__":
    daemon = PPCDaemon()
    daemon.start()
