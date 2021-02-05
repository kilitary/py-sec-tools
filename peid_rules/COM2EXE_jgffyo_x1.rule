rule _COM2EXE_jgffyo
{
	meta:
		description = "COM2EXE"
	strings:
		$a = {F0FFFEFF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
