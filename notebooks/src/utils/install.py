import subprocess
import sys
import pkg_resources
import re

def install_packages_if_missing(packages):
    """
    Install packages only if they are not already installed.
    
    Args:
        packages: List of package names, optionally with version specifiers
                  (e.g., ["numpy", "pandas==1.5.0", "requests>=2.25.0"])
    """
    to_install = []
    
    for package_spec in packages:
        # Parse package name and version specifier
        match = re.match(r'([^=<>!]+)([=<>!].+)?', package_spec.strip())
        if not match:
            print(f"Invalid package specification: {package_spec}")
            continue
            
        package_name = match.group(1)
        version_spec = match.group(2) if match.group(2) else None
        
        try:
            # Check if package is installed
            installed_version = pkg_resources.get_distribution(package_name).version
            
            if version_spec:
                # Check if installed version satisfies the requirement
                requirement = pkg_resources.Requirement.parse(package_spec)
                if installed_version not in requirement:
                    to_install.append(package_spec)
                    print(f"{package_name} {installed_version} doesn't satisfy {version_spec}")
                else:
                    print(f"{package_name} {installed_version} already satisfies {version_spec}")
            else:
                print(f"{package_name} {installed_version} already installed")
                
        except pkg_resources.DistributionNotFound:
            # Package not installed at all
            to_install.append(package_spec)
            print(f"{package_name} not installed")
    
    # Install missing packages
    if to_install:
        print(f"\nInstalling: {', '.join(to_install)}")
        subprocess.check_call([sys.executable, "-m", "pip", "install"] + to_install)
        print("Installation complete!")
    else:
        print("\nAll packages are already installed and satisfy requirements.")