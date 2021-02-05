rule _Windows_9x_registry_file_hsfvnc
{
	meta:
		description = "Windows 9x registry file"
	strings:
		$a = {43524547}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
