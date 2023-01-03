1..255 | ForEach-Object { $response = [System.Net.NetworkInformation.Ping]::Ping("10.0.$_.1") if ($response.Status -eq "Success") { Write-Output "10.0.$_.1 is online" } }
