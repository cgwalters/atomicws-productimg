%global pixmaptarget %{_datadir}/lorax/product/usr/share/anaconda/pixmaps
%global pixmapsource %{_datadir}/anaconda/pixmaps/workstation

Name:           fedora-productimg-workstation
Version:        22
Release:        1%{?dist}
Summary:        Installer branding and configuration for Fedora Workstation

# Copyright and related rights waived via CC0
# http://creativecommons.org/publicdomain/zero/1.0/
License:        CC0

BuildArch:      noarch

Conflicts:      fedora-productimg-cloud, fedora-productimg-server

%description
This package contains differentiated branding and configuration for Fedora
Workstation for use in a product.img file for Anaconda, the Fedora
installer. It is not useful on an installed system.

%prep

%build

%install

install -m 755 -d %{buildroot}%{pixmaptarget}

for image in \
  sidebar-bg.png sidebar-logo.png topbar-bg.png
do
 ln -sf %{pixmapsource}/$image %{buildroot}%{pixmaptarget}
done


%files
%dir %{_datadir}/lorax/product/usr/share/anaconda
%dir %{_datadir}/lorax/product/usr/share
%dir %{_datadir}/lorax/product/usr
%dir %{pixmaptarget}
%{pixmaptarget}/*.png

%changelog
* Fri Nov  7 2014 Matthew Miller <mattdm@fedoraproject.org> 22-1 
- bump to 22 for rawhide

* Thu Nov  6 2014 Matthew Miller <mattdm@fedoraproject.org> 21-2
- conflict with the other fedora-productimg packages

* Thu Nov  6 2014 Matthew Miller <mattdm@fedoraproject.org> 21-1
- Change license to CC0

* Thu Nov  6 2014 Matthew Miller <mattdm@fedoraproject.org> 21-0
- Initial creation for Fedora 21
