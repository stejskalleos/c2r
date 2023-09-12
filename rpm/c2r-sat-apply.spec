Name:     c2r-sat-apply
Summary:  Convert2RHEL Satellite Appliance
Version:  0.0.2
Release:  1.el8
License:  GPL
Group:    Unspecified
URL:      http://www.redhat.com

Requires:         bash
Requires(post):   /bin/sh
Requires(postun): /bin/sh

BuildRoot: ~/rpmbuild/
BuildArch: noarch

Source0: 00-init.sh
Source1: 01-prep.sh
Source2: 02-install.sh

%description
Setup Satellite yay!

# prep prepares the sources for building.
# This is where sources are unpacked and
# possible patches applied, and other similar activies could be performed.
# %prep

# The primary function of %setup is to set up the build directory
# for the package, typically unpacking the package’s
# sources but optionally it can just create the directory.
# %setup

# patch is used to apply patches on top of the just unpacked pristine sources.
# %patch

# In %build, the unpacked (and configured) sources are compiled to binaries.
%build

# install is where the compiled binaries are installed
# into the build root.
%install
mkdir -p %{buildroot}/tmp/convert2rhel
cp %{SOURCE0} %{buildroot}/tmp/convert2rhel
cp %{SOURCE1} %{buildroot}/tmp/convert2rhel
cp %{SOURCE2} %{buildroot}/tmp/convert2rhel

%files
%attr(0754, root, root) "/tmp/convert2rhel/00-init.sh"
%attr(0754, root, root) "/tmp/convert2rhel/01-prep.sh"
%attr(0754, root, root) "/tmp/convert2rhel/02-install.sh"

# Runs after the installation of files.
%post -p /bin/sh

/tmp/convert2rhel/00-init.sh
/tmp/convert2rhel/01-prep.sh
/tmp/convert2rhel/02-install.sh

%changelog

* Tue Sep 12 2023 Stejskal Leos <lstejska@redhat.com>  0.0.2
Bla bla bla progress

* Tue Aug 15 2023 Stejskal Leos <lstejska@redhat.com>  0.0.1
First package!

