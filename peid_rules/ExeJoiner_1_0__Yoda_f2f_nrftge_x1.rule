rule _ExeJoiner_1_0__Yoda_f2f_nrftge
{
	meta:
		description = "ExeJoiner 1_0 __ Yoda f2f"
	strings:
		$a = {68001040006804010000E8390300000500104000C6005C6804010000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
