rule _Windows_Write_file_dkveyb
{
	meta:
		description = "Windows Write file"
	strings:
		$a = {??BE000000AB000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
