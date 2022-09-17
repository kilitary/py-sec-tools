rule _COM2EXE_ktzjqz
{
	meta:
		description = "COM2EXE"
	strings:
		$a = {F0FFFEFF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
