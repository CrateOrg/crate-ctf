.PHONY: check clean setrlimit

check: format contents
	make stage1
	make constraints && rm -f x* || (rm -f x* && false)
	@echo $$(cat <(head -1 format) contents <(tail -1 format) | sed -z 's/\n//g') 🥳

clean:
	find -maxdepth 1 -type f -not -name flag -not -name Makefile -not -name .gitignore -delete

format: flag
	grep -oP 'cratectf{|}' $< >$@

contents: flag
	echo -e 'X=$$(subst },,$$(subst cratectf{,,'$$(cat $<)'))\nx:\n\techo $$(X)>$@' | make -sf - x

$(shell (sha1hmac format 2>/dev/null || true) | awk '{print $$1}'): format
	sha1sum format | awk '{print $$1}' > $@

8d7b5bef406384883fe0f30e066339817c05712a: eae2a8e65aa2326a64475835648d846e44d8fdd4
	echo hej > $$(cat $<)

stage2: $(file < eae2a8e65aa2326a64475835648d846e44d8fdd4)
	$(file >$@,$(file < eae2a8e65aa2326a64475835648d846e44d8fdd4))

stage1: $(shell (sha1hmac format 2>/dev/null || true) | awk '{print $$1}')
	make stage2

d=$(shell seq 97 $$(printf %d \'$$(head -c$(1) contents | tail -c1)) | sed -z 's/[0-9]\+\n/a/g')
sub=$(shell echo "$(3)" | sed 's/$(1)/$(2)/')

x$(call d,1)getpgrp x$(call d,2)aaaprctl x$(call d,3)$(call d,3)tuxcall x$(call sub,$(call d,4),,$(call d,6))openat x$(call d,10)$(call d,11)fallocate x$(call d,5)$(call d,8)syncfs x$(call sub,$(call d,1),,$(call d,4))$(call sub,$(call d,2),,$(call d,7))$(call sub,$(call d,3),,$(call d,8))dup3 x$(call d,12)$(call sub,$(call d,7),$(call d,3),$(call d,9))swapoff x$(call d,9)aachroot x$(call sub,$(call d,11),$(call d,6),$(call d,1))socket: contents
	touch $@

setrlimit: contents
	@python -c "$$(echo H4sIACrAN2UAAytKzCxOVQiuLC5JzXWtyCzRyMsvUUjMydGwNLexzS9K0UjWtLE1NDJSSMsvUkhWyMwDooLSEg1NveKSoswCDU1NTS4AwgYiUkQAAAA= | base64 -d | gunzip)" < contents

constraints: setrlimit xaaagetpgrp xaaaaaaaaaaaprctl xaaaaaaaaaatuxcall xaaaaaaaaaaaaaaaaaopenat xaaaaaaaaaaaaafallocate xaaaaaaaaaaaaaaaasyncfs xdup3 xaaaaaaaaaaaaaswapoff xaaaaaaaachroot xaaaaaaaaaaaaaaaaaaaaaasocket
