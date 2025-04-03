Name:		rocm-cmake
Version:	6.3.3
Release:	1
Source0:	https://github.com/ROCm/rocm-cmake/archive/refs/tags/rocm-%{version}.tar.gz
Summary:	CMake modules for working with ROCm
URL:		https://github.com/ROCm/rocm-cmake
License:	MIT
Group:		Development/Tools
BuildArch:	noarch
BuildRequires:	cmake
BuildSystem:	cmake

%description
CMake modules for working with ROCm

%files
%doc %{_docdir}/rocm-cmake
%{_datadir}/rocm
%{_datadir}/rocmcmakebuildtools
