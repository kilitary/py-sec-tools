rule _WarWind_Save_file_jlpmjq
{
	meta:
		description = "WarWind Save file"
	strings:
		$a = {574152534156}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
