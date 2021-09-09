Add-Type -AssemblyName PresentationFramework

$interface = "eth0"             # WSL should be running eth0
$ports = @(8080, 2202, 9999);   # List as many ports as necessary
$reset_on_exit = $True          # If $True, all port forwards will be deleted on exit

$ifconfig = bash.exe -c "ifconfig $interface | grep 'inet '"

$WSLip = $ifconfig -match '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}';

# If there are any connection issues, and ifconfig does not return an IP address, the script should end here
if($WSLip) {
  $WSLip = $matches[0]   
} else {
  echo "ifconfig did not return a valid IP"
  exit;
}

# This script has be be run as Administrator
If (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {   
  $arguments = "& '" + $myinvocation.mycommand.definition + "'"
  Start-Process powershell -Verb runAs -ArgumentList $arguments
  Break
}

for ($i = 0; $i -lt $ports.length; $i++) {
  $port = $ports[$i];
  Invoke-Expression "netsh interface portproxy add v4tov4 listenport=$port connectport=$port connectaddress=$WSLip";
  Invoke-Expression "netsh advfirewall firewall add rule name=$port dir=in action=allow protocol=TCP localport=$port";
}

Invoke-Expression "netsh interface portproxy show v4tov4";

if($reset_on_exit) {
  pause;
  Invoke-Expression "netsh interface portproxy reset";
}
