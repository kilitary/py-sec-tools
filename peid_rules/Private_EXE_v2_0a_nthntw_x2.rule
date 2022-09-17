rule _Private_EXE_v2_0a_nthntw
{
	meta:
		description = "Private EXE v2_0a"
	strings:
		$a = {53E8????????5B8BC32D}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
