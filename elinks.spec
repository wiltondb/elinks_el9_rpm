%define DATE 0.3.2
%define rescue %{nil}
Name: elinks
Summary: text mode www browser with support for frames
Version: 0.3.2
%define rel 1
Release: %{rel}%{rescue}
Source: ftp://ftp.pld.org.pl/software/elinks/elinks-%{version}.tar.bz2
Source1: http://links.sourceforge.net/download/docs/manual-0.82-en.tar.bz2
Patch0: links-0.92-nogpm.patch
Patch1: links-0.96-cookiefix.patch
Group: Applications/Internet
URL: http://elinks.pld.org.pl/
BuildRoot: %{_tmppath}/%{name}-buildroot
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
%setup -q -a 1 -n %{name}-%{DATE}
%if "%{rescue}" != ""
%patch0 -p1 -b .nogpm
autoconf
%endif
%patch1 -p1 -b .cookiefix

%build
%configure
%if "%{rescue}" != ""
perl -pi -e "s,-O2,-O2 -Os,g" Make* */Make*
%endif
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/%{name}-%{version}

%files
%defattr(-,root,root)
%doc README SITES TODO manual-0.82-en
%{_bindir}/links
%{_mandir}/man1/links.1*

%changelog
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
