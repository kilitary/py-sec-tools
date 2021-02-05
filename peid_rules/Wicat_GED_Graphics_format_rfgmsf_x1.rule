rule _Wicat_GED_Graphics_format_rfgmsf
{
	meta:
		description = "Wicat GED Graphics format"
	strings:
		$a = {0D004000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
