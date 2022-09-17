rule _ASProtect_v1_2_sdcrtq
{
	meta:
		description = "ASProtect v1_2"
	strings:
		$a = {6801??????C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
