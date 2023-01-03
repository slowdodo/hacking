1..255 | ForEach-Object { Test-NetConnection -ComputerName "10.0.$_.1" -InformationLevel Quiet }
