Name:		rocm-cmake
Version:	10.0.0
Release:	1
Summary:	CMake modules for working with ROCm
License:	MIT
Group:		Development/Tools
URL:		https://github.com/ROCm/rocm-cmake
Source0:	https://github.com/ROCm/rocm-cmake/archive/refs/tags/therock-10.0.tar.gz#/rocm-cmake-therock-10.0.tar.gz
BuildArch:	noarch

BuildSystem:	cmake
BuildRequires:	rocm-rpm-macros
# Upstream defaults CMAKE_INSTALL_PREFIX to /opt/rocm; OM cmake macros force /usr

%description
CMake modules (ROCmCMakeBuildTools) used by most ROCm library packages.
Header/tooling only — no compiled code.

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_datadir}/rocm
%{_datadir}/rocmcmakebuildtools
# cmake also installs a copy of LICENSE under %%{_docdir}/rocm-cmake
%exclude %{_docdir}/rocm-cmake/LICENSE
