rule _tElock_v0_96_qceooy
{
	meta:
		description = "tElock v0_96"
	strings:
		$a = {E959E4FFFF00}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
