PREFIX ?= /usr
SYSCONFDIR ?= /etc
MANDIR ?= $(PREFIX)/share/man

all:
	@echo Run \'make install\' to install stock-shares.

install:
	
	@echo 'Making directories...'
	@mkdir -p $(DESTDIR)$(PREFIX)/bin
	@mkdir -p $(DESTDIR)$(SYSCONFDIR)/stock-shares

	@echo 'Installing binaries...'
	@sed "s|CONFDIR|$(SYSCONFDIR)/stock-shares|g" < stock-shares > $(DESTDIR)$(PREFIX)/bin/stock-shares
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/stock-shares
	@sed "s|CONFDIR|$(SYSCONFDIR)/main-multiple.py|g" < main-multiple.py > $(DESTDIR)$(PREFIX)/bin/main-multiple.py
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/main-multiple.py

	@echo 'installed stock-shares'

uninstall:
	@echo 'Removing files...'
	@rm -rf $(DESTDIR)$(PREFIX)/bin/stock-shares
	@rm -rf $(DESTDIR)$(SYSCONFDIR)/stock-shares
	@rm -rf $(DESTDIR)$(PREFIX)/bin/main-multiple.py
	@rm -rf $(DESTDIR)$(SYSCONFDIR)/main-multiple.py
//grabbed from neofetch "https://github.com/dylanaraps/neofetch/"
