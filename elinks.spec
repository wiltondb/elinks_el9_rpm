%define rescue %{nil}
Name: elinks
Summary: A text-mode Web browser.
Version: 0.10.1
Release: 1
Source: http://elinks.or.cz/download/elinks-%{version}.tar.bz2
Source1: http://links.sourceforge.net/download/docs/manual-0.82-en.tar.bz2
Patch0: elinks-noegd.patch
Patch1: elinks-0.10.1-utf_8_io-default.patch
Patch2: elinks-0.10.1-pkgconfig.patch
Patch3: elinks-0.4.2-getaddrinfo.patch
Patch4: elinks-sysname.patch
Patch5: elinks-0.10.1-xterm.patch
Group: Applications/Internet
URL: http://elinks.or.cz/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: autoconf, automake, openssl-devel, pkgconfig
License: GPL
Provides: webclient
Obsoletes: links
Provides: links

%description
Links is a text-based Web browser. Links does not display any images,
but it does support frames, tables and most other HTML tags. Links'
advantage over graphical browsers is its speed--Links starts and exits
quickly and swiftly displays Web pages.

%prep
%setup -q -a 1 -n %{name}-%{version}

# Prevent crash when HOME is unset (bug #90663).
%patch0 -p1 -b .noegd

# UTF-8 by default
%patch1 -p1 -b .utf_8_io-default

%patch2 -p1 -b .pkgconfig

# Make getaddrinfo call use AI_ADDRCONFIG.
%patch3 -p1 -b .getaddrinfo

# Don't put so much information in the user-agent header string (bug #97273).
%patch4 -p1 -b .sysname

# Fix xterm terminal: "Linux" driver seems better than "VT100" (#128105)
%patch5 -p1 -b .xterm

aclocal
automake -a
autoconf

%build
export CFLAGS="$RPM_OPT_FLAGS $(getconf LFS_CFLAGS)"
%configure %{?rescue:--without-gpm} --without-x
%if "%{rescue}" != ""
perl -pi -e "s,-O2,-O2 -Os,g" Make* */Make*
%endif
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
ln -s elinks $RPM_BUILD_ROOT%{_bindir}/links
ln -s elinks.1 $RPM_BUILD_ROOT%{_mandir}/man1/links.1
rm -f $RPM_BUILD_ROOT%{_datadir}/locale/locale.alias
%find_lang elinks

%clean
rm -rf $RPM_BUILD_ROOT

%files -f elinks.lang
%defattr(-,root,root)
%doc README SITES TODO manual-0.82-en
%{_bindir}/links
%{_bindir}/elinks
%{_mandir}/man1/links.1*
%{_mandir}/man1/elinks.1*
%{_mandir}/man5/*

%changelog
* Fri Jan 28 2005 Karel Zak <kzak@redhat.com> 0.10.1-1
- sync with upstream; stable 0.10.1

* Thu Oct 14 2004 Karel Zak <kzak@redhat.com> 0.9.2-2
- the "Linux" driver seems better than "VT100" for xterm (#128105)

* Wed Oct  6 2004 Karel Zak <kzak@redhat.com> 0.9.2-1
- upload new upstream tarball with stable 0.9.2 release

* Mon Sep 20 2004 Jindrich Novy <jnovy@redhat.com> 0.9.2-0.rc7.4
- 0.9.2rc7.
- changed summary in spec to get rid of #41732, #61499

* Mon Sep 13 2004 Tim Waugh <twaugh@redhat.com> 0.9.2-0.rc4.3
- Avoid symbol clash (bug #131170).

* Fri Aug  6 2004 Tim Waugh <twaugh@redhat.com> 0.9.2-0.rc4.2
- 0.9.2rc4.

* Mon Jul 12 2004 Tim Waugh <twaugh@redhat.com> 0.9.2-0.rc2.2
- Fix elinks -dump -stdin (bug #127624).

* Thu Jul  1 2004 Tim Waugh <twaugh@redhat.com> 0.9.2-0.rc2.1
- 0.9.2rc2.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun  2 2004 Tim Waugh <twaugh@redhat.com> 0.9.1-3
- Build with LFS support (bug #125064).

* Fri May 28 2004 Tim Waugh <twaugh@redhat.com> 0.9.1-2
- Use UTF-8 by default (bug #76445).

* Thu Mar 11 2004 Tim Waugh <twaugh@redhat.com> 0.9.1-1
- 0.9.1.
- Use %%find_lang.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Dec  8 2003 Tim Waugh <twaugh@redhat.com> 0.4.3-1
- 0.4.3.
- Updated pkgconfig patch.

* Mon Aug 11 2003 Tim Waugh <twaugh@redhat.com> 0.4.2-7.1
- Rebuilt.

* Mon Aug 11 2003 Tim Waugh <twaugh@redhat.com> 0.4.2-7
- Don't require XFree86-libs (bug #102072).

* Tue Jul 22 2003 Nalin Dahyabhai <nalin@redhat.com> 0.4.2-6.2
- rebuild

* Thu Jun 12 2003 Tim Waugh <twaugh@redhat.com> 0.4.2-6.1
- Rebuilt.

* Thu Jun 12 2003 Tim Waugh <twaugh@redhat.com> 0.4.2-6
- Make getaddrinfo call use AI_ADDRCONFIG.
- Don't put so much information in the user-agent header string (bug #97273).

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jun  2 2003 Tim Waugh <twaugh@redhat.com> 0.4.2-4.1
- Rebuild again.

* Mon Jun  2 2003 Tim Waugh <twaugh@redhat.com> 0.4.2-4
- Rebuild.

* Mon May 12 2003 Tim Waugh <twaugh@redhat.com> 0.4.2-3
- Prevent crash when HOME is unset (bug #90663).

* Sun May 04 2003 Florian La Roche <Florian.LaRoche@redhat.de> 0.4.2-2
- use relative symlinks to elinks

* Wed Feb  5 2003 Tim Waugh <twaugh@redhat.com> 0.4.2-1
- 0.4.2 (bug #83273).

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 0.3.2-5
- rebuilt

* Thu Jan 16 2003 Tim Waugh <twaugh@redhat.com>
- Fix URL (bug #81987).

* Tue Jan  7 2003 Nalin Dahyabhai <nalin@redhat.com> 0.3.2-4
- rebuild

* Mon Dec 23 2002 Tim Waugh <twaugh@redhat.com> 0.3.2-3
- Fix bug #62368.

* Thu Dec 12 2002 Nalin Dahyabhai <nalin@redhat.com>
- use openssl's pkg-config data, if available

* Wed Nov 20 2002 Tim Powers <timp@redhat.com> 0.3.2-2
- rebuild on all arches

* Tue Aug 20 2002 Jakub Jelinek <jakub@redhat.com> 0.3.2-1
- update to 0.3.2 to fix the DNS Ctrl-C segfaults
- update URLs, the project moved
- include man page

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jan 24 2002 Tim Powers <timp@redhat.com>
- rebuilt against new openssl

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan  2 2002 Preston Brown <pbrown@redhat.com> 0.96-4
- cookie fix

* Thu Sep 13 2001 Bernhard Rosenkraenzer <bero@redhat.com> 0.96-3
- Save some more space in rescue mode

* Wed Jul 18 2001 Bernhard Rosenkraenzer <bero@redhat.com> 0.96-2
- Add the links manual from links.sourceforge.net (RFE #49228)

* Tue Jul  3 2001 Bernhard Rosenkraenzer <bero@redhat.com> 0.96-1
- update to 0.96

* Fri Jun 22 2001 Nalin Dahyabhai <nalin@redhat.com>
- actually run make in build phase

* Tue Jun 12 2001 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment

* Fri Mar  2 2001 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment

* Tue Jan  9 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 0.95

* Mon Jan  1 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 0.94 final

* Sun Dec 24 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- pre9

* Mon Dec 10 2000 Preston Brown <pbrown@redhat.com>
- Upgraded to pre8.

* Tue Dec  5 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 0.94pre7
- Minor fixes to the specfile (s/Copyright:/License:/)
- merge rescue stuff

* Fri Nov 24 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 0.94pre5

* Wed Nov 15 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 0.94pre4

* Tue Oct 24 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 0.94pre1

* Wed Aug  2 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 0.92 (needed - prior versions won't display XHTML properly)

* Thu Jul 20 2000 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment to work around bugs

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Thu Jun 15 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 0.84

* Sun Jun 11 2000 Preston Brown <pbrown@redhat.com>
- provides virtual package webclient.

* Thu Jan  6 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- initial RPM
