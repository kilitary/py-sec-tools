rule _Windows_9x_User_password_file_xrdlui
{
	meta:
		description = "Windows 9x User password file"
	strings:
		$a = {E3828596}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
